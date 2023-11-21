import os
import pandas as pd
import plotly.express as px
import streamlit as st
from assets.styles.css import styles_analytics as styles
from views.messages import AUTHORS
from dotenv import load_dotenv
from controllers.convert_url import convert_gsheets_url

load_dotenv()
URL_DATA = os.getenv("URL_DATA")


def summary(df):
    total_values = df.shape[0]
    missing_data = df.isnull().sum()
    summary = pd.DataFrame(index=df.columns)
    summary["Unique"] = df.nunique().values
    summary["Missing"] = df.isnull().sum().values
    summary["Missing %"] = ((missing_data / total_values) * 100).round(2)
    summary["Duplicated"] = df.duplicated().sum()
    summary["Types"] = df.dtypes
    return summary


def analisis():
    try:
        url = convert_gsheets_url(URL_DATA)

        st.markdown(styles, unsafe_allow_html=True)
        st.title("📈 Analisis")

        df = pd.read_csv(url)

        st.subheader("Cabeceras del DataFrame")
        st.write("Observamos cuales son las cabeceras a utilizar")
        st.dataframe(df.head(20))

        st.write("")
        st.subheader("Resumen de Datos")
        st.write("Cantidad de Filas y Columnas:")
        st.text(df.shape)
        st.dataframe(summary(df), width=900, height=600)

        st.write("")
        st.subheader("Descripción de Datos")
        st.dataframe(df.describe())

        st.write("")
        st.subheader("Datos Únicos y Porcentaje de Participación")
        st.write(
            "Detectamos los datos unicos y comprobamos que el dataset solo contiene 13 videos distintos pero con distintos comentarios y que la columna IsToxic solo se activa si es que las demás en adelante califican como true , pero no se determina cuantas columnas se activan, simplemente se pone en true sin discriminar si uno, dos o tres se activan , esto nos lleva a preguntarnos ¿Que tan grave es el comentario? ¿Es posible detectar que columnas se activan independientemente?"
        )
        df_unicos = df.drop_duplicates(subset="VideoId")
        st.dataframe(df_unicos, width=900, height=500)
        st.write("")
        st.write(
            "Por tanto vemos el porcentaje de participación de cada columna que determina que IsToxic se active entonces observamos que hay mayor porcentaje de abusivos , provocativos , discurso de odio y racistas. Por otro lado vemos que no hay comentarios sexistas y homofóbicos pero lo dejaremos por si en una posterior version se detectan y se almacenen ahi. Pero no tenemos vision de la cantidad ya que vemos que son 13 videos y no podemos identificar a que videos pertenece cada comentario."
        )

        st.write("")
        st.subheader(
            "Gráfico de Barras: Porcentaje de Participación por Característica"
        )
        columns_names = df.columns.tolist()
        bar_data = {}
        for name in columns_names[1:]:
            bar_data[name] = len(df.loc[df[name] == 1]) / len(df[name])

        bar_df = pd.DataFrame(
            list(bar_data.items()),
            columns=["Porcentaje de participación", "Clasificación de Hate"],
        )
        fig = px.bar(
            bar_df,
            x="Porcentaje de participación",
            y="Clasificación de Hate",
            title="Porcentaje de participación por característica",
            labels={
                "Porcentaje de participación": "Porcentaje de participación",
                "Clasificación de Hate": "Clasificación de Hate",
            },
            width=800,
            height=500,
        )
        st.plotly_chart(fig)

        st.write("")
        st.subheader("Gráfico de Barras: Participación de 'IsToxic'")
        toxic_counts = df["IsToxic"].value_counts()
        data = {"IsToxic": toxic_counts.index, "Conteo": toxic_counts.values}
        toxic_counts_df = pd.DataFrame(data)
        fig = px.bar(
            toxic_counts_df,
            x="IsToxic",
            y="Conteo",
            title='Participación de "IsToxic"',
            labels={"IsToxic": "IsToxic", "Conteo": "Conteo"},
            width=600,
            height=400,
        )
        st.plotly_chart(fig)

        st.write("")
        st.subheader("Gráfico de Barras: Contribución de cada columna en 'IsToxic'")
        toxic_rows = df[df["IsToxic"] == True]
        column_counts = toxic_rows.drop(columns=["IsToxic"]).sum()
        data = {"Columna": column_counts.index, "Conteo": column_counts.values}
        column_counts_df = pd.DataFrame(data)
        fig = px.bar(
            column_counts_df,
            x="Columna",
            y="Conteo",
            title='Contribución de cada columna en "IsToxic"',
            labels={"Columna": "Columna", "Conteo": "Conteo"},
            width=900,
            height=500,
        )
        st.plotly_chart(fig)

        hate_columns = [
            "IsAbusive",
            "IsThreat",
            "IsProvocative",
            "IsObscene",
            "IsHatespeech",
            "IsRacist",
            "IsNationalist",
            "IsSexist",
            "IsHomophobic",
            "IsReligiousHate",
            "IsRadicalism",
        ]

        df["HateNumber"] = df[hate_columns].sum(axis=1)
        df["HatePercentage"] = df["HateNumber"] / len(hate_columns) * 100

        st.write("")
        st.subheader("Visualización de HateNumber")
        fig = px.histogram(
            data_frame=df,
            x=["VideoId"],
            color="HateNumber",
            facet_row=None,
            facet_col=None,
            marginal=None,
            cumulative=False,
        )
        st.plotly_chart(fig)

        st.write("")
        st.subheader("Nueva Columna: HatePercentage")
        st.write("")
        st.write(
            "Al realizar la nueva columna HatePercentage pudimos poner un peso de participación por columna activa por múltiplos de 9 es decir que si una columna se activa será el porcentaje equivalente a 9% , si se activan 2 a 18%, si se activan 3 a 27% y asi sucesivamente."
        )
        df["HatePercentage"] = df[hate_columns].sum(axis=1) / len(hate_columns) * 100
        st.dataframe(df[["IsToxic"] + hate_columns + ["HatePercentage"]])

        st.subheader("Nueva Columna: HateNumber y HatePercentage")
        df["HateNumber"] = df[hate_columns].sum(axis=1)
        df["HatePercentage"] = df["HateNumber"] / len(hate_columns) * 100
        st.dataframe(df[["IsToxic"] + hate_columns + ["HateNumber", "HatePercentage"]])

        st.write("")
        st.subheader("Histograma de HateNumber")
        fig = px.histogram(
            data_frame=df,
            x=["VideoId"],
            color="HateNumber",
            facet_row=None,
            facet_col=None,
            marginal=None,
            cumulative=False,
        )
        st.plotly_chart(fig)

        new_content = {
            "IsToxic": {True: "toxic", False: "Not_toxic"},
            "IsAbusive": {True: "abusive", False: "Not_abusive"},
            "IsThreat": {True: "threat", False: "Not_threat"},
            "IsProvocative": {True: "provocative", False: "Not_provocative"},
            "IsObscene": {True: "obscene", False: "Not_obscene"},
            "IsHatespeech": {True: "hatespeech", False: "Not_hatespeech"},
            "IsRacist": {True: "racist", False: "Not_racist"},
            "IsNationalist": {True: "nationalist", False: "Not_nationalist"},
            "IsSexist": {True: "sexist", False: "Not_sexist"},
            "IsHomophobic": {True: "homophobic", False: "Not_homophobic"},
            "IsReligiousHate": {True: "religious_hate", False: "Not_religious_hate"},
            "IsRadicalism": {True: "radicalism", False: "Not_radicalism"},
        }

        df.replace(new_content, inplace=True)

        st.write("")
        st.subheader("DataFrame con Nuevas Categorías")
        st.dataframe(df.head(11))

        st.write("")
        st.subheader("Reemplazo de Categorías en Columnas Específicas")
        df.replace(new_content, inplace=True)
        st.dataframe(df.head(11))
        st.markdown(AUTHORS, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(
            "Error: El archivo 'youtoxic_english.csv' no se encuentra en el directorio actual."
        )


if __name__ == "__main__":
    analisis()
