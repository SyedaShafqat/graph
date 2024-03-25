import matplotlib.pyplot as plt

arr1 = [1, 2, 6, 4, 5, 6]
arr2 = [2, 3, 4, 8, 6, 7]
arr3 = [3, 4, 0, 6, 7, 8]

plt.plot(arr1)
plt.plot(arr2 )
plt.plot(arr3)

plt.xlabel('x')
plt.ylabel('y')
plt.title('graph')
plt.show()