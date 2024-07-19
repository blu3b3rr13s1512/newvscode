#create a project to ask for the name and age. 
# then put the response/input in a dictionary 
# and then show it as a table
import streamlit as st
import pandas as pd
name = st.text_input("What is your name?")
age = st.number_input("How old are you?",0)

info = {'Name':[name],'Age':[age]}

st.write(info)

table = pd.DataFrame(info)
st.table(table)

