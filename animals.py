# #classwork:
# open a new file and name it animals.py
# ask for an example of a bird, cat, dog, fish, snake, shark
#     then create a dictionary for the response and also a table too. display both respectively

import streamlit as st
import pandas as pd

bird = st.text_input("Give an example of a bird:")
cat = st.text_input("Give an example of a cat:")
dog = st.text_input("Give an example of a dog:")
fish = st.text_input("Give an example of a fish:")
snake = st.text_input("Give an example of a snake:")
shark = st.text_input("Give an example of a shark.")

readcsv = pd.read_csv('animals.csv')
animaldict = {'Bird':[bird],'Cat':[cat],'Dog':[dog],'Fish':[fish],'Snake':[snake],'Shark':[shark]}
animaltable = pd.DataFrame(animaldict)

if st.button("Submit and see your answers!"):
    st.write(animaldict)
    st.table(animaltable)