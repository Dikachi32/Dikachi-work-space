## PYTHON COLLECTION DATA TYPES 

## (1): LIST is an ordered, changeable (mutable) collection of items. e.g
# create a list
fruits = ['mango', 'apple', 'banana', 'pawpaw', 'strawberry']
print(fruits)

## Ordered list has index: python starts counting from 0 not 1
print(fruits[0])

## Mutable can change any item from the list. e.g
# fruits[3] = 'Orange'
print(fruits)

## Add item to the list. e.g
fruits.append('Orange')
print(fruits)

## To remove item from the list. e.g
fruits.remove('mango')
print(fruits)

##(2): Tuple is an ordered unchangeable (immutable) collection of items. e.g
numbers = (10, 20, 30, 40, 50)
print(numbers)
## Tuple can't remove or  add an item in a list.
print(numbers[2])

## (3): Set does not maintain order and does not allow duplicate values. e.g
numb = {10, 20, 30, 40, 40}
print(numb)

## (4): Dictionary stores datas in key:value pairs. e.g
contact = {
    'fullname': 'Dikachi Baron',
    'email': 'dikachibaron@gmail',
      'number': '08100419419'
}
print(contact['email'])
print(contact['number'])

## INVENTORY is a single variable that can store or hold a mix of data types, such as integers (10), 
# strings ('orange'), floats (30.5), and booleans (True). e.g
fruit = [10, 30, 'mango', 'apple', 20.5, True]
# print(fruit)

# ## how to create an empty list. e.g
# empty_list = []
# empty_list1 = list()
# print(empty_list)
# print(empty_list1)
# # accessing element in a list. e.g
# print(fruit[3])

## Slicing is a way to extract a specific portion from an existing list using 
# the colon : symbol inside square brackets. e.g
# print(fruit[:])      ## gets everything on the list
# print(fruit[2])      ## get only the number two
# print(fruit[-1])     ## Get just the last item
# print(fruit[-2:])    ## Get the last two items
# print(fruit[:-1])    ## Get everything EXCEPT the last item
# print(fruit[-4:-1])   ## Get a middle range using negatives

## modify a list. e.g
animal = ['cat', 'rat', 'dog', 'horse', 'goat']
# print(animal)
# print(animal[2])    ## to print the index two
# animal[0] = 'fowl'  ## to replace the first index or animal 
# print(animal)
# animal.append('snake')  ## to add another item to the list
# print(animal)

# ## REMOVING item from the list wit .remove(), .pop(), .del()
# animal.remove('rat')  ## removes by value
# print(animal)
# animal.pop(0)          ## removes by index or position
# print(animal)
# del animal[:]            ## 	Removing a range or clearing memory. index can be used too
# print(animal)