##1 VARIABLES are used in operations (logic & calculations.
# a = 5
# b = 5
# sum = a + b
# print(sum)

##2 swap their values: Output should be: a = 10 b = 5
a = 5
b = 10

a, b = b, a

# print(a)
# print(b)

a = 5
b = 10

temp = a
a = b
b = temp
# print(a)
# print(b)


x = 100
y = 200

x, y = y, x
# print(x)
# print(y)


##3 Create a variable balance = 1000
# add 500 subtract 200 Print final balance.
balance = 1000
balance = balance + 500
balance = balance - 200
#print(balance)

##4 calculate birth year
#birth_year = int(input("Enter Birth year: "))
#age = 2026 - birth_year
#print(age)

##5 Banking system: Ask user how much to withdraw
# Subtract it and Show remaining balance
# balance = 5000
# withdraw = int(input('Enter your withdraw amount: '))
# remaining_bal = balance - withdraw
# print(f'Your remaining balance is: {remaining_bal}')

## MODIFY IT
balance = 5000
withdraw = int(input('Enter your withdraw amount: '))
remaining_bal = balance - withdraw
if balance <= withdraw:
    print(f'Your remaining balance is: {remaining_bal}')
else:
    print('Insufficient funds')
    




##6 Fix this  Make it print:
# 100 + 50 = 150
price = 100
# print(f'{price} + 50 = {price + 50}')


