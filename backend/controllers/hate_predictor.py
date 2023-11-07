from fastapi import Response, status


async def receive_message(response:Response):
    """
    Recibimos a través del endpoint el mensaje desde streamlit
    """
    try:
        return {
            "message": "Todo es correcto"
            }
        response.status_code = status.HTTP_200_OK
    except Exception as error:
        return{
            "message": f"No se pudo realizar la solicitud, {error}"
        }

async def make_prediction(text: str, response:Response):
    """
    Realizamos la predicción
    """
    try:
        print(text)
        return True
        response.status_code = status.HTTP_200_OK

    except Exception as error:
        return{
            "message": f"Hubo un problema, {error}"
        }