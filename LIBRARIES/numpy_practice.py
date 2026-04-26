##. NumPy (Numerical Computing Backbone)
# 🧠 What it is (In AI Engineering)
# NumPy is the engine behind almost all numerical computation in AI.
# Every dataset, image, tensor, embedding → eventually becomes a NumPy array.
# Core Concept: Arrays (ndarray)
import numpy as np

# a = np.array([1, 2, 3])
# print(a)


# #  An array is a container that stores multiple values in a single variable, 
# # usually of the same data type, and organizes them in an ordered way.

# # Create Arrays
# np.array([1,2,3])
# np.zeros((2,3))
# np.ones((3,3))
# np.arange(0,10,2)
# np.linspace(0,1,5)

# # Array Operations (🔥 VERY IMPORTANT)
# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print(a + b)   # [5 7 9]
# print(a * b)   # element-wise multiplication

# # Indexing & Slicing
# a = np.array([10,20,30,40])

# print(a[1])      # 20
# print(a[1:3])    # [20 30]

# Matrix Operations (Used in ML Models)
# You multiply rows of A with columns of B:
# First row, first column: (1×5) + (2×7) = 5 + 14 = 19
# First row, second column: (1×6) + (2×8) = 6 + 16 = 22
# Second row, first column: (3×5) + (4×7) = 15 + 28 = 43
# Second row, second column: (3×6) + (4×8) = 18 + 32 = 50
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

result = np.dot(A, B)

# print(result)

## Statistics :  Adds all values and divides by how many there are.
#-- np.mean(a)
a = np.array([10, 20, 30, 40])      # total value = 100/4 = 25
# print(np.mean(a))


## Standard Deviation (Spread / Variability)  What it does
# Measures how far values are spread from the mean. e.g
#-- np.std(a)
a = np.array([10, 20, 30, 40])
# print(np.std(a))  # Answer is 11.18.... but how
# # Step 1: Find the mean
# np.mean(a) = 25
# # Step 2: Subtract the mean from each value
# 10 - 25 = -15  
# 20 - 25 = -5  
# 30 - 25 = 5  
# 40 - 25 = 15
# # So we get: [-15, -5, 5, 15]
# # Step 3: Square each result
# (-15)^2 = 225  
# (-5)^2  = 25  
# 5^2     = 25  
# 15^2    = 225
# # Now: [225, 25, 25, 225]
# # Step 4: Find the mean of those squares
# (225 + 25 + 25 + 225) / 4 = 500 / 4 = 125
# # Step 5: Take the square root: 11.18 × 11.18 ≈ 125 OR √125 = √(25 × 5)
# # √125 ≈ 11.18 Square root means: “What number multiplied by itself gives 125?”

import numpy as np

# print(np.sqrt(49))   # 7 x 7 = 49
# print(np.sqrt(50))   # 7.0710678... x  7.0710678... = 50


## Sum (Total): Adds everything together.
np.sum(a)
a = np.array([10, 20, 30, 40])

# print(np.sum(a))

# Put It All Together
a = np.array([10, 20, 30, 40])

# print("Mean:", np.mean(a))
# print("Std:", np.std(a))
# print("Sum:", np.sum(a))


#-- Task 1  Find mean: Find std: Find sum
# a = np.array([5, 10, 15, 20, 25])
# print("Mean:", np.mean(a))  # 5+10+15+20+25= 75/5
# print("Std:", np.std(a))    # 75 = 7.071067... x 7.071067... = 75
# print("Sum:", np.sum(a))    # total numba of everything = 75


#-- Task 2 What is the : mean? std?
b = np.array([1, 1, 1, 1])
print("Mean:", np.mean(b))  # 1+1+1+1 = 4/4=1
#Take every number in your data → subtract the mean from it
print("Std:", np.std(b))    # 1-1=0 1-1=0 1-1=0 1-1=0 Our answer is = 0

# Why is std what it is?

# Task 3 (Real ML Thinking)

# Normalize this:

# a = np.array([100, 150, 200])

# 👉 Use:

# (a - np.mean(a)) / np.std(a)