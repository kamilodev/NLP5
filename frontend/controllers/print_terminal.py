import argparse

import pandas as pd
import requests


def get_dataset_from_url(url):
    payload = {"topic": url}
    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict/message?text", json=payload
        )
        if response.status_code == 200:
            result = response.json()
            return pd.DataFrame(result)
        else:
            print(f"Error: {response.json().get('message')}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_prediction_from_text(text):
    payload = {"mood": text}
    try:
        response = requests.post("http://127.0.0.1:8000/predict/mood", json=payload)
        if response.status_code == 200:
            result = response.json()
            mood = payload["mood"]
            print(result["message"])
            print("\n")
        else:
            print("Error en la solicitud. Inténtalo de nuevo más tarde.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Get dataset from URL or text prediction"
    )
    parser.add_argument("input", help="URL or text to send for prediction")
    parser.add_argument(
        "--mode",
        choices=["url", "text"],
        default="url",
        help="Mode of operation (url or text)",
    )

    args = parser.parse_args()
    input_data = args.input
    mode = args.mode

    print("\033c")
    print("\nEstamos trabajando en las predicciones, espera un momento...\n")

    if mode == "text":
        get_prediction_from_text(input_data)
    elif mode == "url":
        dataset = get_dataset_from_url(input_data)
        if dataset is not None:
            toxic = dataset["Toxicidad"].values.tolist().count("👹 Tóxico")
            no_toxic = dataset["Toxicidad"].values.tolist().count("😇 No tóxico")

            pd.set_option("display.max_rows", None)
            print(dataset)
            print("\n")
            print("*" * 80)
            print("\n")
            print(f"Numero de comentarios: {len(dataset)}")
            print(f"Numero de comentarios tóxicos: {toxic}")
            print(f"Numero de comentarios no tóxicos: {no_toxic}")
            print("\n")
    else:
        print("Modo no válido. Use 'url' o 'text'.")


if __name__ == "__main__":
    main()
