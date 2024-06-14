#starting point

#number of iteration

#example of gradient decent

x=10
learning_rate =0.1
num_interation = 100
 #create a loop for gradient descent

for i in range(num_interation):
     #compute our gradient
     gradient = 2 * x

     #update the x with new parameter that is new x
     x = x- learning_rate * gradient
     print(f"iteration {i+1}: x = {x}, f(x) = {x**2}")

print(f"minimum value of the x:{x}")  