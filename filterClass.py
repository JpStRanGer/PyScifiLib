# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 10:47:51 2019

@author: jp
"""

#class stoy:
#    
#    def __init__(self,frek,amplitude):
#        import numpy as np
#        
#        self._frek = frek
#        self._amplitude = amplitude
#        self._array = list()
#        
#
#støy1 = stoy(2,3)
#
#støy1._frek

class Dog:
    
    
    # Class atribute
    species = "mammal"
    
    # initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("################## Initiating #########################")
        print("A new DOG is born, he's name is {}".format(self.name))
        print("###########################################")
        print()
        
# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
Henry = Dog("Henry", 18)
Lasso = Dog("Lasso", 3)
Fred = Dog("Fred", 7)

# Access the instance attributes
print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))

# Is Philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))
    
print()
print("###########################################")
print()
def get_biggest_number(*args):
    
    buf = 0
    name = ""
    for i in args:
        if i.age > buf:
            buf = i.age
            name = i.name
            print('{} is {} years old'.format(i.name,i.age))
    print('The oldest dog is {} years old, and he\'s name is {}'.format(buf,name))
get_biggest_number(philo, mikey,Henry,Lasso)