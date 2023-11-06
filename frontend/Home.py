import streamlit as st
from assets.styles.css import styles
from views.messages import AUTHORS, CYBORG, INTRO, SIDE_INFO, TITLE


def app():
    st.set_page_config(
        page_title="Hate Guard - Advanced AI Anti-hate",
        page_icon="🛡️",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    st.markdown(styles, unsafe_allow_html=True)

    st.image(CYBORG)

    st.title(TITLE)
    st.markdown(INTRO)
    st.sidebar.info(SIDE_INFO)

    st.header("Installation")
    # st.code("pip install streamlit-toggle", language="bash")
    # st.header("Quickstart")
    # st.code(QUICKSTART, language="python")
    st.markdown(AUTHORS, unsafe_allow_html=True)


if __name__ == "__main__":
    app()
