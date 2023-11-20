import pandas as pd
import tensorflow as tf
from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np
import re
import random

# Set seeds for reproducibility
np.random.seed(1)
tf.random.set_seed(1)
random.seed(1)

# Function to clean the text
def clean_text(text):
    text = " ".join(text.split())  # Remove extra whitespaces
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r'\S*@\S*\s?', '', text)  # Remove email addresses
    return text

# Load the dataset
data = pd.read_csv('youtoxic_english_1000.csv')
data['CleanedText'] = data['Text'].apply(clean_text)
data_cleaned = data.drop_duplicates(subset=['Text'], keep='first').reset_index(drop=True)

# Split the dataset
train_data, val_data = train_test_split(data, test_size=0.1, random_state=1)

# Initialize the tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

# Tokenize the text
train_encodings = tokenizer(list(train_data['CleanedText']), truncation=True, padding=True)
val_encodings = tokenizer(list(val_data['CleanedText']), truncation=True, padding=True)

# Convert the 'IsToxic' column to integers
train_labels = train_data['IsToxic'].astype(int).values
val_labels = val_data['IsToxic'].astype(int).values

# Convert encodings and labels to TensorFlow datasets
train_dataset = tf.data.Dataset.from_tensor_slices((dict(train_encodings), train_labels))
val_dataset = tf.data.Dataset.from_tensor_slices((dict(val_encodings), val_labels))

# Load the pre-trained DistilBERT model
model = TFDistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)

# Compile the model
optimizer = tf.keras.optimizers.Adam(learning_rate=0.00005)
loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])

# Train the model
batch_size = 8
epochs = 1
history = model.fit(
    train_dataset.shuffle(10000, seed=1).batch(batch_size),
    epochs=epochs,
    batch_size=batch_size,
    validation_data=val_dataset.batch(batch_size)
)

# Evaluate the model on the training and validation sets
train_results = model.evaluate(train_dataset.batch(batch_size), return_dict=True)
val_results = model.evaluate(val_dataset.batch(batch_size), return_dict=True)

# Display training and validation results
print(f"Training Loss: {train_results['loss']}, Training Accuracy: {train_results['accuracy']}")
print(f"Validation Loss: {val_results['loss']}, Validation Accuracy: {val_results['accuracy']}")

# Predicting on the validation set
val_preds = model.predict(val_dataset.batch(batch_size))
val_preds_labels = np.argmax(val_preds.logits, axis=1)

# Confusion Matrix and Classification Report
cm = confusion_matrix(val_labels, val_preds_labels)
report = classification_report(val_labels, val_preds_labels, target_names=['Not Toxic', 'Toxic'])

print("Confusion Matrix:\n", cm)
print("Classification Report:\n", report)

# Overfitting calculation
overfitting_level = (train_results['accuracy'] - val_results['accuracy']) * 100
print(f"This model has an overfitting of {overfitting_level:.2f}%")

# Save the model
model.save("model")
