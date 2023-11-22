import os

TITLE = "Hate Guardian"

INTRO = """
    Bienvenido a Hate Guardian, una herramienta impulsada por inteligencia artificial para detectar y combatir el discurso de odio en línea. Nuestra misión es fomentar un ambiente digital inclusivo y amigable para todos.
    """

CYBORG = os.path.join(os.path.dirname(__file__), "../assets/images/guardian.png")

AUTHORS = """
    <div class="footer">
        <p>Made with ❤️‍🔥 by <a href="https://www.linkedin.com/in/alexa-montenegro-047b3a252/" target="_blank">Alexa</a> / <a href="https://www.linkedin.com/in/javi-navarro-ai/" target="_blank">Javi</a> / <a href="https://www.linkedin.com/in/miguelmendozaespinoza9a010114a/" target="_blank">Miguel</a> / <a href="https://www.linkedin.com/in/kamilodev/" target="_blank">Camilo</a></p>
    </div>
    """

SIDE_INFO = "Puedes usar nuestro modelo de inteligencia artificial para detectar y combatir el discurso de odio en línea."

FEATURES = """
    👉 Analyze YouTube comments for a video\n
    👉 Classify comments as hate speech or not using a DistilBERT model\n
    👉 View analysis results in an interactive Streamlit dashboard
    """