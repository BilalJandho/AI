# # try:
# #     x=int(input("Enter a number: "))
# #     y=10/x
# #     print("Rresult:",y)
# # except ValueError:
# #     print("please Enter a Valid Integer,")
# # except ZeroDivisionError:
# #     print("Cannot divide by xero")
# # except Exception as e:
# #     print("An error occured:",e)     

# # Writting to a file
# # with open ("sample.txt", "w") as file:
#     file.write("Hello, World!\n")
#     file.write("This is a sample file.\n")

# # Reading from file
# # with open("sample.txt","r") as file:
# #     contents=file.read()
# #     print("file contents:")
# #     print(contents)

# # Strong file contents in a list
# # with open ("sample.txt","r")as file:
# #     lines=file.readlines()
# #     print("file contents as list:")
# #     print(lines)


# def add(a,b):
#     return a+b

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# numbers=[1, 2, 3, 4, 5]
# double_numbers=list(map(lambda x:x*2,numbers))
# print("double numbers:",double_numbers)
# even_numbers=list(filter(lambda x:x%2==0,numbers))
# print("Even numbers",even_numbers)

# squares=[x**2 for x in numbers]
# print("squares:",squares)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# person1=Person("Alice",30)

# class Dog:
#     def __init__(self,name):
#         self.name=name

#     def bark(self):
#             return f"{self.name} says woof!"
# dog1= Dog("Buddy")
# print(dog1.bark())


# class Animal:
#      def speak(self):
#           raise NotImplementedError("Subclass must implement abstract method")
#      class Dog(Animal):
#       def speak(self):
#           return "Woof!"
#  class Animal:
#     def make_sound(self):
#         pass
#     class Dog(Animal):
#         def make_sound(self):
#             return "Meow!"
#         class DogCat(Dog,Cat):
#             pass
#         pet=DogCat()
#         print(pet.make_sound())

from abc import ABC, abstractmethod

class