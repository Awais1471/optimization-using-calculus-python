import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 100)
area = x * (20 - x)

i = np.argmax(area)

print("Best length:", x[i])
print("Maximum area:", area[i])

plt.plot(x, area)
plt.scatter(x[i], area[i], color="red")
plt.xlabel("Length (m)")
plt.ylabel("Area (m²)")
plt.title("Maximum Area Optimization")
plt.grid()
plt.show()
