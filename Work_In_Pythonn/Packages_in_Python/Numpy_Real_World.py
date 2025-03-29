import numpy as np
import matplotlib.pyplot as plt
# Data Structure : [restaurant_id,2021,2022,2023,2024]
sales_data = np.array([
    [1,150000, 180000,220000, 250000], #Biryani
    [2,120000, 140000,160000, 190000], #Beijing Bites
    [3,200000, 230000,260000, 300000], #Pizza Hut
    [4,180000, 210000,240000, 270000], #Burger Point
    [5,160000, 185000,200000, 230000]]) #Chai Point

print(sales_data.shape)
print(" Sample Data For 1st 3rd restaurant : \n",sales_data[:,1:])

'''total sales per year'''
print(np.sum(sales_data,axis=0))
yearly_total = np.sum(sales_data[:,1:],axis=0) # HERE ,1 means we dont to add 1st coloumn. if we dealing  in column then we will use axis = 0
print(yearly_total)

# Minimum sales per restaurant
min_sales = np.min(sales_data[:,1:],axis=1) # if we dealing  in Rows then we will use axis = 1
print(min_sales)

# Maximum Sales  per restaurant 
max_sales = np.max(sales_data[:,1:] ,axis = 0)
print(max_sales)

# Avg sales for restaurant
avg_sales = np.mean(sales_data[:,1:],axis=1)
print(avg_sales)

cumulative_sales = np.cumsum(sales_data[:,1:],axis=1)
print(cumulative_sales)

# Ploting At Graphs
plt.figure(figsize=(10,6))
plt.plot(np.mean(cumulative_sales,axis=0))
plt.title("Average Cumulative sales accorss all restaurant: ")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

