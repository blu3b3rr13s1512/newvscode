import streamlit as st
st.set_page_config(layout='wide')
menu = st.sidebar.subheader ("Ordered")
menu1,menu2 = st.sidebar.columns(2)
st.header ("Mains")
main1,main2,main3,main4,main5,main6 = st.columns(6)
bill=0

with main1:
    st.image('https://cdn.pixabay.com/photo/2017/08/08/18/09/burger-2612137_1280.jpg',use_column_width='always')
    if st.checkbox("Cheeseburger : $56"):
        bill+=56
        with menu1:
            st.image('https://cdn.pixabay.com/photo/2017/08/08/18/09/burger-2612137_1280.jpg',use_column_width='always')

        
with main2:
    st.image('https://cdn.pixabay.com/photo/2017/01/11/20/41/tagliatelle-1972845_1280.jpg',use_column_width='always')
    if st.checkbox("Pesto Pasta : $54"):
        bill+=54
        with menu1:
            st.image('https://cdn.pixabay.com/photo/2017/01/11/20/41/tagliatelle-1972845_1280.jpg',use_column_width='always')
            
        
with main3:
    st.image('https://cdn.pixabay.com/photo/2016/08/30/00/02/caesar-salad-1629534_1280.jpg',use_column_width ='always')
    if st.checkbox("Caesar Salad : $49"):
        bill+=49
        with menu1:
            st.image('https://cdn.pixabay.com/photo/2016/08/30/00/02/caesar-salad-1629534_1280.jpg',use_column_width ='always')
            
        
with main4:
    st.image('https://cdn.pixabay.com/photo/2017/06/27/08/41/pizza-2446700_1280.jpg',use_column_width = 'always')
    if st.checkbox("Magherita Pizza: $56"):
        bill+=56
        with menu1:
            st.image('https://cdn.pixabay.com/photo/2017/06/27/08/41/pizza-2446700_1280.jpg',use_column_width = 'always')
        
with main5:
    st.image('https://cdn.pixabay.com/photo/2020/04/04/15/07/sushi-5002639_1280.jpg',use_column_width = 'always')
    if st.checkbox("Sushi: $50"):
        bill+=50
        with menu1:
             st.image('https://cdn.pixabay.com/photo/2020/04/04/15/07/sushi-5002639_1280.jpg',use_column_width = 'always')

       
with main6:
    st.image('https://cdn.pixabay.com/photo/2019/08/15/10/46/mozzarella-sticks-4407742_1280.jpg',use_column_width = 'always')
    if st.checkbox("Mozzarella Sticks : $ 55"):
        bill+=55
        with menu1:
            st.image('https://cdn.pixabay.com/photo/2019/08/15/10/46/mozzarella-sticks-4407742_1280.jpg',use_column_width = 'always')

        
st.header ("Sides")
side1,side2,side3,side4 = st.columns(4)

with side1:
    if st.checkbox("Mini Salad :$20"):
        st.image('https://cdn.pixabay.com/photo/2015/05/31/13/59/salad-791891_1280.jpg')
        bill+=20
    with menu1:
        st.image('https://cdn.pixabay.com/photo/2015/05/31/13/59/salad-791891_1280.jpg')

with side2:
     st.image('https://cdn.pixabay.com/photo/2015/05/31/13/59/salad-791891_1280.jpg')
if st.checkbox("Fries : $20"):
        bill+=20
        with menu1:
            st.image('https://cdn.pixabay.com/photo/2015/05/31/13/59/salad-791891_1280.jpg')

with side3:
    st.image ('https://cdn.pixabay.com/photo/2017/05/11/19/44/fresh-fruits-2305192_1280.jpg')
    if st.checkbox("Fruit Salad : $25"):
        bill+=25
        with menu1:
           st.image ('https://cdn.pixabay.com/photo/2017/05/11/19/44/fresh-fruits-2305192_1280.jpg')

with side4:
    st.image('https://cdn.pixabay.com/photo/2014/01/16/01/48/chicken-nuggets-246180_1280.jpg')
    if st.checkbox ("Chicken Nuggets : $23"):
        bill+=23
    with menu1:
        st.image ('https://cdn.pixabay.com/photo/2014/01/16/01/48/chicken-nuggets-246180_1280.jpg')
       
       
