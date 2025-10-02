import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score ,f1_score , r2_score , precision_score, silhouette_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.preprocessing import LabelEncoder , OneHotEncoder , StandardScaler
from sklearn.ensemble import RandomForestClassifier as RFC , GradientBoostingClassifier as GBC , VotingClassifier as VC
from Used_Methods import Re_arrange_Age


data = pd.read_csv("Data_marketing_campaign.csv" )
# print(data.isnull().sum())
data.dropna(inplace=True)
data.info()

# combine the results of all comapigns in one column as a toatal result

data["AcceptedCmps"] = ((data["AcceptedCmp1"] + data["AcceptedCmp2"] + data["AcceptedCmp3"] +   data["AcceptedCmp4"] +  data["AcceptedCmp5"]))/5
data.drop(columns=["AcceptedCmp1" , "AcceptedCmp2" ,"AcceptedCmp3" , "AcceptedCmp4" , "AcceptedCmp5"] ,inplace=True)

data["Proten_Products"] = (( data["MntMeatProducts"] + data["MntFishProducts"] ) // 2)
data.drop(columns=["MntMeatProducts" , "MntFishProducts" ] ,inplace=True)

# combine all Purchases 
data["All_Purchases"] = ((data["NumDealsPurchases"] + data["NumWebPurchases"]  +  data["NumCatalogPurchases"] + data["NumStorePurchases"])//4)

data.drop(columns=["NumDealsPurchases" , "NumWebPurchases" , "NumCatalogPurchases"  , "NumStorePurchases"] ,  inplace=True)

# data['Imprtant_Products']  = ((data["MntSweetProducts"] + data["MntGoldProds"] // 2))
data.drop(columns=["MntSweetProducts" , "MntGoldProds"] ,  inplace=True)


data.info()
'''Marital_Status -> {'Single' : 0  , 'Married' : 1 , 'Together' : 2 , 'Divorced' :3  , 'Widow' :4 }
'''

# has  a data  in out of the range  , so it is droped
data.drop(columns=["MntWines"] ,inplace=True)

# Now we can convert the age values to ranges its map added below this line and  : - 


    
data["Age"] = data["Age"].apply(func=Re_arrange_Age)

# Note that Response is the target

# see all outlayers for all columns -> 
# for column in data.columns :
#    plt.figure(figsize=[10, 10])
#    sns.boxplot(data=data , x=column )
#    plt.xlabel(xlabel=f"The data of \' {column} \' " , loc="center")
#    plt.show()

# names of columns that contains outlayers -> Income , MntFruits , NumWebVisitsMonth  ,  Proten_Products , All_Purchases , Important_Products
 

# for column in [ "NumWebVisitsMonth" , "NumWebVisitsMonth"  , "Proten_Products" , "All_Purchases" ] :
#         result = compute_outlayers(data=data , column_name=column)
#         if type(result) is tuple :
#           print(column , result[0])
          # here we will delete the outlayers
        #   data[column] = data[data[column] > result[1] & data[column] < result[2] ][column] 
        #   print(f'The column {column} has deleted its quatiles')
          
        # elif type(result) is tuple and result[0] <= 5.0  :
        #    print(f"The  column {column} has quatiles but less than 5.0")
        # else :
        #     print(f'The problem is in column \'{column}\'' , end= f"\n{'*' * 50}\n")


x = data.drop(columns=['Response'])
y = data['Response']

x_train , x_test , y_train , y_test = train_test_split(x , y , test_size=0.2 , random_state=42 , stratify=y)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)


models =  [LogisticRegression() , RFC() ]

models[0].fit(x_train , y_train)

y_train_pred = models[0].predict(x_train)
y_test_pred = models[0].predict(x_test)

train_accuracy =  accuracy_score(y_train , y_train_pred)
test_accuracy =  accuracy_score(y_test , y_test_pred)

print(f'Accuracy Score using {models[0]} for Train ->{train_accuracy}')
print(f'Accuracy Score {models[0]} for Test ->{test_accuracy}\n{'*'*50}')


models[1].fit(x_train , y_train)

y_train_pred = models[1].predict(x_train)
y_test_pred = models[1].predict(x_test)

train_accuracy =  accuracy_score(y_train , y_train_pred)
test_accuracy =  accuracy_score(y_test , y_test_pred)

print(f'Accuracy Score using {models[1]} for Train ->{train_accuracy}')# 0.9944008958566629
print(f'Accuracy Score {models[1]} for Test ->{test_accuracy}\n{'*'*50}') # 0.8747203579418344

# So the used model is Random forest 

import pickle as pk 
import joblib as jb

# with open("Marketing_model.pkl" , 'wb') as model_file :
#    pk.dump(models[1] , model_file)
# with open("Marketing_scaler.pkl" , 'wb') as scaler_file :
#   pk.dump(scaler , scaler_file)

'''with open("Marketing_model.pkl" , 'wb') as model_file :
  jb.dump(models[1] , model_file)

with open("Marketing_scaler.pkl" , 'wb') as scaler_file :
  jb.dump(scaler , scaler_file)'''

# print('The model file and scaler file saved sucessfully ....')

data.info()

print("Recency" , data["Recency"].unique())
print("Complain"  , data["Complain"].unique())


