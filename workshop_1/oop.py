class Cat:
    def __init__(self, name, age, color, gender):
        self.name = name 
        self.age = age 
        self.color = color 
        self.gender = gender
    
    def __repr__(self):
        return f"Cat('{self.name}', '{self.age}', '{self.color}', '{self.gender}')"
    
    def __str__(self):
        return f"{self.name} {self.age}"
    
    def __len__(self):
        return self.age
    
    def __add__(self, other):
        return self.name + " " + other.name

    def meow(self):
        print("meoww...")

mindy = Cat("mindy", 12, "blue", "f")
alexa = Cat("alexa", 15, "yellow", "f")

class BankAccount:

    number_of_instances = 0

    def __init__(self, name, type):
        BankAccount.number_of_instances += 1
        self.name = name 
        self.type = type 
        self.balance = 0
        self.counter = 0
    
    @staticmethod
    def increment_instances():
        BankAccount.number_of_instances += 1
    
    @classmethod
    def increment_instances(cls):
        cls.number_of_instances += 1

    def deposit(self, amount):
        self.balance += amount
        self.counter += 1
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("you need to make some money bro")

print(BankAccount.number_of_instances)
ericsAccount = BankAccount("eric dube", "chequing")
print(BankAccount.number_of_instances)
BankAccount.increment_instances()
print(ericsAccount.balance)
ericsAccount.deposit(400)
ericsAccount.deposit(200)
print("counter:", ericsAccount.counter)
ericsAccount.withdraw(300) # 300
print(ericsAccount.balance)
ericsAccount.withdraw(500) # message
print(ericsAccount.balance)


class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary 
        self.legs = 2
    
    def get_paid(self):
        print("i just got paid")

class Developer(Employee):
    def __init__(self, name, salary, prog_language):
        super().__init__(name, salary)
        self.prog_language = prog_language
    
    def write_code():
        print("I write code")

dev = Developer("eric", 50000000000, "python")

print(dev.legs)