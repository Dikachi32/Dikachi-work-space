## VARIABLES are used for storing data, giving meaning to data, and making 
# code readable and understandable. e.g

##1 Variables allow user interaction.
# name = input('Enter your name ')
# print(name.title())


#name = input("Enter your name? ")
#color = input("Enter your favourite color? ")
#print(f"{name} likes {color}")


##2 They help connect different parts of your program
name = 'baron dikachi'       #box name → contains "baron dikachi"
display = (f'Hello {name.title()} the tech bro.')  
# print(display)

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# print(f'Hello {name}')
# print(f'You are {age} years old')

##3 Ask for user name and return the initials
#first_name = input('Enter your first name: ')
#first_name_initial = first_name[0:1].upper()

#middle_name = input('Enter your middle name: ')
#middle_name_initial = middle_name[0:1].upper()

#last_name = input('Enter your last name: ')
#last_name_initial = last_name[0:1].upper()

#print(f'Your initials are: {first_name_initial} {middle_name_initial} {last_name_initial}')


name = "Dikachi"   # string
age = 20           # int
height = 5.9       # float
is_student = True  # boolean

##4 Create variables for: a product name its price whether it's in stock (True/False)
# Print all of them
product_name = 'iphone'
price = 50000
is_in_stock = True

# print(product_name)
# print(price)
# print(is_in_stock)

##4 Using the IF statement 
product_name = input("Enter product name: ")
price = int(input("Enter price: "))
is_in_stock = input("Is it in stock (True/False): ").title()

if is_in_stock == "True":
    print(f"Product: {product_name}")
    print(f"Price: {price}")
    print(f"In stock: {is_in_stock}")

else:
    print('Sorry, this product is currently unavailable.')

