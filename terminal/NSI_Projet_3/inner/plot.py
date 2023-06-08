import matplotlib.pyplot as plt
x = [(3, 546), (14, 726), (4, 820)]
plt.scatter(*zip(*x))
plt.show()