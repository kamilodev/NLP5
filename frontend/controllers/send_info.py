import pandas as pd
import requests
import streamlit as st


def send_text(topic):
    if topic:
        payload = {"topic": topic}
        try:
            response = requests.post(
                "http://localhost:8000/predict/message?text", json=payload
            )
            if response.status_code == 200:
                result = response.json()
                print("results: ", result)
                dataset = pd.DataFrame(result)
                st.success(
                    "¡Hemos hecho scrapping a tu video! 🥳 Observa los resultados:"
                )
                st.dataframe(dataset)
            else:
                st.error(response.json().get("message"))
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")
    else:
        st.warning(
            "Por favor, ingresa el ID del comentario para hacer la predicción del tema."
        )


def send_text_area(mood):
    if mood:
        payload = {"mood": mood}

        try:
            response = requests.post("http://localhost:8000/predict/mood", json=payload)
            if response.status_code == 200:
                result = response.json().get("message")
                print("results: ", result)
                st.success(f"Predicción del texto {payload['mood']}: {result}")
            else:
                st.error("Error en la solicitud. Inténtalo de nuevo más tarde.")
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")
    else:
        st.warning(
            "Por favor, ingresa el texto para hacer la predicción del estado de ánimo."
        )
