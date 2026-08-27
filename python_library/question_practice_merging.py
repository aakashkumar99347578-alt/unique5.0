import numpy as np
import pandas as pd

q1_path = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\quarter-1.csv')
q2_path = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\quarter-2.csv')
q3_path = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\quarter-3.csv')
items_path = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\items.csv')
ipl_match = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\ipl-matches.csv')
ipl_ball_by_ball_deliveries = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\IPL_Ball_by_Ball_2008_2022.csv')

# print("--------------------------------data frame of q1_paht--------------------------------------------")
# print(q1_path)

# print("--------------------------------data frame of q2_path---------------------------------------------")
# print(q2_path)

# print("--------------------------------data frmae of q3_path----------------------------------------------")
# print(q3_path)

# print("--------------------------------data frmae of items_path---------------------------------------------")
# print(items_path)

#print("----------------------------------data frame of ipl match------------------------------------------------")
#print(ipl_match)

#print("---------------------------------data frame of ipl match ball by ball --------------------------------------")
#print(ipl_ball_by_ball_deliveries)
# # Q1 : You are given three quater files, your job is to append these three files and make a single dataframe

# print("------------------------------------Questions 1--------------------------------------------------------")
# print(q1_path.merge(q2_path,on='order_id'))

# Q-2 : our are given a file items.csv which has item_id and item_name. Find out most sold items in each quarter.

print("----------------------------------Questions 2 ------------------------------------------------------------")
print(items_path.merge(q1_path,on='item_id').groupby(['item_id','item_name'])['quantity'].sum().sort_values(ascending=False).head(5))
print(items_path.merge(q2_path,on='item_id').groupby(['item_id','item_name'])['quantity'].sum().sort_values(ascending=False).head(5))

# Q-3 : Find out items which has made most revenue in each quarter

print("-------------------------------------------Questions3----------------------------")
merge_dataframe = items_path.merge(q1_path,on='item_id')
merge_dataframe['item_price_in_rupees'] = (merge_dataframe['item_price'].str.replace('$','',regex=False).astype(float))*95.49
print(merge_dataframe.groupby(['item_id','item_name'])['item_price_in_rupees'].sum().sort_values(ascending=False).head(1))

# Q-4 : Find out avg order price of each quarter.

print("--------------------------Questions4------------------------------------------------")
print(merge_dataframe.groupby(['item_id','item_name'])['item_price_in_rupees'].sum()/merge_dataframe.groupby(['item_id','item_name'])['quantity'].sum())

# Q-5 : From the IPL wala dataset you have to find the Purple cap holder each season.

print("------------------------------Questions - 5 --------------------------------------------")
print(ipl_match.merge(ipl_ball_by_ball_deliveries,on='ID').dropna(subset='player_out').groupby(['Season','bowler'])['isWicketDelivery'].sum().reset_index().sort_values(['Season','isWicketDelivery'],ascending=[True,False]).drop_duplicates(subset='Season',keep='first'))