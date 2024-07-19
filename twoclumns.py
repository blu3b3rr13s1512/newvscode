import streamlit as st
col1,col2 = st.columns(2)
with col1:
    if st.button("Submit"):
        with col2:
            st.success("Welcome!")