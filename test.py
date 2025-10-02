import pandas as pd
from Used_Methods import Re_arrange_Age

d = pd.read_csv("marketing_campaign.csv" , sep='\t')
d.info()
print(d["Dt_Customer"].unique())
# d2 = pd.read_csv("Data_marketing_campaign.csv")
# d.columns =  d.columns.str.strip()
# d2.columns =  d2.columns.str.strip()

# d.info()
# d.dropna(inplace=True)
# d2.dropna(inplace=True)

# d2["AcceptedCmps"] = ((d2["AcceptedCmp1"] + d2["AcceptedCmp2"] + d2["AcceptedCmp3"] +   d2["AcceptedCmp4"] +  d2["AcceptedCmp5"]))/5
# d2.drop(columns=["AcceptedCmp1" , "AcceptedCmp2" ,"AcceptedCmp3" , "AcceptedCmp4" , "AcceptedCmp5"] ,inplace=True)

# d2["Proten_Products"] = (( d2["MntMeatProducts"] + d2["MntFishProducts"] ) // 2)
# d2.drop(columns=["MntMeatProducts" , "MntFishProducts" ] ,inplace=True)

# combine all Purchases 
# d2["All_Purchases"] = ((d2["NumDealsPurchases"] + d2["NumWebPurchases"]  +  d2["NumCatalogPurchases"] + d2["NumStorePurchases"])//4)

# d2.drop(columns=["NumDealsPurchases" , "NumWebPurchases" , "NumCatalogPurchases"  , "NumStorePurchases"] ,  inplace=True)

# d2['Imprtant_Products']  = ((d2["MntSweetProducts"] + d2["MntGoldProds"] // 2))
# d2.drop(columns=["MntSweetProducts" , "MntGoldProds"] ,  inplace=True)


# d2.info()
'''Marital_Status -> {'Single' : 0  , 'Married' : 1 , 'Together' : 2 , 'Divorced' :3  , 'Widow' :4 }
'''

# has  a d2  in out of the range  , so it is droped
# d2.drop(columns=["MntWines"] ,inplace=True)

# Now we can convert the age values to ranges its map added below this line and  : - 


    
# d2["Age"] = d2["Age"].apply(func=Re_arrange_Age)


# print(d["Education"].value_counts())
# print("*"*20)
# print(d2["Education"].value_counts())

