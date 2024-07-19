import streamlit as st
game = 150
vip = 50
premium = 120
pink = 30
blue = 30
gold = 30
pet = 40
eight = 10
two = 25
four = 50

pay = 0

start = st.selectbox("Do you want to download Roblox?",['Choose','Yes ($150)',"NO"])
if start == "Yes ($150)":
    pay+=150

user = st.text_input("Choose a username:")
password = st.text_input("Enter a safe password:",type = 'password')

allow = st.selectbox("Choose a pass:", ['None','VIP ($50)','Premium ($120)'])
if allow == ():

