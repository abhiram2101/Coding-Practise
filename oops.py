"""
class Hotel:
    def hotel_specs(self):
        print("name is" +" "+ self.Name)
        print("price is" +" " + self.Price)
        print("type is" +" "+ self.Type)
hotel1 = Hotel()
hotel1.Name = "Ar aparts"
hotel1.Price = "23,000"
hotel1.Type = "4BHK"
hotel1.hotel_specs()

hotel2 = Hotel()
hotel2.Name = "Abc aparts"
hotel2.Price = "8000"
hotel2.Type = "2BHK"
hotel2.hotel_specs()

class dog:
    breed = input()
    breedone = "rare"
    breedtwo = "cross"
    hgt = "6 ft"
    clr = "white" 
    def dog_type(self):
        if self.breed == "white":
             print("the breed is" + " " + breed1.breedone+  " "+"color is"+ " "+ breed1.clr)
        else:
             print("the breed is" +" " +breed1.breedtwo)
breed1 = dog()
breed1.dog_type()

class Vehicle:
    def __init__(self, maxspeed , mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage
model = Vehicle(80 , 40)
print(model.mileage , model.maxspeed)

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Child_vehicle(Vehicle):
    pass
def seating_capacity(self, capacity,vehicle):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
bus = Child_vehicle("bus",80,45)

class Robot:
    color:"white"
def __init__(self,color):
    print("the color of bus is "+ " "+ self.color)
class Vehicle:
    name = "car"
    def por(self,name):
        print("the name is" +" " + Vehicle.name + "the color is " +" " + self.color)
por()


class Bar :
    mini=5000
    def bar_Details(self, name, cash, mini):
        self.name = name
        self.cash = cash
        self.mini = mini
        if cash <= 2000:
            print("unable to enter"+ " " + "minnimum pay is" +str(self.mini))
        else:
            print("entered successfully",bar1.name)
bar1 = Bar()
bar1.name = input()
bar1.cash = int(input())
bar1.bar_Details(bar1.name , bar1.cash , Bar.mini)

--> Python self , init practise
s1 = Student("ar",580)
print(s1.name)
print(s1.rno)

class Student:
    def __init__(self , name , rno):
        self.name = name
        self.rno = rno
    def print_d(self):
        print( self.name , self.rno)
s1 = Student("Ar",580)
s1.print_d()

class Student:
    def __init__(self):
        self.name = "ar"
        self.rno = 580
s1 = Student()
s2 = Student()
s1.name = "akki"
s2.rno = 569
print(s1.name)
print(s2.rno)

#Inheritance example
class Parent():
    def __init__(self , display,ram):
        self.display = display
        self.ram = ram
    def print_m1(self):
        print("display is {} ".format(self.display))
        print("ram is {} " .format(self.ram))
class Child(Parent):
    def __init__(self, display , ram , camera , price):
        self.camera = camera
        self.price = price
        Parent.__init__(self, display , ram)
    #def print_m1(self):
       # print("display is {}".format(self.display))
       # print("ram is {} ".format(self.ram))
        print("camera is {} ".format(self.camera))
        print("Price is {} ".format(str(self.price)))
m1 = Child("16 inch" , "8GB" , "35px" , 34000)
m1.print_m1()

#Polymorphism example
class Animal:
    def speak(self):
        pass
	#raise NotImplementedError("Subclass must implement this method")
class Dog(Animal):
    name = "dog"
    def speak(self):
        print(self.name)
        return "Woof!"

class Cat(Animal):
    name = "cat"
    def speak(self):
        print(self.name)
        return "Meow!"
animal1 = Cat()
animal2 = Dog()
print(animal1.speak())
print(animal2.speak())

class A:
    def __init__(Self):
        pass
    def print_d1(self):
        print("Parent class accessed ")
c1 = A()
c1.print_d1
# illustrating protected members & protected access modifier 
class details:
    _name="Jason"
    _age=35
    _job="Developer"
class pro_mod(details):
    def __init__(self):
        print(self._name)
        print(self._age)
        print(self._job)
 
# creating object of the class 
obj = pro_mod()

class details:
    _name="Jason"
    _age=35
    _job="Developer"
class pro_mod(details):
    def __init__(self):
        print(self._name)
        print(self._age)
        print(self._job)
 
# creating object of the class 
obj = pro_mod()
# direct access of protected member
print("Name:",obj._name)
print("Age:",obj._age)

from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def print_d1(self):
        print("Parent class accessed ")
class B(A):
    def print_d1(self):
        super().print_d1()
        print("child class accessed ")
c1 = B()
c1.print_d1

def fizzBuzz(n):
    for i in range(1,n+1) :
        if i%3==0 and i%5==0 :
            print("FizzBuzz")
        elif i%3 ==0 and i%5!=0 :
            print("Fizz")
        elif i%3!=0 and i%5==0 :
            print("Buzz")
        else:
            print(i)
fizzBuzz(15)

"""























