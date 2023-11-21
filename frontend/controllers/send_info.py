import pandas as pd
import requests
import streamlit as st

# If you are using a local backend, uncomment the following lines:
# from dotenv import load_dotenv
# load_dotenv()
# URL = os.getenv("URL")

# If you want to deploy your backend in streamlit sharing, uncomment the following lines:
# URL = os.environ["URL"]


def send_text(topic):
    if topic:
        payload = {"topic": topic}
        try:
            response = requests.post(
                "http://127.0.0.1:8000/predict/message?text",
                json=payload,
            )
            if response.status_code == 200:
                result = response.json()
                dataset = pd.DataFrame(result)

                st.write("")
                st.success("¡Hemos hecho scrapping a tu video! 🥳")
                st.write("Numero de comentarios: ", len(dataset))
                st.write("")
                st.dataframe(dataset, width=1600, height=900)
                st.write("")
                st.write(
                    "Numero de comentarios tóxicos: ",
                    dataset["Toxicidad"].values.tolist().count("Tóxico"),
                )
                st.write(
                    "Numero de comentarios no tóxicos: ",
                    dataset["Toxicidad"].values.tolist().count("No tóxico"),
                )
            else:
                st.error(response.json().get("message"))
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")


def send_text_area(mood):
    if mood:
        payload = {"mood": mood}

        try:
            response = requests.post("http://127.0.0.1:8000/predict/mood", json=payload)
            if response.status_code == 200:
                result = response.json()
                mood = payload["mood"]

                st.write("")
                st.write(result["message"])
            else:
                st.error("Error en la solicitud. Inténtalo de nuevo más tarde.")
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")
