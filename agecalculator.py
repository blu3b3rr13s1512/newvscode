import streamlit as st # this is the framework to develop your software
st.title("My age Calculator") # big name on the screen
name = st.text_input('ENter your name') # This input for text
yob = st.number_input('Enter your year of birth',1900,2023,value=1950) # input for number
curr = st.number_input("Enter the current year",2023,2025,value = 2023) # input for number
if st.checkbox("Are you allowed to use the internet"):
    st.write("That's so cool")
age = curr-yob
if st.button("CHeck Your Age"): # create a button, also check if clicked
    st.write(name,"you are", age,"in year", curr)
    #executes/run if True

