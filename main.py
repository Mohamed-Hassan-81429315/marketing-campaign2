import streamlit as st  , pandas as pd
import pickle as p , joblib as jb
import datetime as dt

from Used_Methods import Re_arrange_Age  , Date_Calculation
# from  fastapi import FastAPI 
# from flask import Flask

model = jb.load("Marketing_model.pkl")
scaler = jb.load("Marketing_scaler.pkl")

st.title(" Marketing Campagin Project \n  This is a project about market that show if the user/client has responsed to the \n computations or not as this helps the market to improve\n its strategies to  increase its clients\n\n Now you can fill the following forum to show if the client has responsed to the campagin or not" , anchor='center')

# ======================================================================

user_name = st.text_input("Client name" , placeholder='type the user name like \'Mohamed\'' ,  icon="👤" , max_chars=25 , value="Mohamed")
user_age = st.date_input(label='The client BirthDay like :- \'2004/12/27\'' , min_value=dt.date(1975 , 10 , 10) , max_value='today' , value=dt.date.today() , key="user_age" )
user_age = Date_Calculation(user_age=user_age) # returns the age of user as (year , month , day)
Age =  Re_arrange_Age(user_age[0]) # here we will pass the years of the user

Transaction_Start_Time = st.date_input(label='The date that the client starts in coming to Markrt like :- \'2005/1/1\'' , min_value=dt.date(2005 , 1 , 1) , max_value='today' , value=dt.date.today() , key="Transaction_Start_Time" )
preiord = Date_Calculation(Transaction_Start_Time)
Transaction_Start_Time = float(preiord[0] + (preiord[1]/12)) # here refers to if the user takes 10 years and 6 months then Transaction_Start_Time will take value 10.5 ,....etc
Marital_Status = st.selectbox("What is the martial status of the user/client ?" , options=["Single" , "Married" , "Divorced"  , "Widow", "Together"])
Marital_Status  = int(0) if Marital_Status == 'Single' else int(1) if Marital_Status == 'Married' else int(2) if Marital_Status == 'Together'  else int(3) if Marital_Status == 'Divorced' else int(4)
Income = float(st.number_input("What is the user Income ?" , min_value= 0  , step= 1 , icon="💵"))
Education = st.selectbox("What is the degree of your education ?" ,  options=["Basic" , "2n-Cycle" , "Graduation"  , "Master" , "PhD"])
Education =  float(2.0) if Education == "Graduation" else float(4.0) if Education == "PhD" else float(3.0) if Education == "Master" else float(1.0) if Education == "2n-Cycle" else float(0.0)

if "options" not in st.session_state :
  st.session_state.options = [ "None" , "Campagin 1" , "Campagin 2" ,"Campagin 3" , "Campagin 4"  , "Campagin 5"]
if "selected_campaigns" not in st.session_state :
  st.session_state.selected_campaigns = ['None']

# I want to change in  on_change parameter

Campaigns = st.multiselect("Select the campagines that the user/client responsed to  , If the user not responed to any of them select None" , options= st.session_state.options, default =st.session_state.selected_campaigns , max_selections = 5) 

if 'None' in Campaigns and len(Campaigns) > 1 :
   Campaigns = [option for option in Campaigns if option!='None'] # here 'None' will not appear again in  selected options

elif ('None' not in Campaigns and len(Campaigns) == 0) : # ('None' in Campaigns and len(Campaigns) == 1 ) 
  Campaigns = ['None']

AcceptedCmps= len([option for option in Campaigns if option!='None'])

amount1 = st.number_input("What is the amount of the meat that the user takes from Market ? like 10 Kg" , icon="🥩" , min_value = 0 ,  step=1)
amount2 = st.number_input("What is the amount of the fish that the user takes from Market ?like 5 Kg" , icon="🐟" , min_value = 0 ,  step=1)
Proten_Products = (amount2 + amount1 ) //2

MntFruits = st.number_input("What is the amount of the fruits that the user takes from Market ?like 5 Kg" , icon="🎰" , min_value = 0 ,  step=1)

amount3 = st.number_input("What is the Number of deals Purchases that the user has made until now ?" , min_value = 0)
amount4 = st.number_input("What is the Number of Web Purchases that the user has made until now ?" , min_value = 0)
amount5 = st.number_input("What is the Number of Catalog Purchases that the user has made until now ?" , min_value = 0)
amount6 = st.number_input("What is the Number of Store Purchases that the user has made until now ?" , min_value = 0)

All_Purchases =  (amount3 + amount4 + amount5 + amount6)// 4

NumWebVisitsMonth = st.number_input("How often does the user visits the website of the market at month ? like 20 times -> 20" , min_value=0)

Recency  =  st.date_input(label='The date that the client starts in coming to Market  ' , min_value=dt.date(2005 , 10 , 10) , max_value='today' , value=dt.date.today()  , key="Recency")
Recency = (Date_Calculation(Recency))[2] # refers to the number of days from the last purchase to data collection time

Complain = st.selectbox("Has The customer filed a complaint during the last two years ?" , options= ["Yes" , "No"] , placeholder="if the user complained during the latest years")
Complain = 1 if Complain =="Yes" else 0
if st.button(" Predict The Client Response " , type="primary" , icon="🎯") :
    input_data = pd.DataFrame({
        "Education" :  Education , 
        "Marital_Status" : Marital_Status , 
        "Income" : Income , 
        "Recency" : Recency ,
        "MntFruits" : MntFruits ,
        "NumWebVisitsMonth" : NumWebVisitsMonth,
        "Complain" : Complain ,
        "Age" : Age ,
        "Transaction_Start_Time" : Transaction_Start_Time ,
        "AcceptedCmps" : AcceptedCmps , 
        "Proten_Products" : Proten_Products ,
        "All_Purchases" : All_Purchases
    } , index=[0])
    input_data = scaler.transform(input_data)
    prediction = model.predict(input_data)
    res = '  responded \'accepted \' ' if int(prediction) == 1  else 'not responded \'rejected \' '
    st.success(f'The client {user_name} has {res} to the marketing campaign' , icon="🎯")
    
       



# =======================================================================================
# # delete 'None' from options and the selections if the user selected anything instead of 'None' 

# if 'None' in Campaigns and len(Campaigns) > 1 :
#   # delete 'None' from the selections
#   Campaigns = [option for option in Campaigns if option!='None'] # here 'None' will not appear again in options
# else :
#    Campaigns = Campaigns
   
# if 'None' in st.session_state.options  :
#     st.session_state.options.remove('None')

#     # if the user deleted all its choiced then we will restore None as default again

# if len(Campaigns) == 0  and ('None' in st.session_state.options) :
#       Campaigns = ['None']

# st.session_state.selected_campaigns = Campaigns
