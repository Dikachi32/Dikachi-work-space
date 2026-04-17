# a = float(input("enter number 1:"))
# b = float(input("enter number 2:"))
# print(a+b)
# print(a-b)
# print(a8b)
# print(a/b)

# FUNCTION
# A function is a block of code that performs in a given task. e.g

# Write a function called greet that prints:
# Hello, Ai Engineer!
# def greet():
#     print("Hello, Dikachi the Tech bro!")
# greet()

# #-- Write a function called say_hello that pints:
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
def power(base, exponent=2):
    return base ** exponent

result = power(3)
print(f"The result is: {result}")
##- Create a function: def cube(n):It should: Return the cube (n³), Store result in a variable
# Print: The cube is: 27
# def cube(n):
#     return n * n * n

# result = cube(3)
# print(f"The cube is: {result}")

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

