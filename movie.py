import streamlit as st
import pandas as pd
#create a new python program
#create a csvfile and display is using streamlit
#Ask user for their best game and best movie using two columns
#create a dictionary from their response and display is as a dataframe

csvfile= pd.read_csv('gamemovie.csv')
st.dataframe(csvfile)

game,movie = st.columns(2)

with game:
    game = st.text_input("What's your favorite game?")

with movie: 
    movie = st.text_input("What's your favorite movie?")

if st.button("submit"):
    st.write("your favorite game is",game,"and your favorite movie is",movie)

dict = {'game':[game],'movie':[movie]}
st.write(dict)