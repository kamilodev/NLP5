# Welcome to Hate Guardian Project 👋

Hate Guardian is an AI-powered hate speech detection tool. It allows users to analyze online comments and detect hate speech.

<p align="center">
  <img src="frontend/assets/images/guardian.png" alt="Guardian" width="30%">
</p>

## Installation

The project consists of a frontend built with Streamlit and a backend built with FastAPI.

### Clone the repository:

```bash
git clone https://github.com/AI-School-F5-P2/NLP5.git
```

Create a virtual environment and activate it

<br/>

### To run the frontend:

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

<br/>

### To run the backend:

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

<br/>

## Tech Stack

| **Frontend** |                                                                                                                      |
| ------------ | -------------------------------------------------------------------------------------------------------------------- |
| Streamlit    | ![Streamlit Badge](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) |
| Python       | ![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)          |

<br/>

| **Backend** |                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------- |
| FastAPI     | ![FastAPI Badge](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white) |
| Python      | ![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)    |

<br/>

| **Machine Learning** |                                                                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| TensorFlow           | ![TensorFlow Badge](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)       |
| Transformers         | ![Transformers Badge](https://img.shields.io/badge/Transformers-3399FF?style=for-the-badge&logo=huggingface&logoColor=white)  |
| Scikit-Learn         | ![Scikit-Learn Badge](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) |

<br/>

## Features

-   Analyze YouTube comments for a video
-   Classify comments as hate speech or not using a DistilBERT model
-   View analysis results in an interactive Streamlit dashboard

<br/>

## Description

Hate Guardian allows users to input a YouTube video URL. It will scrape the comments for that video and run them through a hate speech classification model. The results are displayed in a Streamlit dashboard showing each comment and whether it was classified as hate speech.

The goal is to provide an easy way for people to analyze online content and detect hate speech. This allows identifying toxic comments so that action can be taken, such as filtering or removing them.

The project uses a DistilBERT model fine-tuned on a dataset of English YouTube comments labeled for hate speech. The model achieves over 95% accuracy on a test set.

<br/>

## Making Predictions from the Terminal

Navigate to the frontend directory:

```bash
cd frontend
```

<br/>

Run the following command:

```bash
python controllers/print_terminal.py <youtube_url>
```

<br/>

Example:

```bash
python controllers/print_terminal.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

This will scrape the comments from the YouTube URL, make toxicity predictions on each comment using the ML model, and print out the results.

<br/>

You can also make a prediction on a single text input:

```bash
python controllers/print_terminal.py "This is a text input" --mode text
```

The --mode flag allows switching between URL and text input modes.

## Contributors

<table>
  <tr>
    <td align="center">
    <a href="https://github.com/montenegro-28" target="_blank"><img src='https://avataaars.io/?avatarStyle=Circle&topType=LongHairStraight&accessoriesType=Blank&hairColor=BrownDark&facialHairType=Blank&clotheType=BlazerShirt&eyeType=Default&eyebrowType=Default&mouthType=Default&skinColor=Light' width="100px;" alt=""/><br /><sub><b>Alexa</b></sub>
    </td>
    <td align="center">
    <a href="https://github.com/Nicklessss" target="_blank"><img src='https://avataaars.io/?avatarStyle=Circle&topType=ShortHairShortWaved&accessoriesType=Blank&hairColor=BlondeGolden&facialHairType=BeardMajestic&facialHairColor=Platinum&clotheType=BlazerSweater&eyeType=Happy&eyebrowType=DefaultNatural&mouthType=Smile&skinColor=Light' width="100px;" alt=""/><br /><sub><b>Javi</b></sub></a>
    </td>
    <td align="center">
    <a href="https://github.com/migue29" target="_blank"><img src='https://avataaars.io/?avatarStyle=Circle&topType=ShortHairShortFlat&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=Black&eyeType=Wink&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light' width="100px;" alt=""/><br /><sub><b>Miguel</b></sub></a>
    </td>
    <td align="center">
    <a href="https://github.com/kamilodev" target="_blank"><img src='https://avataaars.io/?avatarStyle=Circle&topType=ShortHairShortWaved&accessoriesType=Blank&hairColor=Black&facialHairType=BeardLight&facialHairColor=Black&clotheType=CollarSweater&clotheColor=Heather&eyeType=Close&eyebrowType=Default&mouthType=Twinkle&skinColor=Light' width="100px;" alt=""/><br /><sub><b>Kamilo</b></sub></a>
    </td>
    </tr>
</table>
