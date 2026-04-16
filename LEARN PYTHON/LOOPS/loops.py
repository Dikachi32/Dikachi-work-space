## LOOP
## A loop is a way to repeat a block of code multiple times without rewriting it.
## Instead of doing:
## print(0)
## print(1) 
## print(2)
## print(3). e.g

# for i in range(4): 
#     print(i)
#--- range(4) generates numbers starting from 0 up to 3 It does NOT include 4
# for i in range(1,4):
#     print(i)
# --- What it does:Starts from 1 Stops before 4



# ## RANGE FUNCTION:- range(start, end, step) Start = 0 End = 100 (NOT included) Step = 10
# for i in range(0, 100, 10):
#     # print(i)

# ## TYPES OF LOOPS IN PYTHON
# -##- 1. FOR LOOP means do this task at a specific number of times without going beyound ur command. e.g
# students = ["dikachi", "maluchi", "phillip", "ebere"]
# for student in students:
#     print(f"Hello {student}".title()) ## it goes through each item one by one automatically....

## Loop through a list of names:
#* fruits = ["apple", "banana", "mango","carrot", "orange"] 
# for fruit in fruits:
#     print(fruit)

#* name = ["Chisolum", "Onyedikachi", "Amarachi", "Ekenechukwu", "Kosarachi"]
# for names in name:
#     print(f"Hello {names} you are my blood we are one family.")


# Create a list of 5 numbers and print: each number its square
# num = [22, 33, 44, 55, 66]
# for numbers in num:
#     print(numbers, numbers ** 2)

#     # OR
# num = [22, 33, 44, 55, 66]
# for numbers in num:
#     print("Number:", numbers)
#     print("Square:", numbers ** 2)

# ## LOOPING THROUGH A STRING:- Loop goes character by character
# name = "Dikachi Sunday"
# for character in name:
#     print(characer)

# # Loop through a word and: print only vowels (a, e, i, o, u)
# vowels = ["a", "e", "i", "o", "u"]
# for letters in vowels:
#     print(letters)

# # Loop through range: Print all odd numbers from 1 to 15.
# for i in range(1,16):
#     print(i)

#. Looping Through Data (Dictionary)
# student = {"name": "Dikachi", "age": 20, "score": 85}
# for key, value in student.items():
#     print(key, value)

# Create a dictionary of 3 items and: print only the values, print only the keys
favourite = {"food": "rice", "fruit": "apple", "color": "white"}
# for value in favourite.values():
#     print(value); 
# for keys in favourite.keys():
#     print(keys)
##What you should understand (important):
##  .values() → gives you only the values
##.keys() → gives you only the keys 
## .items() → gives you both (key, value).

# for keys, value in favourite.items():
#     print(keys,value)


# ## BREAKSTATEMENT:- Print each character When it finds a space (' ')👉 Stop the loop immediately
# name = "Dikachi Sunday"
# for character in name:
#     print(character)
    # if character == ' ':
    #     break

# ## INPUT FOR LOOP
# for i in range(4):
#     name = input('Enter Your Name: ')
#     print(f'Welocome {name}')

# ## collect all the data and print then at once
# inputs = []    # it keep the inputs and print all once
# for i in range(3):
#     name = input("Enter Your Name " + str(i+1) + ": ")
#     inputs.append(name)
# print(f"You're All Welcome {inputs}")

# ## 2. WHILE LOOP means keep doing this task as long as the condition is True,
# # unless stopped manually or with break. e.g
# z = 2
# while z < 10:
#     print(z)
#     z = z + 1 #or z += 1 without this ur loop will run forever

# Write a while loop that prints numbers from 10 down to 1.
# numb = 10
# while numb >= 1:
#     print(numb)
#     numb -= 1
#numb >= 1 → keeps the loop running from 10 down to 1
#numb -= 1 → decreases the number each time (same idea as count += 1, but subtracting)

# ## TRAFFIC LIGHT COUNTER EXAMPLE
# start = 10
# color = 'red'
# # print(f"Traffic light is {color}")

# while start >= 0:
#     print(f'hold = {start}')
#     start = start - 1   # counts down
#     if start < 0:
#         color = 'GREEN'




# # A PASSWORD AND USERNAME CHECKER
# # default_username = 'Dikachi'
# # default_password = 'root1'
# # num_of_attempts = 0

# # while True:
# #     if num_of_attempts >= 3:
# #         print('You have exhausted the number of attempts')
# #         print('Please contact the admin via mail')
# #         break

# #     username = input('Please input your username: ')
# #     password = input('Please input your password: ')
# #     if username != default_username:
# #         print('Incorrect Username, Please try again./n')
# #         num_of_attempts = num_of_attempts + 1
# #     elif password != default_password:
# #         print('Incorrect password, Please try again./n')
# #         num_of_attempts = num_of_attempts + 1
# #     else:
# #         print('Your username and password are correct')
# #         print('You are logged in')
# #         break

# # EXAMPLE USING BREAK AND CONTINUE

# # for i in range(15):
# #     if i % 5 == 0:
# #         continue
# #     if i >= 10:
# #         break
# #     if i % 2 == 0:
# #         print(f'{i} is odd')
# #     else:
# #         print(f'{i} is even')



# # Project: Register only canadians for a contest
# # Create an empty list
# # create a loop
# # Get the name and country of the user
# # If the country is canada, store in list
# # If not canada, say they are not eligible
# # print the list of canadian contestants at the end

# # canadian_contestants = []
# # for i in range(5):
# #     name = input("Enter your name: ")
# #     country = input("Enter your country: ")
# #     # Remove whitespace and convert to lower case
# #     country = country.strip().lower()
# #     name = name.strip().title()
# #     if country == "canada":
# #         canadian_contestants.append(name)
# #         print(f'{name} has been register for the contest.')
# #     else:
# #         print(f'Hi {name}, you are not eligible for the context')

# # print("\nList of canadian contestants:")
# # for contestant in canadian_contestants:
# #     print(contestant)
