def school(subjects):
    print("I take " + subjects)
school("math")

def school2(subjects):
    print("I take " + subjects)
school2("math")

def employees(names):
    print(names + " head of department")
employees("Robert")


def teachers(age):
    print("I am " + str(age) + " years old")
teachers(23)


def players(first_name, second_name, location, age, score):
    print(first_name + second_name, "lives in " + location, "and is " + str(age) + " years old" + " and scored " + str(score))
players("Robert", " Irungu", "Kiambu", 23, 40)


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(country = "Kenya"):
    print("I am from " + country)
my_function("Uganda")
my_function()
my_function("Tanzania")
my_function("Zambia")


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)





def matunda(fruits):
    for x in fruits:
        print(x)
fruits = ["apple", "banana", "orange"]
matunda(fruits)


def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
























































