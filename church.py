#create a simple church age range database

#This will get the name, age, gender of the church member

#create a submit button
#Make sure you group members in different category based on their age 
# (Kids(3- 12), Teens(13-19), Youth(20-35), Adult(36-64), Elders(65+) )

import streamlit as st
name = st.text_input ("What's your name?")
age = st.number_input("How old are you?",3)
gender = st.radio ("Gender",['male','female'])
if st.button ("Submit"):
 if (age>2 and age <13):
  st.success("Submitted! You are sorted into the Kids Group")
 elif (age>12 and age <20):
  st.success("Submitted! You are sorted into the Teens Group")
 elif (age > 19 and age < 36):
  st.success("Submitted! You are sorters into the Youth Group!")
 elif (age>35 and age <65):
  st.success("Submitted! You are sorted into the Adults Group")
 elif (age>65):
  st.success("Submitted! You are sorted into the Elders Group")
  
 