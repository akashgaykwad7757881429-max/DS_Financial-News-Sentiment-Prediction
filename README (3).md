Financial News Sentiment Prediction

Project Overview

This project aims to predict the sentiment of financial news headlines and tweets using Deep Learning and Natural Language Processing (NLP). The model classifies financial text into three categories:

- Bullish
- Bearish
- Neutral

A Streamlit web application is developed to allow users to enter financial news headlines and receive sentiment predictions in real time.

---

Objectives

- Analyze financial news sentiment.
- Classify news into Bullish, Bearish, or Neutral categories.
- Build an NLP-based Deep Learning model.
- Deploy predictions through a Streamlit web application.

---

Dataset Information

The dataset contains financial news headlines and corresponding sentiment labels.

Dataset Features

- Text: Financial news headline or tweet.
- Label:
  - 0 = Bearish
  - 1 = Bullish
  - 2 = Neutral

Dataset Size

- Training Records: 9543
- Validation Records: 2388

---

Exploratory Data Analysis (EDA)

The following analysis was performed:

- Dataset shape analysis
- Missing value check
- Label distribution analysis
- Sentiment distribution visualization

Findings

- No missing values found.
- Neutral sentiment had the highest frequency.
- Dataset contains three sentiment classes.

---

Data Preprocessing

The following preprocessing steps were applied:

- Text cleaning
- Lowercase conversion
- Tokenization
- Sequence generation
- Padding sequences
- Label preparation

---

Model Development

A Deep Learning model was built using TensorFlow and Keras.

Model Architecture

- Embedding Layer
- LSTM Layer
- Dropout Layer
- Dense Layer
- Output Layer (Softmax)

Model Parameters

- Vocabulary Size: 10,000
- Maximum Sequence Length: 100
- Batch Size: 32
- Epochs: 5
- Optimizer: Adam
- Loss Function: Sparse Categorical Crossentropy

---

Model Training

The model was trained using the training dataset and validated using the validation dataset.

Performance

- Training Accuracy: ~97%
- Validation Accuracy: ~80%

---

Streamlit Application

The Streamlit application provides:

- User-friendly interface
- Financial news input box
- Real-time sentiment prediction
- Sentiment probability visualization

Input

Financial news headline or tweet.

Output

- Bullish
- Bearish
- Neutral

---

Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- TensorFlow
- Keras
- Streamlit
- NLP Techniques

---

Project Structure

├── app.py
├── financial_news_sentiment_model.h5
├── DS_Financial_News_Sentiment_Prediction.ipynb
├── README.md
├── sent_train.csv
└── sent_valid.csv

---

Conclusion

This project successfully predicts financial market sentiment from news headlines and tweets using Deep Learning. The Streamlit application enables real-time sentiment analysis and provides an interactive user experience for financial news classification.

---

Author

Akash D. Gaikwad