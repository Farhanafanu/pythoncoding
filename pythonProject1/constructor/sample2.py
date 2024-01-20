# class Baseclass:
#     def __init__(self):
#         print("baseclass")
#     def setname(self,name):
#
#         self.name=name
#         print("baseclass setname")
#     def displayname(self):
#         print(self.name)
#
# class Subclass(Baseclass):
#
#
#     def setname(self,name):
#         super().setname(name)
#         print("subclasssetname")
#
#
#         self.name=name
#
#         def displayname(self):
#             print(self.name)
#
#
#
# # b=Baseclass()
# # b.setname("aslufanu")
# # b.displayname()
# s=Subclass()
#
# s.setname("aslu")
# s.displayname()
# class Baseclass:
#     def setname(self,name):
#         self.name=name
#         print(self.name)
# class Subclass(Baseclass):
#     def setname(self,name):
#         self.name=name
#         print(self.name)
#         super().setname()
#
# s=Subclass()
# s.setname("aju")
class Baseclass:
    def setname(self, name):
        self.name = name
        print(self.name)

class Subclass(Baseclass):
    def setname(self, name):
        self.name = name
        print(self.name)
        super().setname(name)  # Pass the 'name' argument here

s = Subclass()
s.setname("aju")
