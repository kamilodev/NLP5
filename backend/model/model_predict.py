import pandas as pd
import tensorflow as tf
from transformers import DistilBertTokenizer
import numpy as np

def load_model():
    return tf.keras.models.load_model("./model/BERT_model")

# Function to predict the toxicity of the input text
def predict_toxicity(model, text):
    tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
    encodings = tokenizer(text, truncation=True, padding=True, return_tensors="tf")
    predictions = model(encodings)
    logits = predictions["logits"]
    probs = tf.nn.softmax(logits, axis=-1)
    predicted_class = np.argmax(probs, axis=1)[0]

    return predicted_class
