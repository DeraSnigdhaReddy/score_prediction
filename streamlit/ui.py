import streamlit as st
import requests
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db=client["Demo_practise"]
collection=db["practise"]

st.title("📑Score Prediction")

name=st.sidebar.text_input("Enter the name")
age=st.sidebar.text_input("Enter the age")
roll=st.sidebar.text_input("Enter the Roll")
phn=st.sidebar.text_input("Enter the Phn")
add=st.sidebar.text_input("Enter the add")

study=st.sidebar.slider("Study Time",0,10)
atd=st.sidebar.slider("Attended Days",0,100)
gen=st.sidebar.selectbox("Gender",["Male","Female"])

gender=1 if(gen=="Male") else 0
sub = st.sidebar.button("Predict the score")
if sub:
    st.write("Name:",name)
    st.write("Age:",age)
    st.write("Roll:",roll)
    st.write("phn:",phn)
    st.write("Address:",add)
    st.write("Study_time :",study)
    st.write("Attendance :",atd)
    st.write("Gender :",gen)
   
    data={
        "study_time":study,
        "attendance": atd,
        "gender_Male":gender

    }
    res=requests.post("https://score-predi-1.onrender.com/predict",json=data)
    result=res.json()
    st.write("The Predicted Score is ", result["Predicted_score"])

    collection.insert_one({
        "name":name,
        "age":age,
        "roll":roll,
        "phn":phn,
        "add":add,
        "Study_Time":study,
        "Attended Days":atd,
        "Gender":gender,
        "Predicted_score":result["Predicted_score"]
    })
    out=list(collection.find())
    for i in out:
        st.write(i["name"],i["age"],i["roll"],i["add"],i["phn"],i["Study_Time"],i["Attended Days"])
    
