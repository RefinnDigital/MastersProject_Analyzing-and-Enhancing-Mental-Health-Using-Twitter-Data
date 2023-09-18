import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from datetime import datetime
from track_utils import add_page_visited_details, view_all_page_visited_details, view_all_prediction_details

from track_utils import create_page_visited_table, create_emotionclf_table

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You need to log in to access this page!")
    st.stop()

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

col1, col2 = st.columns([1, 9])
with col1:
    st.image("pages\img\Logo.png", width=100)
with col2:
    st.title("Social Medial Mental Health Assessment(M-Check)")
st.write("---")
# Create tables if they don't exist
create_page_visited_table()
create_emotionclf_table()


def monitor_page():
    # Log visit to the Monitor page
    add_page_visited_details("Monitor", datetime.now())
    
    # Page Header
    st.info("### Monitor")
    
    
    
    # Emotion Classifier Metrics Expander
    with st.expander('Emotion Classifier Metrics'):
        # Fetch and display emotion classifier details
        df_emotions = pd.DataFrame(view_all_prediction_details(), columns=['Rawtext', 'Prediction', 'Probability', 'Time_of_Visit'])
        st.dataframe(df_emotions)
        
        # Create and display bar chart for emotion predictions
        prediction_count = df_emotions['Prediction'].value_counts().rename_axis('Prediction').reset_index(name='Counts')
        pc = alt.Chart(prediction_count).mark_bar().encode(x='Prediction', y='Counts', color='Prediction')
        st.altair_chart(pc, use_container_width=True)

# Calling the monitor_page function to execute the monitoring page content
monitor_page()
