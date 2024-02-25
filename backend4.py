#FUNCTIONS
#def- defining the function
def greetings_function():
    print("Welcome user")
greetings_function()
def cars_function():
    print("AUDI QUATRO")
cars_function()
def webs():
    print("I am a software developer")
webs()

def classes():
    print("safari")
classes()

def greetings_function2(names,score):
    print(names + " your score is " + str(score))
greetings_function2("JB",40)





def greetings_function(name,age):
    print("Welcome user " + name + " you are " + str(age) + " years old")
greetings_function("John",34)
#not known amounts
def greetings_function(*names):
    print("Welcome" + names[1])
greetings_function("John", "Tim", "Tom")

def salutation(name, location):
    print("Hello I am " + name + " from" + location)
salutation("Irungu"," K-road" )


def greetings_function(name,age):
    print("Welcome user " + name + " you are " + str(age) + " years old")

name = input("Enter your name: ")
age = input("Enter your age: ")
greetings_function(name, age)

def hello(location, score):
    print("Hello I live in " + location + " and my score is " + str(score))

location = input("Enter your location: ")
score = input("Enter your score: ")
hello(location, score)














