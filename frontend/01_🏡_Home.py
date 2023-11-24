import streamlit as st
from assets.styles.css import styles
from views.messages import AUTHORS, CYBORG, FEATURES, SIDE_INFO, TITLE


def app():
    st.set_page_config(
        page_title="Hate Guard - Advanced AI anti-hate",
        page_icon="🛡️",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    st.markdown(styles, unsafe_allow_html=True)
    st.image(CYBORG)
    st.title(TITLE)
    st.sidebar.info(SIDE_INFO)

    st.markdown(
        "Hate Guardian is an AI-powered hate speech detection tool. It allows users to analyze online comments and detect hate speech."
    )

    st.header("Installation")
    st.markdown(
        "The project consists of a frontend built with Streamlit and a backend built with FastAPI."
    )

    st.header("Clone the repository:")
    st.code("git clone https://github.com/AI-School-F5-P2/NLP5.git")

    st.markdown("Create a virtual environment and activate it")

    st.write("")
    st.header("To run the frontend:")
    st.code(
        """
        cd frontend
        pip install -r requirements.txt
        streamlit run app.py
    """
    )

    st.write("")
    st.header("To run the backend:")
    st.code(
        """
        cd backend
        pip install -r requirements.txt
        uvicorn main:app --reload
    """
    )

    st.write("")
    st.header("Tech Stack")
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.header("Frontend")

    st.markdown(
        "| | |\n| ------------ | -------------------------------------------------------------------------------------------------------------------- |\n| Streamlit    | ![Streamlit Badge](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) |\n| Python       | ![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)          |"
    )

    st.write("")
    st.header("Backend")
    st.markdown(
        "| | |\n| ----------- | -------------------------------------------------------------------------------------------------------------- |\n| FastAPI     | ![FastAPI Badge](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white) |\n| Python      | ![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)    |"
    )

    st.write("")
    st.header("Machine Learning")
    st.markdown(
        "| | |\n| -------------------- | ----------------------------------------------------------------------------------------------------------------------------- |\n| TensorFlow           | ![TensorFlow Badge](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)       |\n| Transformers         | ![Transformers Badge](https://img.shields.io/badge/Transformers-3399FF?style=for-the-badge&logo=huggingface&logoColor=white)  |\n| Scikit-Learn         | ![Scikit-Learn Badge](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) |"
    )

    st.write("")
    st.header("Features")
    st.markdown(FEATURES)

    st.header("Description")
    st.markdown(
        "Hate Guardian allows users to input a YouTube video URL. It will scrape the comments for that video and run them through a hate speech classification model. The results are displayed in a Streamlit dashboard showing each comment and whether it was classified as hate speech."
    )

    st.markdown(
        "The goal is to provide an easy way for people to analyze online content and detect hate speech. This allows identifying toxic comments so that action can be taken, such as filtering or removing them."
    )

    st.markdown(
        "The project uses a DistilBERT model fine-tuned on a dataset of English YouTube comments labeled for hate speech. The model achieves over 95% accuracy on a test set."
    )

    st.header("Making Predictions from the Terminal")
    st.markdown("Navigate to the frontend directory:")
    st.code("cd frontend")

    st.write("")
    st.markdown("Run the following command:")
    st.code("python controllers/print_terminal.py <youtube_url>")

    st.write("")
    st.markdown("Example:")
    st.code(
        'python controllers/print_terminal.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"'
    )

    st.write("")
    st.markdown(
        "This will scrape the comments from the YouTube URL, make toxicity predictions on each comment using the ML model, and print out the results."
    )

    st.write("")
    st.markdown("You can also make a prediction on a single text input:")

    st.code('python controllers/print_terminal.py "This is a text input" --mode text')

    st.write("")
    st.markdown("The --mode flag allows switching between URL and text input modes.")

    st.header("Contributors")

    contributors = [
        {
            "name": "Alexa",
            "avatar": "https://avataaars.io/?avatarStyle=Circle&topType=LongHairStraight&accessoriesType=Blank&hairColor=BrownDark&facialHairType=Blank&clotheType=BlazerShirt&eyeType=Default&eyebrowType=Default&mouthType=Default&skinColor=Light",
        },
        {
            "name": "Javi",
            "avatar": "https://avataaars.io/?avatarStyle=Circle&topType=ShortHairShortWaved&accessoriesType=Blank&hairColor=BlondeGolden&facialHairType=BeardMajestic&facialHairColor=Platinum&clotheType=BlazerSweater&eyeType=Happy&eyebrowType=DefaultNatural&mouthType=Smile&skinColor=Light",
        },
        {
            "name": "Miguel",
            "avatar": "https://avataaars.io/?avatarStyle=Circle&topType=ShortHairShortFlat&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=Black&eyeType=Wink&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light",
        },
        {
            "name": "Kamilo",
            "avatar": "https://avataaars.io/?avatarStyle=Circle&topType=ShortHairShortWaved&accessoriesType=Blank&hairColor=Black&facialHairType=BeardLight&facialHairColor=Black&clotheType=CollarSweater&clotheColor=Heather&eyeType=Close&eyebrowType=Default&mouthType=Twinkle&skinColor=Light",
        },
    ]

    for contributor in contributors:
        st.markdown(
            f"<br/><img src='{contributor['avatar']}' width='100px' class='contributors' alt='{contributor['name']}'><sub><b>{contributor['name']}</b></sub>",
            unsafe_allow_html=True,
        )

    st.markdown(AUTHORS, unsafe_allow_html=True)


if __name__ == "__main__":
    app()
