import streamlit as st
st.write("ELementary fee is 50000 dollars, and college fee is 25000 dollars.")
amountofkidselementary = st.number_input("How many kids do you have for the elementary school?",0)
amountofkidscollege = st.number_input("How many kids do you have for college?",0)
elementaryprice = (amountofkidselementary*50000)
collegeprice = (amountofkidscollege*25000)
fullprice = (elementaryprice+collegeprice)
st.write("Your payment is",fullprice)u 