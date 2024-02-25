#name = input("Input your name: " )
#age = int(input("Input your age: " ))
#print("Your name is " + name + " and you are ", age )
#sentence = input("Enter your sentence: ")
#print("Your sentence is:" + sentence)
#word1 = input("Enter the word to replace:")
#word2 = input("Enter the word to replace it with:")
#print(sentence.replace(word1, word2))
#sentence2 = input("Enter your sentence: ")
#print("Your sentence is:" + sentence2)
#word3 = input("Enter the word to replace:")
#word4 = input("Enter the word to replace it with:")
#print(sentence2.replace(word3, word4))


countries = ['Brazil', 'France', 'Nigeria', 'Spain']
print(countries)
print(countries[1:4])
print(type(countries))
countries[0] = "Kenya"
print(countries)
countries[3] = "Uganda"
print(countries)
#starting from the back
print(countries[-2])
print(len(countries))
#list constractors double round brackets
classes = list(('Brazil', 'France'))
print(classes)
#LIST METHODS
list1 = [1, 2, 3, 4, 5]
list2 = ["banana", "apple", "orange", "mango"]
#printing the two lists together
list1.extend(list2)
print(list1)
list2.append("cherry")
print(list2)
print(len(list2))
#adding an object at a particular index in a list
list2.insert(1,"berry")
print(list2)
#removing from a list
list2.remove("apple")
print(list2)
#clearing the list
list2.clear()
print(list2)
#index of object
list2 = ["banana", "apple", "orange", "mango", "mango"]
print(list2)
print(list2.index("mango"))
#counting number of times object is repeated in a list
print(list2.count("mango"))
#printing in order
list1 = [4, 3, 5, 1, 2]
list1.sort()
print(list1)
#printing in reverse
list1.reverse()
print(list1)
list3 = list2.copy()
print(list3)
#removing the last value
list2.pop()
print(list2)
list2.pop(1)
print(list2)
#TUPLES
#you cannot change a value in a tuple
three = (1,2,3,"home")
print(three)
#tuples allow repetition of values
print(len(three))
strings = ['apple', 'banana', 'orange']
booleans = [True, False, True, False]
print(booleans)
print(type(three[0]))

#IF STATEMENTS


a = 4
b = 3

if a >= b:
    print("True")

c = 7
d = 8

if a == b:
    print("A equals B")
else:
    print("A not equals B")

x = False
y = 5

if x == True:
    print("X is true")
elif x == False:
    print("X  is False")
else:
    print("X is none of the two")




#EXAMPLE1 - CHECKING THE DATA TYPE
value = input("Input a value: ")

if type(value) == str:
    print(value + " is a string")
elif type(value) == int:
    print(value + " is an integer")
elif type(value) == list:
    print(value + " is a list")
else:
    print("Invalid input")

#EXAMPLE2 - IF A NUMBER IS DIVISIBLE BY 5
value2 = int(input("Input a number: "))

if value2%5== 0:
    print(value2, "can be divided by 5")
else:
    print(value2, "cannot be divided by 5")

#EXAMPLE - CHECKING IF LENGTH (REVIEW LATER)

#value3 = input("Enter your sentence: ")

#if value3<10:
    #print(value3, "is less than 10")
#else:
    #print(value3, "is more than 10")













