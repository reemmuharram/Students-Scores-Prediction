import pandas as pd
import numpy as np
import streamlit as st
import joblib


model = joblib.load("model.pkl")

st.title("Student Score Prediction 📚")
st.write("Please fill the following for Score prediction")

col1, col2, col3, col4 = st.columns(4)


with col1:
    Gender = st.radio("Please select your gender:", ["Male", "Female"])
    Gender = 0 if Gender == "Male" else 1

    Learning_Disabilities = st.radio("Do you have any learning disabilities?", ["Yes", "No"])
    Learning_Disabilities = 0 if Learning_Disabilities == "Yes" else 1

    Extracurricular_Activities = st.radio("Have you participated in any Extracurricular Activities?", ["Yes", "No"])
    Extracurricular_Activities = 0 if Extracurricular_Activities == "Yes" else 1

    Internet_Access = st.radio("Is internet accessable for you?", ["Yes", "No"])
    Internet_Access = 0 if Internet_Access == "Yes" else 1

    School_Type = st.radio("What type of schools do you attend?", ["Public", "Private"])
    School_Type = 0 if School_Type == "Public" else 1




with col2:
    Hours_Studied = st.number_input("How many hours have you studied?", 
                                    min_value=1, 
                                    max_value=45, 
                                    step=4,
                                    value=23 )

    Attendance = st.number_input("What is your attendance percentage?", 
                                 min_value=60,
                                 max_value=100,
                                 step=5,
                                 value=100)
    
    Previous_Scores = st.number_input("What is your previous score?", 
                                      min_value=50,
                                      max_value=100,
                                      step=1,
                                      value=75)
    
with col3:
    Parental_Involvement = st.selectbox("Level of Parental Involvement:", ["Low", "Medium", "High"])
    if Parental_Involvement == "Low":
        Parental_Involvement = 0
    elif Parental_Involvement == "Medium":
        Parental_Involvement = 1
    else:
        Parental_Involvement = 2

    Access_to_Resources = st.selectbox("Availability of Educational Resources:", ["Low", "Medium", "High"])
    if Access_to_Resources == "Low":
        Access_to_Resources = 0
    elif Access_to_Resources == "Medium":
        Access_to_Resources = 1
    else:
        Access_to_Resources = 2

    Motivation_Level = st.selectbox("Level of Motivatoin:", ["Low", "Medium", "High"])
    if Motivation_Level == "Low":
        Motivation_Level = 0
    elif Motivation_Level == "Medium":
        Motivation_Level = 1
    else:
        Motivation_Level = 2 

    Family_Income = st.selectbox("Family Income:", ["Low", "Medium", "High"])
    if Family_Income == "Low":
        Family_Income = 0
    elif Family_Income == "Medium":
        Family_Income = 1
    else:
        Family_Income = 2 

    Teacher_Quality = st.selectbox("Quality of the teachers:", ["Low", "Medium", "High"])
    if Teacher_Quality == "Low":
        Teacher_Quality = 0
    elif Teacher_Quality == "Medium":
        Teacher_Quality = 1
    else:
        Teacher_Quality = 2 
    
    Parental_Education_Level = st.selectbox("What's your parents' highest education level?", ["High School", "College", "Postgraduate"])
    if Parental_Education_Level == "High School":
        Parental_Education_Level = 0
    elif Parental_Education_Level == "College":
        Parental_Education_Level = 1
    else:
        Parental_Education_Level = 2 

    Distance_from_Home = st.selectbox("How far is your school from home?", ["Near", "Moderate", "Far"])
    if Distance_from_Home == "Near":
        Distance_from_Home = 0
    elif Distance_from_Home == "Moderate":
        Distance_from_Home = 1
    else:
        Distance_from_Home = 2


    Peer_Influence = st.selectbox("What is the influence of your peers on your academic performance?:", ["Negative", "Neutral", "Positive"])
    if Peer_Influence == "Negative":
        Peer_Influence = 0
    elif Peer_Influence == "Neutral":
        Peer_Influence = 1
    else:
        Peer_Influence = 2 


Sleep_Hours = st.slider("How many hours of sleep have you been getting?", 
                        max_value = 10,
                        min_value=4, 
                        value=8,
                        step=1)

with col4:
    Tutoring_Sessions = st.slider("How many tutoring sessions have you attended?", 
                            max_value = 8,
                            min_value=0, 
                            value=4,
                            step=1)
    
    Physical_Activity = st.slider("Please enter the Average number of hours of physical per week", 
                                max_value = 6,
                                min_value = 0,
                                value = 3,
                                step = 1)

if st.button("Predict 🚀"):
    data = {
        "Hours_Studied":Hours_Studied,
        "Attendance":Attendance,
        "Parental_Involvement" : Parental_Involvement,
        "Access_to_Resources" : Access_to_Resources,
        "Extracurricular_Activities" : Extracurricular_Activities,
        "Sleep_Hours" : Sleep_Hours,
        "Previous_Scores" : Previous_Scores,
        "Motivation_Level" : Motivation_Level,
        "Internet_Access": Internet_Access,
        "Tutoring_Sessions" : Tutoring_Sessions,
        "Family_Income" : Family_Income,
        "Teacher_Quality" : Teacher_Quality,
        "School_Type" : School_Type,
        "Peer_Influence" : Peer_Influence,
        "Physical_Activity" : Physical_Activity,
        "Learning_Disabilities" : Learning_Disabilities,
        "Parental_Education_Level" : Parental_Education_Level,
        "Distance_from_Home" : Distance_from_Home,
        "Gender" : Gender
    }
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    st.success(f"Predicted Score: {prediction:.2f}")
