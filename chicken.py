#A poultry farm sells a chicken for 10$. Create a program in Python to ask how many chickens people want to get and then tell them the total price.
import streamlit as st
st.title ("Chicken Shop")
st.write ("One chicken for 10 dollars.")
noofchickens =st.number_input (" Enter the amount of chickens you want",0, value = 0)
totalprice = noofchickens*10
if st.button ("Check the price"):
    st.write ("Your total is",totalprice, "dollars.")