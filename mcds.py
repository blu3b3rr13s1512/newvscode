import streamlit as st
bill = 0
b1,b2,b3,b4 = st.columns(4)

with b1:
    st.checkbox("Cheeseburger: $10")
    bill+=10
    st.success("Added to Cart")
with b2:
    st.checkbox("Beef Burger: $10")
    bill+=10
    st.success("Added to Cart")
with b3:
    st.checkbox("Shrimp BUrger : $10")
    bill+=10
    st.success(" Added to Cart")
with b4:
    st.checkbox("Big Mac : $10")
    bill+=10
    st.success("Added to cart")

d1,d2 = st.columns(2)
with d1:
    st.checkbox("Coke : $5")
    bill+=5
    st.success ("Added to Cart")

with d2 :
    st.checkbox("Sprite: $5")
    bill+=5
    st.success ("Added to Cart")

st.checkbox("Fries : $5")
bill+=5
st.success ("Added to cart")

if st.button("Chech Total"):
    st.header (f"Your Total is {bill}")

