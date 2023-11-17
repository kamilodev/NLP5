from controllers import hate_predictor
from fastapi import APIRouter, Response, status

predictor = APIRouter(prefix="/predict", tags=["ML Predictor"])


@predictor.get(
    "/message",
    summary="Enviamos el mensaje que viene por el campo de texto de streamlit",
    response_description="Muestra el mensaje de la predicción",
    status_code=status.HTTP_200_OK,
)
async def receive_message(response: Response):
    return await hate_predictor.receive_message(response)


@predictor.post(
    "/message",
    summary="Recibimos y enviamos la respuesta de Hate Predictor",
    response_description="Respuesta de Hate Predictor",
    status_code=status.HTTP_200_OK,
)
async def make_prediction(text: dict, response: Response):
    return await hate_predictor.make_prediction(text, response)


@predictor.post(
    "/mood",
    summary="Recibimos y enviamos la respuesta de Hate Predictor",
    response_description="Respuesta de Hate Predictor",
    status_code=status.HTTP_200_OK,
)
async def make_mood_prediction(text: dict, response: Response):
    return await hate_predictor.make_mood_prediction(text, response)
