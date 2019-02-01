# Exercise 1

# 1. Create a Student class with the following:
# - Has the attributes:
#       fname 
#       lname
#       studentID 
#       age
# - Has the methods:
#       fullname()
#           - returns the students full name


# 2. Modify your student class from question 1 by creating a Person
# class and inheriting from it. The person class should
# have the attributes fname, lname, and age.
# the student class then inherits these attributes and adds studentID, and program
# implement __repr__ and __str__ to output a string representation of your objects
# print(str(yourStudentObject)) should display "{fname} {lname} - {studentID} - {program}"
# print(repr(yourStudentObject)) should display "Student('{fname}', '{lname}', '{age}', '{studentID}', '{program}')"


# 3. Create a Tesla class with the following:
# - Has the attributes:
#       model (i.e. "Model X"): str - vehicle model
#       color: str - color of the vehicle
#       year: int - make year of the vehicle
#       isRunning: bool - tells if the engine is running or not, should start out as false 
# - Has the methods:
#       start():
#           if isRunning is False:
#           - sets isRunning to True
#           - prints "starting engine..."
#           else:
#           - prints "engine is already running!"
#       stop():
#           if isRunning is True:
#           - sets isRunning to False
#           - prints "stopping engine..."
#           else:
#           - prints "engine is already turned off!"
#       drive():
#           if isRunning is True:
#           - prints "driving into the sunset"
#           else:
#           - prints "start engine first!"
#       __str__():
#           - return the details of the car in a string "{model}, {year}, {color}"
