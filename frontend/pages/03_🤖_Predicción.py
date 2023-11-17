import streamlit as st
from assets.styles.css import styles
from controllers.send_info import send_text, send_text_area


def prediction():
    base_url = "https://www.youtube.com/watch?v="
    st.set_page_config(page_title="Predicción Hate", page_icon="🤖", layout="wide")
    st.markdown(styles, unsafe_allow_html=True)

    st.title("🤖 Predicción Hate")

    st.markdown("Escribe a continuación el ID del comentario que deseas predecir")

    topic = st.text_input(label="URL de YouTube", placeholder="ID")
    mood = st.text_area(
        label="Comentario de texto",
        placeholder="Escribe aquí",
    )

    if st.button(label="Predecir", type="primary"):
        if topic:
            if base_url in topic:
                send_text(topic)
            else:
                st.error("Introduce una URL válida de YouTube")
        if mood:
            send_text_area(mood)
        if not topic and not mood:
            st.error("Debes escribir algo para poder predecir")


if __name__ == "__main__":
    prediction()
