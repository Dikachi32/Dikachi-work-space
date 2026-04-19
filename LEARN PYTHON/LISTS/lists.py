## LIST is a collection of items stored in a single variable.
# numbers = [22, 33, 44, 55]
# print(numbers)
# name = ['Dikachi', 'Abuchi', 'Ebuka', 'Maluchi']
# print(name)
# mixed = ['Dikachi', 22, True, 3.3]
# print(mixed)

#- ✅ Task 1: Create a list called cities with 5 city names and print it.
# cities = ['Enugu', 'Owerri', 'Aba', 'Awka', 'Abakiliki']
# print(cities)

##-- Accessing List Items (Indexing) Each item has an index (starting from 0
# cities = ['Enugu', 'Owerri', 'Aba', 'Awka', 'Abakiliki']
# print(cities[0]) # Enugu
# print(cities[-1]) # Abakiliki the last index
# print(cities[3])  # Awka

##-- ✅ Task 2: Given:Print the first item, Print the last item using negative indexing
# colors = ["red", "blue", "green", "yellow"]
# print(colors[0])
# print(colors[-1])

##-- . SLICING LIST: You can get a range of items:
# numbers = [1, 2, 3, 4, 5]
# print(numbers[1:4])  # [2, 3, 4]
# # Variations:
# print(numbers[:3])   # [1, 2, 3]
# print(numbers[2:])   # [3, 4, 5]

##- Slice this list to get only middle values:

# data = [10, 20, 30, 40, 50]
# print(data[1:4])  #👉 list[start:stop] i

##-- . CHANGING LIST ITEMS: Lists are mutable:
# numbers = [1, 2, 3]
# numbers[1] = 100

# print(numbers)  # [1, 100, 3]

#- Change "banana" to "mango":
# fruits = ["apple", "banana", "cherry"]
# fruits[1] = "mango"
# print(fruits)

##-- ADDING ITEMS: append() – adds at the end
# numbers = [1, 2, 3]
# numbers.append(4)
# insert() – adds at specific index
# numbers.insert(1, 10)
# print(numbers)

# #-:Create a list ['Dikachi', 'Abuchi', 'Ebuka', 'Maluchi'] 
# # Add 'Chisom' at the end Insert 'Chimdalu' at index 1
# name = ['Dikachi', 'Abuchi', 'Ebuka', 'Maluchi']
# name.append('Chisom')
# print(name)
# name.insert(1, 'Chimdalu')
# print(name)

##-- REMOVING ITEMS
#--- remove()
name = ['Dikachi', 'Abuchi', 'Ebuka', 'Maluchi']
# name.remove('Ebuka')
# print(name)
#--- pop()
# name.pop()      # removes last
# print(name)
# name.pop(1)     # removes index 1
# print(name)
# #--- del
# del name[0]
# print(name)

##. Looping Through Lists
# numbers = [1, 2, 3]
# for num in numbers:
#     print(num)

##. Loop through:
# scores = [90, 80, 70, 60]
# for num in scores:
#     print(num)

##. list Length
# numbers = [1, 2, 3]
# print(len(numbers))  # 3

# Find the length of:
# students = ["A", "B", "C", "D"]
# print(len(students))

##. Checking Items
# fruits = ["apple", "banana"]

# if "apple" in fruits:
#     print("Yes")

# # Check if "AI" exists in:
# tech = ["ML", "DL", "AI"]
# if 'AI' in tech:
#     print(True)

#.  Sorting Lists
#. Sort: nums = [10, 5, 8, 2]
#. Ascending: Descending:
# nums = [10, 5, 8, 2]
# nums.sort()
# print(f"Ascending: {nums}")

# nums.sort(reverse=True)
# print(f"Descending: {nums}")

# #. List Comprehension (VERY IMPORTANT ⚡)
# # Create a list of numbers from 1–10, but only even numbers.
# even =[x for x in range(1, 11)]
# print(even)

# #. Nested Lists (2D Lists)
# # Create a 2D list of 2 rows and 3 columns and print one element.
# # Create 2D list
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# # Print one element (row 1, column 2 → value 2)
# print(matrix[0][1])
# # matrix[0][1] → first row, second column
# # matrix[1][2] → second row, third column (which is 6)

#. Copying Lists: Copy a list and modify the copy without affecting original.
# list1 = [22, 33, 44]
# list2 = list1.copy()
# print(list2)

#. Combining Lists: Combine:
x = ["AI"] 
y = ["Engineer"]
z = x + y
print(z)
