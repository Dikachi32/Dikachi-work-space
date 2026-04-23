##. A tuple is an ordered collection of items in Python—just like a list.But the key difference is:
# Tuples are immutable (you cannot change, add, or remove items after creation)

# my_tuple = (10, 20, 30)
# print(my_tuple)

# #. Create a tuple that contains: your name, your age, whether you are 
# # learning AI (True/False) Then print it.
# data = ("Dikachi", 20, "True")
# print(data)

##. Indexing and Accessing Tuples
ai_data = ("Programming", "Python", "Machine Learning", "Deep Learning")

# print(ai_data[0])  # Programming
# print(ai_data[2])  # Machine Learning
# print(ai_data[-1])  # Deep Learning

#. Create a tuple of 5 AI-related topics (e.g. ML, NLP, CV, etc.)
# Then:print the first item, print the last item, print the middle item
ai_topic = ("ML", "NLP", "CV", "SVM", "LLM")
# print(ai_topic[0])
# print(ai_topic[-1])
# print(ai_topic[2])

##. Immutability (MOST IMPORTANT CONCEPT) Tuples cannot be changed.
# t = (1, 2, 3)
# t[0] = 100  # ❌ ERROR

#. attempt to: change the first value Write down what error you get and what it means.
m = (10, 20, 30, 40)
# m[0] = 11             # you cannot change, add, or remove items.
# print(m)

# If you want to change a tuple, you must: Convert to list
# m = list(m)          # Converted to list
# m[1] = 22
# print(m)

##. Tuple Packing and Unpacking (VERY IMPORTANT IN AI)
## PACKING e.g
model_info = ("ResNet", 50, "ImageNet")
## UNPACKING
name, layers, dataset = model_info

# print(name)
# print(layers)
# print(dataset)

##. Create a tuple with: model name: accuracy: loss
#Then unpack it into variables and print each one separately.
# model_info = ("NeuralNetV1", 0.92, 0.15)

# model_name, accuracy, loss = model_info
# print("Model Name:", model_name)
# print(f"Accuracy: {accuracy}")
# print(f"Loss: {loss}")


##. Tuple Methods (Limited but useful) Tuples have only two main methods:
#-- count()
# d = (1, 2, 2, 3)
# print(d.count(2))  # 2 .count() → number of times value appears
# #-- index()
# print(d.index(3))  # 3 is at position 3  .index() → position of first occurrence
# print(d.index(2))

##. Create a tuple: count how many times 5 appears: find the index of 20
f = (5, 10, 5, 20, 5)
# print(f.count(5))
# print(f.index(20))


##. Nested Tuples (REAL AI STRUCTURES) Tuples can contain other tuples:
dataset = (
    ("image1.jpg", 1),
    ("image2.jpg", 0),
    ("image3.jpg", 1)
)

#. Create a nested tuple with 3 students:
# Each student should have: name: score:  Then print: second student’s score
student = (
    ("Dikachi", 95),
    ("Maluchi", 90),
    ("Philip", 92)
)
print(student[1][1])