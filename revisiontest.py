import streamlit as st
#1.What is streamlit used for? 
st.write("Streamlit is used to create a python program  to show up on a webpage to collect data, or to show some information and gather.")


#2.show 8 ways to display text on streamlit
st.write("st.write")
st.header('st.header')
st.title("st.title")
st.success("St.success")
st.subheader("St.subheader")
st.error("st.error")
st.info ("st.info")
st.warning("st.warning")


#3.show how to ask for a text on streamlit
name = st.text_input("What is your name?")



#4.show how to ask for a number on streamlit
age = st.number_input("How old are you?")
#5.create a button on the left column but show the output on the right column
button = st.columns(2)
button = st.button("Submit")
output = ("output")
#6.create a radio button with a horizontal orientation
st.radio("Whats your favorite color",["red","pink","purple"])
# 7.import an image with a 150*150 size
st.image('https://cdn.pixabay.com/photo/2017/08/08/18/09/burger-2612137_1280.jpg')
# 8. read and dispay a CSV file in python

# 9.create a toggle option to display any database/dataframe

# 10.create a dictionary of 5 different cars with 5 attributes (without using a CSV file)
# and convert it to a dataframe/table
cardict = {'model':'tesla','color':'pink','wheel':'big','year':1989,'place':'US',}
st.write(cardict)
