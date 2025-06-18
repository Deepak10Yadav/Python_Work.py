import matplotlib.pyplot as plt
x = ["Java","Python","PHP","JS","C+","C++"]
pop = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.barh(x,pop,color = ('purple','orange','blue','red'))
plt.xlabel("Lang")
plt.ylabel("Popularity")
plt.grid(True,linestyle = '--',linewidth="0.5",color = 'black')
plt.show()