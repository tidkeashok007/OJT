import matplotlib.pyplot as plt


#data 
x = [1,2,3,4,5]
y1 = [1,4,9,16,25]
y2 = [1,2,3,4,5]

#create
plt.plot(x,y1,linestyle='-', color='b',linewidth=3,marker='o',markersize=8,markerfacecolor='orange')
plt.plot(x,y2,linestyle='-',color='r',linewidth=3,marker='x',markersize=8,markerfacecolor='yellow')


#title and label
plt.title('Customixed line plot grid')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

#create a legend method
plt.legend()

#add the value
plt.grid(True)

#Cusomise the grid
plt.grid(color='gray',linestyle='--',linewidth=1)
 
plt.show()
