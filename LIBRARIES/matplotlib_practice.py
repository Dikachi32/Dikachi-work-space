# ## MATPLOTLIB is for visualizing data. 👉 Matplotlib helps you SEE what your data is saying.
# As an AI engineer, you don’t just train models — you: 1. explore data 2. debug models 
# 3. explain results.     Matplotlib is critical in all three.

import matplotlib.pyplot as plt  # import matplotlib for plotting

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# plt.plot(x, y)
# plt.show()

##.. 1. Plot numbers from 1–10 on x-axis 2. Plot their squares on y-axis

# Step 1: Create x values (numbers from 1 to 10)
x = list(range(1, 11))   # [1, 2, 3, ..., 10]

# Step 2: Create y values (square of each number)
y = [i**2 for i in x]    # [1, 4, 9, ..., 100]

# Step 3: Plot the values
# plt.plot(x, y)           # draw line graph

# # Step 4: Add labels and title
# plt.xlabel("Numbers (1–10)")        # label for x-axis
# plt.ylabel("Squares")               # label for y-axis
# plt.title("Plot of Numbers vs Their Squares")  # title of the graph

# plt.show()  # Step 5: Show the graph


##.. Histogram (VERY important in ML)
data = [10, 20, 20, 30, 30, 30, 40]

# plt.hist(data)
# plt.show()

##.. Generate 50 random numbers, Plot histogram
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(0, 100, 50)

# plt.hist(data, bins=10)
# plt.show()


##..Scatter Plot (SUPER IMPORTANT)
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

# plt.scatter(x, y)
# plt.show()


## Create two lists where y = 3x + noise Plot scatter, Observe if it looks linear
x = np.arange(1, 51)
noise = np.random.randn(50) * 5
y = 3 * x + noise

# plt.scatter(x, y)
# plt.show()



##. Labels & Titles (This is what makes your work look professional.)
# plt.plot(x, y)
# plt.title("My First Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

#. Plot any data: Add title, xlabel, ylabel, Try changing title to something meaningful
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.title("Relationship Between Study Time and Score")
plt.xlabel("Study Time (hours)")
plt.ylabel("Score")

plt.show()