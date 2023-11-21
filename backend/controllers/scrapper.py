import os

import googleapiclient.discovery as discovery
import pandas as pd
from controllers.translate import translate_text
from dotenv import load_dotenv
from fastapi import Response, status
from googleapiclient.errors import HttpError
from model.model_predict import load_model, predict_toxicity

from . import process_comments

load_dotenv()
model = load_model()
DEV_KEY = os.getenv("DEV")


def scrapper_video(video_Id, fastapi_response: Response):
    try:
        service_name = "youtube"
        version = "v3"

        youtube = discovery.build(service_name, version, developerKey=DEV_KEY)
        video_Id = video_Id.split("v=")[1][0:11]

        all_comments = []

        nextPageToken = None
        while True:
            youtube_response = (
                youtube.commentThreads()
                .list(
                    part="snippet,replies",
                    videoId=video_Id,
                    maxResults=100,
                    order="relevance",
                    pageToken=nextPageToken,
                )
                .execute()
            )

            comments = process_comments.process_comments(youtube_response)
            all_comments.extend(comments)

            nextPageToken = youtube_response.get("nextPageToken")
            if not nextPageToken:
                break

        df = pd.DataFrame(
            all_comments,
            columns=["Autor", "Comentario"],
        )

        comments = df["Comentario"]
        comments = [translate_text(comment) for comment in comments]

        df["Toxicidad"] = None

        for i, comment in enumerate(comments):
            prediction = predict_toxicity(model, comment)
            df.at[i, "Toxicidad"] = "👹 Tóxico" if prediction == 1 else "😇 No tóxico"

        df.reset_index(drop=True, inplace=True)
        fastapi_response.status_code = status.HTTP_200_OK
        return df

    except HttpError as error:
        if error.resp.status == 404:
            fastapi_response.status_code = status.HTTP_404_NOT_FOUND
            return f"El video con id {video_Id} no existe"
        return f"Ha ocurrido un error, {error}"
