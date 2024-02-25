my_dict = {
    "name": "Bree",
    "nationality": "United States",
    "country": "United States",
    "age" : 78,
    "is_tall": True,
    "friends": ["JB", "NYR", "JNR"]
}
#you can add a list to a data type
#duplicates are not allowed in dictionaries
print(my_dict)
print(my_dict["name"])
print(len(my_dict))

#CLASSES AND OBJECTS IN PYTHON
class Myclass:
    x = 5
    y = 8
    z = 7
p1 = Myclass
print(p1.x)
print(p1.y)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p2 = Person("JB",67)
print(p2.name)

class Man:
    def __init__(self,name,score):
        self.name = name
        self.score = score

name = input("What is your name?")
score = input("What is your score?")

p3 = Man(name, score)
print(p3.name)
print(p3.score)

# pass - used to bypass any error (if you do not have the data)












