import streamlit as st
import pandas as pd
import numpy as np
import re

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model
model = load_model("financial_news_sentiment_model.h5")

st.title("Financial News Sentiment Prediction")

st.write("Enter a financial tweet/news headline and predict sentiment.")

# Text cleaning function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Load dataset for tokenizer
train_df = pd.read_csv("sent_train.csv")

train_df["clean_text"] = train_df["text"].apply(clean_text)

tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(train_df["clean_text"])

user_text = st.text_area("Enter Financial News / Tweet")

if st.button("Predict"):

    cleaned = clean_text(user_text)

    seq = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(seq, maxlen=100)

    prediction = model.predict(padded)

    sentiment_map = {
        0: "Bearish 📉",
        1: "Bullish 📈",
        2: "Neutral ➖"
    }

    pred_class = np.argmax(prediction)

    st.success(
        f"Predicted Sentiment: {sentiment_map[pred_class]}"
    )

    probs = prediction[0]

    chart_df = pd.DataFrame({
        "Sentiment": ["Bearish", "Bullish", "Neutral"],
        "Probability": probs
    })

    st.bar_chart(
        chart_df.set_index("Sentiment")
    )