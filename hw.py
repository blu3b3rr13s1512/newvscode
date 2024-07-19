import streamlit as st
number1 = st.number_input("Put a number:")
number2=st.number_input("Choose another number:")
multiply = (number1*number2)
added = (number1+number2)
numberdict = {'number 1':[number1],'number 2':[number2],'multiply':[multiply],'added':[added]}
if st.button("Submit"):
    st.write(numberdict)
