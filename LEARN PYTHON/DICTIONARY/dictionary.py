##. A dictionary stores data in key → value pairs. Think of it like a real dictionary:
# student = {
#     "name": "David",
#     "age": 22,
#     "score": 90
# }
# # Word = key  "name" → key
# # Meaning = value "David" → value
# print(student["name"])

# #. Create a dictionary called car with: brand, year, price. Then print it.
# car = {
#     "brand": "Benz",
#     "year": 2025,
#     "price": 20000
# }
# print(car)
# print(car["price"])

#. Create a dictionary person and: Print one value using [], Print one value using .get()
person ={
    "name": "Dikachi",
    "age": 25,
    "job": "AI Engineer"
}
# print(person.get("name"))  #-- print only name
# print(person["job"])       #-- print only job
# person["gender"] = "Male"  #-- adding data
# person["age"] = 27         #-- updating data
# print(person)

# person.pop("age")          #-- Remove age
# del person["job"]          #-- Delete job
# print(person)

##. Looping Through Dictionary
# for key in  person:
#     print(key)

# for key, value in person.items():
#     print(key, value)

##. Loop through a dictionary and print: name → Dikachi, age → 22
student ={
    "name": "Dikachi",
    "age": 22,
    "salary": 2000
}
# for key, value in student.items():
#     print(f"{key} → {value}")

#. Checking if Key Exists
# if "name" in student:
#     print("Yes")
# if "age" in student:
#     print("True")

##. Dictionary Methods
# print(student.keys())    #-- print only keys
# print(student.values())  #-- print only Values
# print(student.items())   #-- print both keys and values

##. Nested Dictionaries (SUPER IMPORTANT FOR AI)
students ={
    "student1": {"name": "Dikachi", "score": 95},
    "student2": {"name": "Chisom", "score": 90}
}
# print(students["student2"]["name"]) 
# print(students["student1"])

##. Create a nested dictionary of 2 users: Each should have name and age Then print one user’s age.
user ={
    "num1": {"name": "philip", "age": 24},
    "num2": {"name": "Ebere", "age": 27}
}
# print(user["num2"]["age"])

# ##. Modify your code to: Print the name of num1 Loop through all users and print:
# for key, value in user.items():
#     print(f"{key} → {value["name"]}, {value["age"]}")

##. Dictionary Comprehension (Advanced but IMPORTANT)
numbers = {x: x*x for x in range(5)}
# print(numbers)

#-- Create a dictionary where: keys = numbers 1–5 values = cube of numbers
cubes = {i: i**3 for i in range(1, 6)}
# i**3 means i × i × i e.g (When i = 2, 2**3 = 2 × 2 × 2 = 8)
# print(cubes)

#. Copy a dictionary and: Change the copy Show original is unchanged
original = {
    "name": "Dikachi",
    "age": 22
}
# copy_dict = original.copy()         # Copy the dictionary
# copy_dict["age"] = 30               # Change the copy
# # Print both
# print(f"Original: {original}")
# print("Copy:", copy_dict)


#. Create a list of dictionaries: Each has name and score Print students with score > 
students = [
    {"name": "Dikachi", "score": 95},
    {"name": "Ebere", "score": 67},
    {"name": "Philip", "score": 89},
    {"name": "Ada", "score": 40},
    {"name": "John", "score": 76}
]
for student in students:
    if student["score"] > 50:
        print(student["name"], student["score"])