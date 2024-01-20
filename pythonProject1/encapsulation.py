class Student:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self.__age = age  # Private attribute

    def display_info(self):
        print(f"Name: {self._name}, Age: {self.__age}")

    def update_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
            print("Age updated successfully")
        else:
            print("Invalid age")


# Creating an instance of Student
student = Student("Alice", 20)

print(student._name)  # Accessing protected attribute (not recommended)
# student.__age = 21  # This won't modify the actual private attribute
student.display_info()

student.update_age(22)
student.display_info()
