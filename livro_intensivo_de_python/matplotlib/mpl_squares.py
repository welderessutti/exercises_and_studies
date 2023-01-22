import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=5)

# Defines the graph title and names the axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Defines the size of the tags' labels..
plt.tick_params(axis="both", labelsize=14)

plt.show()
