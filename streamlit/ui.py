
import streamlit as st
import requests

st.title("📑Score Prediction")

study=st.sidebar.slider("Study Time",0,10)
atd=st.sidebar.slider("Attended Days",0,100)
gen=st.sidebar.selectbox("Gender",["Male","Female"])

gender=1 if(gen=="Male") else 0
sub = st.sidebar.button("Predict the score")
if sub:
    st.write("Study_time :",study)
    st.write("Attendance :",atd)
    st.write("Gender :",gen)
    data={
        "study_time":study,
        "attendance": atd,
        "gender_Male":gender

    }
    res=requests.post("http://127.0.0.1:8000/predict",json=data)
    result=res.json()
    st.write("The Predicted Score is ", result["Predicted_score"])
