import streamlit as st # Import the Streamlit library for building web applications
import joblib  # Import joblib for loading the trained model

# Load the trained model from the "sentiment-model.pkl" file

model = joblib.load("sentiment-model.pkl")

# dictionary defined to map the numerical sentiment labels predicted by the model to text 

sentiment_labels = {'1': 'Positive', '0': 'Negative'}


#creating streamlit application

st.title("Sentiment Analysis Tool")
st.markdown("""
This tool predicts the sentiment of your text as either positive or negative. Enter your text below to get started!
""")

input = st.text_area("Enter your text here")

if st.button("Analyze Sentiment"):
    print(input)
    predicted_sentiment = model.predict([input])[0] # Use the model to predict the sentiment of the input text
    predicted_sentiment_label = sentiment_labels[str(predicted_sentiment)]  # Map the predicted sentiment label to its corresponding sentiment

    st.info(f"predicted sentiment: {predicted_sentiment_label}")




