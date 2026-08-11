class Employee:
    companyName = "Samsung"
    noOfEmployees = 0
    def __init__(self, name):
        self.name = name
        self.raiseAmount = 0.02
        Employee.noOfEmployees += 1
    def showDetails(self):
        print(f"The name of the employee is {self.name} in {self.noOfEmployees} sized company {self.companyName} and the raise amount is {self.raiseAmount}")

# Employee.showDetails(emp1)

emp1 = Employee("Harry")
emp1.raiseAmount = 0.06
emp1.companyName = "US Samsung" # <- Instance Variables are chosen if present
emp1.showDetails()

Employee.companyName = "Google" # <- Class Variable Value changed, thus the value for emp2 companyName changed as well
print(Employee.companyName)

emp2 = Employee("Umar")
emp2.showDetails() # <- Class Variable value used because instance variable was not present

emp3 = Employee("Abdullah")
emp3.companyName = "Nestle"
emp3.showDetails()