import streamlit as st
from datetime import date

st.markdown(""" <h1 style='text-align: center;'>CODING SURVEY</h1> """, unsafe_allow_html=True)
language = st.selectbox("Choose your Programming Language: ", ["Python", "Java", "Scala", "Ruby"])
dob = st.date_input("Enter Your Date of Birth:", min_value= date(2000,1,1), max_value= date.today())

gender = st.radio("Choose your Gender: ", ["Male", "Female", "Other"], horizontal=True)

current_year = date.today()
age = current_year.year - dob.year
st.write(F"Your age is {age} years")
 
 
col01 , col02 = st.columns(2)
with col01:
     st.image("python.png")

with col02:
     st.image("python.png")
     
st.sidebar.text_input("Enter your name: ")

with st.expander("Expand me"):
     st.write(F"your choosen language is {language} is impressive.")
     st.write(F"master the fundamentals of {language} is neccessary.")
     st.write(F"build real world project using {language}. ")


st.markdown(
     """
     <style>
     .block-container{
          padding-top: 2rem;
     }
     </style>      
     """, 
     unsafe_allow_html=True
)









