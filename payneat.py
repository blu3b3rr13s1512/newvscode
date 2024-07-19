import streamlit as st
st.set_page_config(layout='wide')
bill = 0
st.title ("Pay N Eat Restaurant")
st.image('https://cdn.pixabay.com/photo/2017/09/28/18/13/bread-2796393_1280.jpg')

st.header('Meals')
meal1,meal2,meal3,meal4 = st.columns(4)

with meal1:
    if st.checkbox ('Grilled Cheese Sandwich with Chicken : $46'):
        bill+=46
        st.success('Added to Cart')

with meal2:
    if st.checkbox ("Caesar Salad with Hummus Wrap : $45"):
        bill+=45
        st.success ("Added to Cart")

with meal3:
    if st.checkbox ("Curry with Pork Cutlet:$37"):
        bill+=37
        st.success("Added to cart")

with meal4:
    if st.checkbox ("Burger and Fries : $ 50"):
        bill+=50
        st.success("Added to cart")


st.header('Side Meals')
side1,side2,side3,side4 = st.columns(4)
with side1:
    if st.checkbox("Mozzarella Sticks : $25"):
        bill+=25
        st.success("Added to cart")

with side2:
    if st.checkbox("Meatballs: $24"):
        bill+=24
        st.success("Added to cart")

with side3:
    if st.checkbox("Garlic Bread : $26"):
        bill+=26
        st.success("Added to Cart")

with side4:
    if st.checkbox ("Chicken Strips: $22"):
        bill+=22
        st.success("Added to Cart")

st.header('Drinks')
drink1,drink2,drink3,drink4 = st.columns(4)
with drink1:
    if st.checkbox("Soft Drink (Coke, Sprite, Fanta): $15"):
        bill+=15
        st.success("Added to Cart")
with drink2:
     if st.checkbox("Milk Tea : $35"):
        bill+=35
        st.success ("Added to Cart")
with drink3:
    if st.checkbox("Apple Juice: $20"):
        bill+=20
        st.success("Added to Cart")
with drink4:
    if st.checkbox("Coffee : $30"):
        bill+=30
        st.success("Added to Cart")

st.header("Dessert")
dessert1,dessert2,dessert3,dessert4, = st.columns(4)
with dessert1:
    if st.checkbox("Brownie with Ice Cream : $36"):
        bill+=36
        st.success("Added to Cart")
with dessert2: 
    if st.checkbox("Banana Split : $40"):
        bill+=40
        st.success("Added to Cart")
with dessert3:   
    if st.checkbox("Lemon Tart : $36"):
        bill+=36
        st.success("added to Cart")
with dessert4:
    if st.checkbox("Rainbow Cupcake : $38"):
        bill+=38
        st.success("Added to Cart")

if st.button ("Check your total"):
    st.header(f'Your total bill is ${bill}')
    