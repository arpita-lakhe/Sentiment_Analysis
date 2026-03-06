import streamlit as st
import pickle

# Load trained model and vectorizer
model = pickle.load(open("model(3).pkl", "rb"))
vectorizer = pickle.load(open("vectorizer(1).pkl", "rb"))

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="😊",
    layout="centered"
)

# Title
st.title("😊 Sentiment Analysis App")
st.write("Enter a sentence to analyze whether the sentiment is Positive or Negative.")

# User input
user_input = st.text_area("Enter your text here")

# Analyze button
if st.button("Analyze Sentiment"):

    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    
    else:
        # Convert text into vector
        text_vector = vectorizer.transform([user_input])

        # Predict sentiment
        prediction = model.predict(text_vector)

        # Display result
        if prediction[0] == "positive":
            st.success("Positive Sentiment 😊")
        else:
            st.error("Negative Sentiment 😡")

# Footer
st.write("---")
st.write("Built with Python and Streamlit")
