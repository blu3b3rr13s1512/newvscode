import streamlit as st

name = st.text_input("What is your name?")
age = st.text_input("How old are you?")

st.write(name,age)
