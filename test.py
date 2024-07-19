# #Test 1
# #Create a Maths Scoresheet App
# A lecturer in the university wants you as programmer to create a software to mark students scores
# Ask the students for their scores in Maths only
# If the total score is above 90, give the student A+
# If the total score is between 80-89, give the student A
# If the total score is between 70-79, give the student B
# If the total score is between 60-69, give the student C
# If the total score is between 50-59, give the student D
# If the total score is below 50, give the student F

import streamlit as st
st.set_page_config(layout ='wide')
st.title ("Maths Scoresheet App")
score = st.number_input ("What was your maths score:")
if st.button ("Check your score"):
    if score >=90:
        st.write (" You got a A+.")
    if score >=80 and score <=89:
        st.write (" You got a A.")
    if score >=70 and score <=79:
        st.write ("You got a B.")
    if score >= 60 and score <=69:
        st.write ("You got a C.")
    if score >=50 and score <=59:
        st.write ("You got a D.")
    if score < 50:
        st.write ("You got a F.")
