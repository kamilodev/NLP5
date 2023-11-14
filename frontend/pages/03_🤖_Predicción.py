import streamlit as st
from assets.styles.css import styles
from controllers.send_info import send_text, send_text_area


def prediction():
    st.set_page_config(page_title="Predicción Hate", page_icon="🤖")
    st.markdown(styles, unsafe_allow_html=True)

    st.title("🤖 Predicción Hate")

    st.markdown("Escribe a continuación el ID del comentario que deseas predecir")

    topic = st.text_input(label="Comentario de YouTube", placeholder="ID")
    mood = st.text_area(
        label="Comentario de texto",
        placeholder="Escribe aquí",
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button(label="Predecir (Topic)", type="primary"):
            send_text(topic)
    with col2:
        if st.button(label="Predecir (Mood)", type="primary"):
            send_text_area(mood)


if __name__ == "__main__":
    prediction()
