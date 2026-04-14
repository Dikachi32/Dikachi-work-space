## EXPLORING STRING METHODS; UPPER(), LOWER(), LEN(), STRIPE(), TITLE();

name1 = 'Onyedikachi'
name2 = 'dikaChi'

# ## .upper() method creates a new version of your string where every 
# lowercase letter is turned into a capital letter.
# print(name1.upper())

# ## .lower() method does the exact opposite; it takes any capital 
# letters and turns them into lowercase.
# print(name1.lower())

## .title() is a string method that converts the first letter of 
# every word to uppercase and the rest to lowercase.
# print(name2.title())

## len() function counts every single character in a string, including 
# spaces, punctuation, and special characters.
# print(len(name2))

sentence = "dikachi is now coding for the world"
# print(sentence)
# print(sentence.upper())
# print(len(sentence))

# print(sentence.title())

#  startswith() is a string method used to check if a string begins with
#  a specific sequence of characters. It returns a Boolean value: True or False.
print(sentence.startswith("Dikachi"))

#  strip() is a string method used to remove leading and trailing whitespace (spaces, tabs, and newlines) from a string
name3 = "    ONYEDIKACHI   "
# print(len(name3))
# print(name3)
# print(name3.strip())

