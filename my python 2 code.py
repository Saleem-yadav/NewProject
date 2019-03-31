# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:43:15 2019

@author: 15145
"""

# a list of comprehension
cubes = [i**3 for i in range(5)]

print(cubes)


# a list comprehension
squares = [i*2 for i in range(10)]

print(squares)

# a list comprehension
evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)

#a list comprehension 
even = [2*i for i in range(10**100)]

print(even)


a = [x*10 for x in range(5,9)]

print(a)

# string formatting
nums = [4,5,6]
msg = "numbers: {0} {1} {2}"
format(nums[0],nums[1],nums[2])
print(msg)


#string formatting
a = "{x},{y}".format(x=5,y=12)
print(a)

#string formatting
a = "{x}, {y}".format(x=5, y=12)
print(a)


same = (",".join(["spam","eggs","ham"]))
print(same)


a = "spam"
b = a.upper()
print(b)


print(min(1,2,3,4,0,2,1))

print(max([1,4,9,2,5,6,8]))


print(abs(-99))


print(abs(42))


print(sum([1,2,3,4,5]))

print(round(2.578))


a=min([sum([11,22]), max(abs(-30),2)])
print(a)


nums = [55, 44, 33, 22, 11]
if all([i>5 in nums]):
    print("All larger than 5")
    
if any ([i % 2 == 0 for i in nums]):
    print("At least one is even")
    
for v in enumerate(nums):
    print(v)


nums= [-1,2,-3,4,-5]
if all([abs(i) < 3 for i in nums]):
    print(1)
else:

class student:
    def__init__(self,name):
        self.name = name
        
        
 test = Student

class animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color
        
fido = animal("fido","brown")
print(fido.color)        
        


class Cat(Animal):
    def purr(self):
        print("purr...")
        
class Dog:
    def __init__(self,color):
        self.color = color

fido = Dog("brown")
print(fido.color) 

class student:
    def __init__ (self,name):
        self.name = name
        
test = student("Bob")
print(test.name)        
    

class Dog:
    def __init__ (self,name,color):
        self.name = name
        self.color = color
        
    def bark(self):
        print("Woof!")
        
fido = Dog("fido","brown")
print(fido.name) 
print(fido.color)
fido.bark()    

class Dog:
    legs = 4
    def __init__ (self,name,color):
        self.name = name
        self.color = color
        
fido = Dog("Fido","brown")
print(fido.legs)
print(Dog.legs)
print(fido.name)
print(fido.color)    


class student:
    def __init__ (self,name):
        self.name = name
        
    def sayHi(self):
     print("Hi from" + self.name)
     
    def girl(self):
        print("hot")

s1 = student("Amy")
s1.sayHi()        
s1.girl()

### create a class animal and inheritance
class Animal:
    def __init__ (self,name, color):
        self.name = name
        self.color = color
        
class Cat(Animal):
    def purr(self):
       print("purr...")
       
class Dog(Animal):
    def bark(self):
        print("Woof!")
        
fido = Dog("Fido","brown")
print(fido.color)
fido.bark()
fido = Cat("samy","brown")
fido.purr() 
print(fido.color)
print(fido.name)

##superclass and subclass
class Wolf:
    def __init__ (self,name,color):
        self.name = name
        self.color = color
        
    def bark1(self):
        print("Grr...")
        
class Dog(Wolf):
     def bark(self):
         print("Woof!")
         
husky = Dog("Max","grey")
husky.bark()
print(husky.name)
print(husky.color)
#Dog.name
#Dog.color
husky = Wolf("Max","Grey")
print(husky.name)
print(husky.color)
print(husky.bark1())

husky.name


##indirect inheritance
class A:
    def a(self):
        print(1)
        
class B(A):
    def b(self):
        print(2)
        
class C(B):
    def c(self):
        print(3)
        
c = C()
c.a()        
c.c()
c.b()

##inheritance with super function
class A:
    def spam(self):
        print(1)
        
class B(A):
    def spam(self):
        print(2)
        super().spam()
        
B().spam()


##Magic methods
class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector2D(self.x + other.x,self.y + other.y)
    
first = Vector2D(5,7)
second = Vector2D(3,9)
result = first + second
print(result.x)
print(result.y)













































































       














































































































    




































    