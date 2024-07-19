#CLASSWORK WITH MENU
# A fashion app 
# -title
# -image
# -categories
# Men's Fashion

# Women's Fashion

# Children's Fashion

# (each category must havedifferent types of unique items and the prices like shirts(long sleeves,short, round neck, polo etc), boxers, trousers, shoes, bags etc)


#A menu is way to create separate pages and functionality for the the same data app
#colors: blue, green, orange, red, violet.

import streamlit as st
st.set_page_config(layout = 'wide')
bill = 0

menu = st.sidebar.selectbox('Menu',['Fashion Store','About Me'])
if menu == 'Fashion Store':
    st.title ("Welcome to Kyra's Fashionista Store")

    st.header ("Women's Fashion")
    wf1,wf2,wf3,wf4 = st.columns(4)
    with wf1:
        if st.checkbox ("Blue Striped blouse : $125"):
            bill+=25
            st.success ("Added")
    with wf2:
        if st.checkbox ("Pink Mini Tee : $100"):
            bill+=100
            st.success ("Added")
    with wf3:
        if st.checkbox ("Pale Blue Jeans : $130"):
            bill+=130
            st.success ("Added")
    with wf4:
        if st.checkbox ("Brown Checkered Skirt : $110"):
            bill+=110
            st.success ("Added")

    st.header ("Men's Fashion")
    mf1,mf2,mf3,mf4 = st.columns (4)
    with mf1:
        if st.checkbox ("Blue Tie : $50"):
            bill+=50
            st.success ("Added")
    with mf2:
        if st.checkbox ("Grey Button Shirt : $125"):
            bill+=125
            st.success ("Added")
    with mf3: 
        if st.checkbox ("Green Hoodie : $100"):
            bill+=100
            st.success("Added")
    with mf4:
        if st.checkbox ("Navy Jogger Pants : $110"):
            bill+=110
            st.success ("Added")

    st.header ("Children's Fashion")
    cf1,cf2,cf3,cf4 = st.columns(4)
    with cf1:
        if st.checkbox ("Unicorn T shirt : $98"):
            bill+=98
            st.success ("Added")
    with cf2: 
        if st.checkbox ("Dinosaur Hat : $ 87"):
            bill+=87
            st.success ("Added")
    # with cf3:
    #     if st.chec

if menu == 'About Me':
    st.title  ("This is about My Fashionista Store")

