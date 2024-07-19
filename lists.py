# classwork:
# create a list.py file
# -tell us what a list is in python
# -create an example of a list and display it in python
# -give 3 examples of how to use a list in streamlit




import streamlit as st
st.write("A list is when you store multiple pieces of data into a single variable file, and you can also choose which data/ information you want to show on the screen.")
colors = ['red','pink','blue','purple']
st.write(colors)

food = ['cookie','ice cream','seaweed','takis']
st.write(food)

gender = st.radio("Gender",['male','female'])

favcolor = st.selectbox("Favorite Color",['pink','purple','green','blue','red'])
