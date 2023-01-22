import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=100)

# Defines the graph title and names the axes.
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Valeu", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Defines the size of the tags' labels.
plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()
