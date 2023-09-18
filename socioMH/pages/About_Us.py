import streamlit as st
from streamlit_extras.switch_page_button import switch_page

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


st.info("### About Us")
intro_text = """
This project is the culmination of rigorous academic research and dedication, spearheaded       by     Jennifer Nneoma Shedrack, a Master's student specializing in Big Data Analytics at the Faculty of         Engineering and Computing, Birmingham City University.
Our project focuses on the intersection of social media and mental health, a rapidly evolving field of study with profound implications for our understanding of human behavior and well-being. We leverage the power of Big Data to analyze Twitter-generated content, aiming to assess mental health outcomes based on social media engagement and activity.
The inspiration for this project stems from the recognition of social media's pervasive influence on our daily lives and its potential as a rich source of data for understanding mental health. By analyzing patterns, sentiments, and trends in Twitter data, we aim to uncover insights that can contribute to mental health research and potentially inform interventions and support.
As we navigate the complexities of Big Data and mental health, we remain committed to ethical data practices, respecting user privacy, and contributing valuable insights to the field of mental health research.
Looking ahead, we envision this project as a stepping stone towards more comprehensive and nuanced understanding of mental health in the digital age. We believe in the potential of Big Data to transform mental health research and are excited about the possibilities this project might unlock."""
st.markdown('<div style="text-align: justify;">{}</div>'.format(intro_text), unsafe_allow_html=True)