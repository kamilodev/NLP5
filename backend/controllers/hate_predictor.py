from controllers.translate import translate_text
from fastapi import Response, status
from model.model_predict import load_model, predict_toxicity
from pydantic import BaseModel

from . import scrapper

model = load_model()


class Text(BaseModel):
    topic: str


async def receive_message(response: Response):
    """
    Recibimos a través del endpoint el mensaje desde streamlit
    """
    try:
        return {"message": "Todo es correcto"}
        response.status_code = status.HTTP_200_OK
    except Exception as error:
        return {"message": f"No se pudo realizar la solicitud, {error}"}


async def make_prediction(text, response: Response):
    """
    Realizamos la predicción
    """
    df = scrapper.scrapper_video(text.get("topic"), response)
    if response.status_code == 200:
        response.status_code = status.HTTP_200_OK
        return df.to_dict(orient="records")
    elif response.status_code == 404:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"El video {text.get('topic')} no existe"}


async def make_mood_prediction(text, response: Response):
    """
    Realizamos la predicción
    """
    try:
        text = text.get("mood")
        text_translate = translate_text(text)
        prediction = predict_toxicity(model, text_translate)
        predict_message = "👹 Es Tóxico" if prediction == 1 else "😇 No es tóxico"
        return {"message": f"El mensaje 👉 {text}, {predict_message}"}
        response.status_code = status.HTTP_200_OK

    except Exception as error:
        return {"message": f"Hubo un problema, {error}"}
