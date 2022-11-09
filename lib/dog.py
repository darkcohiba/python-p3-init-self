#!/usr/bin/env python3

# class Dog:
#     def __init__(self, name, breed, color, owner):
#         self.name = name
#         self.breed = breed
#         self.color = color
#         self.owner = owner

#     def bark(self):
#         print("Woof!")
    
#     def showing_self(self):
#         print(f"the dog breed is {self.breed}, color is {self.color}, and name is {self.name}. The owner is {self.owner}.")

#     def adopt(dog, owner_name):
#         dog.owner = owner_name
    

# leo = Dog("Leo", "German Shorthair Pointer", "Brown", "Me")
# leo.bark()
# leo.showing_self()
# leo.adopt("You")
# leo.showing_self()


class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed