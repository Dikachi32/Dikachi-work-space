# a = float(input("enter number 1:"))
# b = float(input("enter number 2:"))
# print(a+b)
# print(a-b)
# print(a8b)
# print(a/b)

# FUNCTION
# A function is a block of code that performs in a given task. Instead of writing the 
# same logic over and over, you define it once and call it whenever you need it e.g

# Write a function called greet that prints:
# Hello, Ai Engineer!
# def greet():
#     print("Hello, Dikachi the Tech bro!")
# greet()

# #-- Write a function called say_hello that prints:
# # "Hello, future AI engineer!"
# def say_hello():
#     print("Hello Dikachi, future AI engineer!")
#     print("Winners never quit!")
#     print("Your born for greatness")
# say_hello()


##-- Parameters and Arguments Functions become powerful when they accept inputs.
# def greet(name):       # Parameter → variable inside function (name)
#     print(f"Hello {name}")
# greet("Dikachi")   # Argument → value passed ("Dikachi")


##.. Create a function square(num) that prints the square of a number.
# def square(numb):
#     print(f"{numb} x {numb} is {numb * numb}")
# square(3)

#.. def square(numb):
#     return numb * numb

# result = square(9)
# print(f"The square is: {result}")

#..Return Values (VERY IMPORTANT) Instead of printing, functions should usually return values.
# def add(a, b):
#     return a + b
# result = add(2, 3)
# print(result)

#..Write a function multiply(a, b) that returns the result.
# def multiply(a, b):
#     return a * b
# result = multiply(2, 2)
# print(result)

# def math_operations(a, b):
#     return a * b, a + b
# sum_result, product_result = math_operations(2, 3)
# print(sum_result)
# print(product_result)

##.. Create a function power(base, exponent=2) that returns the result.
# def power(base, exponent):
#     return base ** exponent
# print(power(2, 10))  # base=2, exponent=10 → 1024 
# 
# OR

# def power(base, exponent):
#     return base ** exponent

# result = power(2, 10)
# print(f"The result is: {result}")

##- Create a function: def cube(n):It should: Return the cube (n³), Store result in a variable
# Print: The cube is: 27
# def cube(n):
#     return n * n * n

# result = cube(3)
# print(f"The cube is: {result}")

##- Return Values (VERY IMPORTANT) Instead of printing, functions should usually return values.
# def add(a, b):
#     return a + b
# result = add(2, 3)
# print(result)


##.. Write a function multiply(a, b) that returns the result.
# def multiply(a, b):
#     return a * b
# result = multiply(2, 4)
# print(result)

##- Keyword Arguments
# def introduce(name, age):
#     print(f"My name is {name} and i'm {age} years old.")
# introduce(age=25, name="Dikachi")

##- Write a function student(name, score) and call it using keyword arguments.
# def student(name, score):
#     print(f"My name is {name} and my score is {score}")
# student(name="Dikachi", score=92)
           # OR USING THE RETURN FUNCTION
# def student(name, score):
#     return f"My name is {name} and my score is {score}"
# result = student(name="Dikachi", score=92)
# print(result)

##-- Write a function that returns: the minimum the maximum of two numbers.
# def min_max(a, b):
#     return min(a, b), max(a, b)
# # Example usage
# minimum, maximum = min_max(5, 10)

# print("Minimum:", minimum)
# print("Maximum:", maximum)

## CHANGE DOLLAR TO POUNDS

def dollar2pounds():
    dollar = float(input("Enter amount in dollars: "))
    pounds = dollar * 0.75
    print(f"£{pounds}")
    return pounds

pounds = dollar2pounds()
print(pounds)

# def add():
#     a = float(input("enter number 1:"))
#     b = float(input("enter number 2:"))
#     print(a+b)

# def subtract():
#     a = float(input("enter number 1:"))
#     b = float(input("enter number 2:"))
#     print(a-b)
# # subtract()

# def dollar2pounds():
#     dollar = float(input("Enter amount in dollars: "))
#     pounds = dollar * 0.75
#     # print(f"£{pounds}")
#     return pounds


# pounds = dollar2pounds()
# print(pounds)

