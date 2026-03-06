Sentiment Analysis Web App

A simple Sentiment Analysis Web Application built using Python and Streamlit.
This application analyzes the sentiment of a given sentence and predicts whether it is Positive 😊 or Negative 😡.

Project Overview

This project uses a Machine Learning model trained on a dataset of text reviews to determine the sentiment of user input.

The application allows users to:

Enter any sentence or review

Analyze the sentiment

View the result instantly on the web interface

Technologies Used

Python

Streamlit

Scikit-learn

Pandas

Pickle

Project Structure
sentiment_analysis_project
│
├── app.py
├── train_model.py
├── sentiment_dataset.csv
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
How the Project Works

The dataset contains text reviews labeled as positive or negative.

A CountVectorizer converts the text into numerical features.

A Naive Bayes Machine Learning model is trained on this data.

The trained model is saved using pickle.

The Streamlit app loads the model and predicts the sentiment of user input.

Installation
Step 1: Clone the repository
git clone https://github.com/your-username/sentiment-analysis-app.git
Step 2: Navigate to the project folder
cd sentiment-analysis-app
Step 3: Install dependencies
pip install -r requirements.txt
Run the Application

Run the following command:

streamlit run app.py

The application will open in your browser at:

http://localhost:8501
Example

Input:

I really love this product

Output:

Positive Sentiment 😊

Input:

This service is very bad

Output:

Negative Sentiment 😡
Future Improvements

Add neutral sentiment detection

Add sentiment confidence score

Add data visualization charts

Improve the dataset for better accuracy

Deploy the application online

Author

Created as a Machine Learning project using Python and Streamlit.
