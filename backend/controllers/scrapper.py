import os

import googleapiclient.discovery as discovery
import pandas as pd
from dotenv import load_dotenv
from fastapi import Response, status
from googleapiclient.errors import HttpError
from model.model import predict_toxicity, load_model

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
        for comment in comments:
            prediction = predict_toxicity(model, comment)
            if prediction == 1:
                df["Toxicidad"] = "Tóxico"
            else:
                df["Toxicidad"] = "No tóxico"

        # Elimina la columna de indices del dataframe
        df.reset_index(drop=True, inplace=True)
        fastapi_response.status_code = status.HTTP_200_OK
        return df

    except HttpError as error:
        if error.resp.status == 404:
            fastapi_response.status_code = status.HTTP_404_NOT_FOUND
            return f"El video con id {video_Id} no existe"
        return f"Ha ocurrido un error, {error}"
