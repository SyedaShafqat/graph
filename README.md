# Plotting Graphs using Matplotlib

Below is a Python program using Matplotlib to plot multiple lines on a graph.

```python
import matplotlib.pyplot as plt

# Define data arrays
arr1 = [1, 2, 6, 4, 5, 6]
arr2 = [2, 3, 4, 8, 6, 7]
arr3 = [3, 4, 0, 6, 7, 8]

# Plot the data
plt.plot(arr1, label='Array 1')
plt.plot(arr2, label='Array 2')
plt.plot(arr3, label='Array 3')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph')

# Add legend
plt.legend()

# Display the plot
plt.show()
![Graph Output](path/to/your/screenshot.png)
