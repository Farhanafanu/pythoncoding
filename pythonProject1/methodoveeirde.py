# class Baseclass:
#     def __init__(self):
#         print("baseclass")
# class Subclass(Baseclass):
#
#     def __init__(self):
#         Baseclass.__init__(self)
#         super().__init__()
#         print("subclass")
#
# # b=Baseclass()
# s=Subclass()
class Animal:
    def sound(self):
        print("sound")
class Dog(Animal):
    def sound(self):
        print("woof")

d=Dog()
d.sound()