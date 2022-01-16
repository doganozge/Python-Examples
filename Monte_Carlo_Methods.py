# Import numpy library.
import numpy as np

# Create 100.000.000 points.
def pi_number(points = 100000000):
    counter = 0
    
    # Create a random number for x and y axis.
    for i in range(points):
        x = np.random.rand() 
        y = np.random.rand()
        
        # If points are in the circle, increase number of points by one
        if np.square(x) + np.square(y) < 1:
            counter+=1
    # Return the Pi number.
    return 4 * float(counter) / points
    
print(pi_number())