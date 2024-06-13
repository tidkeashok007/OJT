import numpy as np
import matplotlib.pyplot as plt

#dataset
x = [1,2,3,4,5]
y = [2,3,5,7,11]


#create a plot for our data
plt.plot(x,y)

#customization for the plot

#ADD a title
plt.title('Line Plot')

#Add the labels
plt.xlabel("x-axix")
plt.ylabel("y-axis")

#output the plot
plt.show()