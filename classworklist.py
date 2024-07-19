import streamlit as st
name,age,gender = st.columns(3)
with name:
    name = st.text_input("What is your name?")
with age:
    age = st.number_input("How old are you?")
with gender:
    gender = st.radio ("What gender are you:",["Female","Male"])
favgame = st.selectbox ("What's your favorite game?",["Roblox","Minecraft","BOTW","Valorant"])
bestmovie = st.selectbox ("Whats your favorite movie?",["Spiderverse","Endgame","Eras Tour"])
favcolor = st.selectbox ("What's your favorite color?",["Green","Blue","Pink","Purple"])
bestie = st.text_input("Who's your best friend?")

if st.button("SUBMIT"):
    st.success (f"{name} ({gender}) your favorite game is {favgame} and your favorite color is {favcolor} and your favorite movie is {bestmovie} and your best friend is {bestie}")
