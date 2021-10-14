# -*- coding: utf-8 -*-
"""
Created on Sat May  1 19:48:01 2021

@author: 212709023
"""
##CLASS AND OBJECT

# class parrot:
#     #class attribute
#     species='bird'
#     #instance attribute
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def sing(self,song):
#         print('{} is singing {}'.format(self.name,song))
    
# #new instance
# obj1=parrot('bob',2)

# print('Parrot {} of age {}'.format(obj1.name,obj1.age))

# obj1.sing('Zoop')

##################################################################################################################
#Inheritance:

# class parent():
#     attr='P'
#     def __init__(self):
#         print('Calling parent')
#     def printcall(self):
#         print('Parent printing')

# class child(parent):
#     attr='C'
#     def __init__(self):
#         super().__init__()
#         print('Calling Child')
#     def printcall(self):
        
#         print('Child printing')
#         parent.printcall(self)
#         print(parent.attr)
        

# p=parent()
# p.printcall()

# c=child()
# c.printcall()


##################################################################################################################
#Encapsulation

# class Car():
#     def __init__(self):
#         self.__carName='Creta'
#     def printCar(self):
#         return self.__carName
#     def upgrade(self,name):
#         self.__carName=name
        
# c=Car()
# print(c.printCar())
# c.__carName='New'
# print(c.printCar())
# c.upgrade('Tucson')
# print(c.printCar())

##################################################################################################################
#Polymorphism

class Parrot():
    def __init__(self,name):
        self.name=name
    def fly(self):
        print('{} can fly'.format(self.name))
    def swim(self):
        print('{} cannot swim'.format(self.name))


class Penguin():
    def __init__(self,name):
        self.name=name
    def fly(self):
        print('{} cannot fly'.format(self.name))
    def swim(self):
        print('{} can swim'.format(self.name))

def polyFunc(bird):
    poly_var=bird.name
    print(poly_var)
    bird.fly()
    bird.swim()
    
p1=Parrot('Tom')
p2=Parrot('Ping')

polyFunc(p1)
polyFunc(p2)