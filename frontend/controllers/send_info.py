import streamlit as st
import requests

def send_info(topic, mood):
    # st.write(topic, mood)
    try:
        response = requests.get("http://localhost:8000/predict/message")

    except Exception as error:
        st.error(f"Ha ocurrido un error: {error}")