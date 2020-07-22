# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path
data = pd.read_csv(path)
#Code starts here
data.rename(columns={'Total': 'Total_Medals'}, inplace = True)
# Data Loading 
data.head(10)

# Summer or Winter
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter') 
data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])

better_event=data['Better_Event'].value_counts().idxmax()
better_event
# Top 10

top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

# Plotting top 10
data_1=data[:-1]
data_1
top_countries=top_countries[:-1]
# Top Performing Countries
def top_ten(df,colname):
        
    top_10=df.nlargest(10, colname)

    country_list=list(top_10['Country_Name'])
    return country_list

top_10_summer=top_ten(top_countries,"Total_Summer")  
top_10_winter=top_ten(top_countries,"Total_Winter")
top_10=top_ten(top_countries,"Total_Medals")



if set(top_10_summer) & set(top_10_winter) & set(top_10):
    common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))
common

summer_df= data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data["Country_Name"].isin(top_10_winter)]
top_df=data[data["Country_Name"].isin(top_10)]

summer_df
plt.figure(figsize=(20,20))
plt.bar(summer_df["Country_Name"],summer_df["Total_Summer"])
plt.bar(winter_df["Country_Name"],winter_df["Total_Winter"])
plt.bar(top_df["Country_Name"],top_df["Total_Medals"])
plt.show()




summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer'] 
summer_max_ratio=max(summer_df['Golden_Ratio']) 
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name'] 

# Best in the world 

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter'] 
winter_max_ratio=max(winter_df['Golden_Ratio']) 
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']



top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals'] 
top_max_ratio=max(top_df['Golden_Ratio']) 
top_country_gold=summer_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']

data
data_1=data[:-1]
data_1["Total_Points"]=(data_1["Gold_Total"]*3)+(data_1["Silver_Total"]*2)+(data_1["Bronze_Total"]*1)
most_points=max(data_1['Total_Points'])
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
best=data[data['Country_Name']==best_country] 
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)




# Plotting the best



