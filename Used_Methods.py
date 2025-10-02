import pandas as pd 
from datetime import date 

def Date_Calculation(user_age : date) : # used in  main.py file  # used to compute the date from certain date dedicated by user untill this day
  years = (date.today().year - user_age.year)
  months = (date.today().month - user_age.month)
  days = (date.today().day - user_age.day)
  years = years if years > 0 else 0
  if months >= 0 :
        months =  months
  else :
        years -=1
        months = date.today().month
  if days >= 0 :
        days =  days
  else :
        months -=1
        days = 30 - date.today().day
  return (years , months , days)

def Re_arrange_Age(value) : # The following comment refers to the used values
    if  1<value<=20 :
        return 1
    elif  21<value<=40 :
      return 2
    elif  41<value<=60 :
      return 3
    elif  61<value<=80 :
      return 4
    elif  81<value<=100 :
      return 5
    elif  101<value<=120 :
      return 6
    elif  121<value<=140 :
      return 7
    else :
       return 8
    
'''
--------------------------------------------------------------
Age_range   |  Respresented_Character |  value_used_in_DataSet
--------------------------------------------------------------
1 - 20      |       A                 |       1 
--------------------------------------------------------------
21 - 40     |       B                 |       2 
--------------------------------------------------------------
41 - 60     |       C                 |       3 
--------------------------------------------------------------
61 - 80     |       D                 |       4 
--------------------------------------------------------------
81 - 100    |       E                 |       5 
--------------------------------------------------------------
101 - 120   |       F                 |       6 
--------------------------------------------------------------
121 - 140   |       G                 |       7 
--------------------------------------------------------------
> 140       |       H                 |       8
--------------------------------------------------------------
'''

# looking for the outlayers 
def compute_outlayers(data:pd.DataFrame , column_name: str):
    try :
         q1 = data[column_name].quantile(0.25)
         q3 = data[column_name].quantile(0.75)
         IQR = q3 - q1 
         low = q1 - IQR * 1.5
         high = q3 +  IQR * 1.5
         outlayers = data[(data[str(column_name)] < low ) | (data[str(column_name)] > high ) ] 
         percentage_outlayers = (( outlayers.shape[0] / data.shape[0] ) * 100)
         print(f"with \' {column_name} \' done until now" , end=f"\n{'#'*100}\n")
         return (percentage_outlayers , low , high )
    except :
           return column_name

