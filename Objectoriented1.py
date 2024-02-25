#Object Oriented Programming in Python
def hello():
    print("Hello")
#METHODS - IT IS A FUNCTION THAT GOES INSIDE A CLASS
home = "house"
print(home.upper())


string = "hello"
print(string.upper())
print(string.lower())

class Dog:
    def __init__(self,name):
        self.name = name
        print(name)
    def add_one(self,x):
        return x + 1
    def bark(self):
        print("bark")

d = Dog("tim")

class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
c = Cat("jb", "doe")
print(c.name)
print(c.name)

class Win:
    def __init__(self,name,position):
        self.name = name
        self.position = position
w = Win("John","rw")
w2 = Win("Jk","lw")
print(w.name)
print(w.position)

class One:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def set_name(self, name):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age = age
o = One("JB",23)
o2 = One("John",40)
print(o.get_name())
print(o.get_age())
print(o2.get_name())
print(o2.get_age())
o.set_age(30)
print(o.get_age())
o.set_name("John")
print(o.get_name())


class Five:
    def __init__(self, name, age, location, gender):
        self.name = name
        self.age = age
        self.location = location
        self.gender = gender
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age = age
    def get_location(self):
        return self.location
    def set_location(self,location):
        self.location = location
    def get_gender(self):
        return self.gender
    def set_gender(self,gender):
        self.gender = gender
f = Five("Peter", 34, "Juja", "Male")
f2 = Five("Bree", 24, "K_Road","Female")
f3 = Five("Robert", 19, "Kiambu", "Male")
print(f.get_name())
print(f.get_age())
print(f.get_location())
print(f.get_gender())
f.set_age(20)
print(f.get_age())
f.set_location("KU")
print(f.get_location())
f.set_name("ki")
print(f.get_name())
f.set_gender("Female")
print(f.get_gender())



#more numbers
class Student():
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade #0 - 100
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
            return value / len(self.students)

s1 = Student("tim", 19,73)
s2 = Student("nyr",25, 78)
s3 = Student("jill",19, 65)
course = Course("science",2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)
course.get_average_grade()
print(course.get_average_grade())

#INHERITANCE
class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

    def show(self):
            print(f"I am {self.name} and I am {self.age} years old and {self.color} ")

    def speak(self):
        print("meow")
class Dog(Pet):
    def __init__(self,name,age,pace):
        super().__init__(name,age)
        self.pace = pace
    def run(self):
        print(f"I am {self.name} and I am {self.age} and I am {self.pace}")
    def speak(self):
        print("bark")
p = Pet("tim", 30 )
print(p.show())
c = Cat("hope",45, "brown")
print(c.show())
y = Dog("jill",30,"45")
print(y.run())


class People:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = People("John", 36)

print(p1)

class Chelsea:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
c1 = Chelsea("Enzo",21)
print(c1)
class Zerson:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Zerson("John", 36)
p1.myfunc()

class Liverpool:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc2(self):
        print(f"Hello my name is {self.name} ")
p3 = Liverpool("Waluke", 76)
p3.myfunc2()

class Mls:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc3(self):
        print(f"Hello my name is {self.name} ")

m1 = Mls("Favour", 21)
m1.myfunc3()

class Reason:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc4(self):
    print("Hello my name is " + self.name)

p1 = Reason("John", 36)

p1.age = 40

print(p1.age)


class Season:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc5(self):
        print(f"Hello my name is {self.name}")
s=Season("Omondi", 16)
s.age = 38
s.myfunc5()
print(s.age)

class Won:
    pass

class Child:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Jsp(Child):
  def __init__(self, fname, lname):
    Jsp.__init__(self, fname, lname)
class Jsp2(Child):
  def __init__(self, fname, lname,age):
    super().__init__(fname, lname)
    self.age = 40
def all(self):
    print(f"Welcome {self.firstname} {self.lastname} to the class of {self.age}")

cp = Jsp2("john", "Doe",67)
cp.all




#Use the Person class to create an object, and then execute the printname method:

x = Child("Fin", "Doe")
x.printname()

#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

#Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.












