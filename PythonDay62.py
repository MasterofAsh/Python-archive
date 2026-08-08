# class Employee:
#     def __init__(self):
#         self.__name = "Harry"
# a = Employee()
# # print(a.__name) Cannot be accessed
# print(a._Employee__name)

class Student:
    def __init__(self):
        self._name = "harry"
    
    def _funName(self):
        return "Code with Harry"
    
class Subject(Student):
    pass

obj1 = Student()
obj2 = Subject()

print(obj1._name)
print(obj1._funName())

print(obj2._name)
print(obj2._funName())