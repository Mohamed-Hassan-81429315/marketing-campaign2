import pickle as p
import joblib as jb
import streamlit as st
import pandas as pd
import datetime as dt

from Used_Methods import Re_arrange_Age, Date_Calculation
# from fastapi import FastAPI 
# from flask import Flask

# ===================== Load Model & Scaler =====================
model = jb.load("Marketing_model.pkl")
scaler = jb.load("Marketing_scaler.pkl")

# ===================== App Title =====================
st.title(
    "Marketing Campaign Project \n"
    "This is a project about market that shows if the client has responded "
    "to the campaign or not. This helps the market improve its strategies "
    "to increase its clients.\n\n"
    "Now you can fill the following form to predict the client response."
)

# ===================== User Inputs =====================
user_name = st.text_input(
    "Client name",
    placeholder="type the user name like 'Mohamed'",
    max_chars=25,
    value="Mohamed"
)

user_age = st.date_input(
    label="The client Birthday (e.g. 2004/12/27)",
    min_value=dt.date(1975, 10, 10),
    max_value=dt.date.today(),
    value=dt.date.today(),
    key="user_age"
)
user_age = Date_Calculation(user_age=user_age)  # (year, month, day)
Age = Re_arrange_Age(user_age[0])  # use years only

Transaction_Start_Time = st.date_input(
    label="The date the client started coming to Market (e.g. 2005/1/1)",
    min_value=dt.date(2005, 1, 1),
    max_value=dt.date.today(),
    value=dt.date.today(),
    key="Transaction_Start_Time"
)
period = Date_Calculation(Transaction_Start_Time)
Transaction_Start_Time = float(period[0] + (period[1] / 12))

Marital_Status = st.selectbox(
    "What is the marital status of the client?",
    options=["Single", "Married", "Divorced", "Widow", "Together"]
)
Marital_Status = (
    0 if Marital_Status == "Single" else
    1 if Marital_Status == "Married" else
    2 if Marital_Status == "Together" else
    3 if Marital_Status == "Divorced" else
    4
)

Income = float(st.number_input("What is the client Income?", min_value=0, step=1))

Education = st.selectbox(
    "What is the degree of your education?",
    options=["Basic", "2n-Cycle", "Graduation", "Master", "PhD"]
)
Education = (
    2.0 if Education == "Graduation" else
    4.0 if Education == "PhD" else
    3.0 if Education == "Master" else
    1.0 if Education == "2n-Cycle" else
    0.0
)

# ===================== Campaigns =====================
if "options" not in st.session_state:
    st.session_state.options = ["None", "Campaign 1", "Campaign 2", "Campaign 3", "Campaign 4", "Campaign 5"]

if "selected_campaigns" not in st.session_state:
    st.session_state.selected_campaigns = ["None"]

Campaigns = st.multiselect(
    "Select the campaigns the client responded to. If none, select 'None'",
    options=st.session_state.options,
    default=st.session_state.selected_campaigns,
    max_selections=5
)

if "None" in Campaigns and len(Campaigns) > 1:
    Campaigns = [option for option in Campaigns if option != "None"]
elif "None" not in Campaigns and len(Campaigns) == 0:
    Campaigns = ["None"]

AcceptedCmps = len([option for option in Campaigns if option != "None"])

# ===================== Other Inputs =====================
amount1 = st.number_input("Amount of meat taken from Market (kg)", min_value=0, step=1)
amount2 = st.number_input("Amount of fish taken from Market (kg)", min_value=0, step=1)
Proten_Products = (amount1 + amount2) // 2

MntFruits = st.number_input("Amount of fruits taken from Market (kg)", min_value=0, step=1)

amount3 = st.number_input("Number of Deals Purchases", min_value=0)
amount4 = st.number_input("Number of Web Purchases", min_value=0)
amount5 = st.number_input("Number of Catalog Purchases", min_value=0)
amount6 = st.number_input("Number of Store Purchases", min_value=0)

All_Purchases = (amount3 + amount4 + amount5 + amount6) // 4

NumWebVisitsMonth = st.number_input("How often does the client visit the website per month?", min_value=0)

Recency = st.date_input(
    label="The last date the client visited the Market",
    min_value=dt.date(2005, 10, 10),
    max_value=dt.date.today(),
    value=dt.date.today(),
    key="Recency"
)
Recency = Date_Calculation(Recency)[2]

Complain = st.selectbox(
    "Has the customer filed a complaint in the last two years?",
    options=["Yes", "No"]
)
Complain = 1 if Complain == "Yes" else 0

# ===================== Prediction =====================
if st.button("Predict The Client Response", type="primary"):
    input_data = pd.DataFrame({
        "Education": Education,
        "Marital_Status": Marital_Status,
        "Income": Income,
        "Recency": Recency,
        "MntFruits": MntFruits,
        "NumWebVisitsMonth": NumWebVisitsMonth,
        "Complain": Complain,
        "Age": Age,
        "Transaction_Start_Time": Transaction_Start_Time,
        "AcceptedCmps": AcceptedCmps,
        "Proten_Products": Proten_Products,
        "All_Purchases": All_Purchases
    }, index=[0])

    input_data = scaler.transform(input_data)
    prediction = model.predict(input_data)
    res = "responded (accepted)" if int(prediction) == 1 else "not responded (rejected)"

    st.success(f"The client {user_name} has {res} to the marketing campaign 🎯")
