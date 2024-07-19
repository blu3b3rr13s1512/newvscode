import streamlit as st
import pandas as pd
movies = {'Name':['Spiderman','Barbie','Demon Slayer'] , 'Producer':['Chris Miller','Robbie Brenner','Hikaru Kondo'],'Main Character':['Miles Morales','Barbie','Kamado Tanjiro'],'Rating' : ['4 Star','4 Star','4 Star']}
st.write(movies)
table = pd.DataFrame(movies)
st.table(table)

