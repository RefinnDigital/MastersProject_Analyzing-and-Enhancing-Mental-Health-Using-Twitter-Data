
import streamlit as st

import pandas as pd
import numpy as np
import plotly.express as px
import pickle
import base64
import json
import googlemaps
import pydeck as pdk
from datetime import datetime, timedelta, date
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from streamlit_extras.switch_page_button import switch_page
from keras.preprocessing.text import Tokenizer
import altair as alt
import psycopg2
import re
from track_utils import add_prediction_details
import nltk
import pytz
nltk.download('stopwords')
from datetime import datetime
import requests
import json


from nltk.corpus import stopwords

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You need to log in to access this page!")
    st.stop()

st.set_page_config(
    page_title="Social Medial Mental Health Assessment(M-Check)",
    page_icon="..\MentalAss\mylogo.png",
    initial_sidebar_state="collapsed",
    layout="wide"
    # Using st.markdown to add custom CSS to your Streamlit app
)




DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = " " #add your DB password
DB_HOST = "localhost"
DB_PORT = "5432"





st.markdown("""
    <style>
        .main {
           background: #000000;
           background: radial-gradient(at left top, #000000, #000000);

           opacity: 0.8;  
        }
        
         /* Change the sidebar color */
        .sidebar .sidebar-content {
            background-color: green;
        }
        .reportview-container .main .block-container {
            background-color: black;
        }
            
        /* Change the placeholder color */
        .stTextInput input {
            background-color: dark-grey;
        }
    </style>
    """, unsafe_allow_html=True)

# Loading the saved model and tokenizer
model_path = 'pages\model\lstm_model.h5'  
model = load_model(model_path)


with open('pages\model\lstm_tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


# model = load_model('.\pages\model\keras.h5')
MAXLEN = 280

def preprocess_text(text):
    sequences = tokenizer.texts_to_sequences([text])
    padded_sequences = pad_sequences(sequences, maxlen=MAXLEN)
    return padded_sequences

def predict_emotions(docx):
    preprocessed_text = preprocess_text(docx)
    results = model.predict(preprocessed_text)
    emotion = np.argmax(results)  
    return model.classes_[emotion]  

def get_prediction_proba(text):
    preprocessed_text = preprocess_text(text)
   
    prediction = model.predict(preprocessed_text)[0]
    return prediction

 
def get_prediction_proba(docx):
     preprocessed_text = preprocess_text(docx)
     return model.predict(preprocessed_text)[0]
# Track Utils
from track_utils import create_page_visited_table,add_page_visited_details,view_all_page_visited_details,add_prediction_details,view_all_prediction_details,create_emotionclf_table

# Fxn
def predict_emotions(docx):
    preprocessed_text = preprocess_text(docx)
    results = model.predict(preprocessed_text)
    return results[0]



MODEL_CLASSES = ["anger", "disgust", "fear", "negative", "joy", "anticipation", "positive", "sadness", "surprise", "surprise"]
EMOTIONS_EMOJI_DICT = {
    "anger": "😠",
    "disgust": "🤮",
    "fear": "😨",
    "negative": "😔",
    "joy": "😂",
    "anticipation": "😐",
    "positive": "🤗",
    "sadness": "😔",
    "trust": "😳",
    "surprise": "😮"
}




# Initialize stopwords
stop_words = set(stopwords.words('english'))

def clean_tweet(tweet):
    # Convert the tweet to lowercase
    tweet = tweet.lower()
    
    # Remove URLs
    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
    
    # Remove user mentions
    tweet = re.sub(r'@\w+', '', tweet)
    
    # Remove punctuations and special characters except for '?' and '!'
    tweet = re.sub(r'[^a-zA-Z\s!?]', '', tweet)
    
    # Remove extra whitespace
    tweet = re.sub(r'\s+', ' ', tweet).strip()
    
    return tweet






def get_tweets_v2(handle, start_date, end_date, bearer_token):
    """Fetch tweets using Twitter API v2 for a given handle within the specified date range."""
    tweets = []
    headers = {
        "Authorization": f"Bearer {bearer_token}",
    }
    # URL for the Twitter API v2 endpoint for user tweet timeline.
    user_url = f"https://api.twitter.com/2/users/by/username/{handle}"
    user_response = requests.get(user_url, headers=headers)
    if user_response.status_code != 200:
        st.error(f"An error occurred while fetching user details: {user_response.json().get('message', 'Unknown error')}")
        return []

    user_id = user_response.json()["data"]["id"]
    
    # Fetch the current UTC time
    current_utc_time = datetime.utcnow()
    # Set the start_time to be 10 minutes before the current UTC time
    start_date_str = (current_utc_time - timedelta(minutes=10)).strftime('%Y-%m-%dT%H:%M:%SZ')
    
    # Subtracting 15 seconds from the current time for the end_date (to give some leeway)
    end_date_str = (current_utc_time - timedelta(seconds=15)).strftime('%Y-%m-%dT%H:%M:%SZ')
    
    url = f"https://api.twitter.com/2/tweets/search/recent?query=from:{handle}&start_time={start_date_str}&end_time={end_date_str}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        for tweet_data in response.json().get("data", []):
            tweets.append(clean_tweet(tweet_data["text"]))
    else:
        st.error(f"An error occurred while fetching tweets: {response.json()}")
    return tweets




# Use this function in your Streamlit app:

# Provide your Bearer Token from the Twitter Developer Dashboard.
bearer_token = " " # We removed to adhere strictly to privacy and confidentiality standards
if 'start_date' in locals() and 'end_date' in locals() and handle:
    tweets = get_tweets_v2(handle, start_date, end_date, bearer_token)






# Streamlit UI
col1, col2 = st.columns([1, 9])
with col1:
    st.image("pages\img\Logo.png", width=100)
with col2:
    st.title("Social Medial Mental Health Assessment(M-Check)")
st.write("---")

st.info("### Analyze your Mental Status")
st.write("#")
# Taking input from the user
handle = st.text_input("Enter Twitter Handle")


years_options = [2023]
end_years_options = [2023]

col1, col2 = st.columns(2)

# Select start dates within the first column
with col1:
    st.write("Start Date")
    start_year = 2023
    start_month = st.selectbox('Select start month', [9], key="start_month")

# Select end dates within the second column
with col2:
    st.write("End Date")
    end_year = 2023
    end_month = st.selectbox('Select end month', [9], key="end_month")



start_date = date(start_year, start_month, 1)
if end_month == 12:
    end_date = date(end_year + 1, 1, 1) - timedelta(days=1)
else:
    end_date = datetime(end_year, end_month, 17, 17, 20, 51)



if st.button("Fetch tweets"):
    if handle:
        tweets = get_tweets_v2(handle, start_date, end_date, bearer_token)
        if not tweets:
            st.write("No tweets found in the given timeframe or the user doesn't exist.")
        else:
            raw_text = ' '.join(tweets)

            col1, col2 = st.columns(2)

            # Appling our Function Here
            prediction = predict_emotions(raw_text)
            probability = get_prediction_proba(raw_text )
            predicted_class_index = np.argmax(prediction)
            predicted_class = MODEL_CLASSES[predicted_class_index]
            emoji_icon = EMOTIONS_EMOJI_DICT[predicted_class]

            add_prediction_details(raw_text, str(prediction.tolist()), float(np.max(probability)), datetime.now())

            with col1:
                with st.container():
                    st.success("Original Text")
                    with st.expander("click to view Tweets"):
                         st.write(raw_text)
                st.success("Prediction")
                st.write("{}: {}".format(predicted_class, emoji_icon))
                st.write("Frequency: {}".format(np.max(probability)))
                prediction_label = predicted_class
                prediction_probability = np.max(probability)
                add_prediction_details(raw_text, str(prediction_label), float(prediction_probability), datetime.now(pytz.utc))
                

            with col2:
                st.success("Prediction Probability")
                probability = probability.reshape(1, -1)
                proba_df = pd.DataFrame(probability, columns=MODEL_CLASSES)
                proba_df_clean = proba_df.T.reset_index()
                proba_df_clean.columns = ["emotions", "probability"]
                fig = alt.Chart(proba_df_clean).mark_bar().encode(x='emotions', y='probability', color='emotions')
                st.altair_chart(fig, use_container_width=True)


            col4, col5 = st.columns(2)
            with col4:             
                
                concerning_emotions = ['sadness', 'anger', 'fear', 'disgust', 'negative']
                if predicted_class in concerning_emotions:
                    st.warning("Based on the tweets, it might be helpful to speak with a mental health professional.")                 
                    st.info("In case of an emergency:")
                    st.write("[NHS Mental Health Emergency Helpline](https://www.nhs.uk/service-search/mental-health/find-an-urgent-mental-health-helpline)")
                    
                else:
                    st.info("This Twitter user does not exhibit signs of a mental health concern in their tweets 🤗")
                    st.subheader("Resources to maintain mental well-being:")
                    st.write("[Mental Health Books](https://positivepsychology.com/mental-health-books/#google_vignette)")
                    st.write("[Mind - Food and Mental Health](https://www.mind.org.uk/information-support/tips-for-everyday-living/food-and-mental-health/?gclid=CjwKCAjw_aemBhBLEiwAT98FMlY878YyypxUVNdBF3XYC07H_1ps7MNA6PcNdfQ0tOIHxAL6KonfYRoCrYkQAvD_BwE)")

                    st.info("Remember to monitor your mental health regularly and seek help if needed!")
st.write("#")

st.info("### Mental Health professionals Near Me")
st.write("#")
special_button = st.button('Specialists Near Me')
if special_button:
    switch_page("Specialist")
                    
          
col1, col2, col3 = st.columns(3)

# Custom styling for the button
button_style = """
    <style>
        .center_button {
            background-color: #007241;
            color: white;
            font-size: 20px;
            height: 50px;
            width: 120px;
            border-radius: 10px;
            cursor: pointer;
        }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

with col2:
    center_button = st.button('Back')
    if center_button:
        switch_page("Resources")

