from connection import connect, createtable, selectfromtable, inserttrainee, updatetrainee, deletetrainee


connect('localhost', 'postgres', 'ahmed123', 'iti')



# updatetrainee(1, "Nabil", 1330, 7)
# inserttrainee(7, "Mahmoud", 22, 12)
deletetrainee(1)
print(selectfromtable("trainee"))

#_____________________________________________________________________

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def drink(self, sentence):
        print(f"{self.name} is drinking {sentence}")
    
    def eat(self,sentence):
        print(f"{self.name} is eating {sentence}.")
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am a {self.gender}.")

class Employee(Human):    
    def __init__(self, name, age, gender, employee_id, position, salary, company_name):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
        self.company_name = company_name
    
    def work(self):
        print(f"{self.name} is working as a {self.position}.")
    
    def introduce(self):
        print(f"I work as a {self.position} at {self.company_name}. My employee ID is {self.employee_id}.")

person = Human(name="Ahmed", age=30, gender="male")
person.introduce()
person.drink("tea")
person.eat("Meat")

employee = Employee(name="Ahmed", age=25, gender="male", employee_id="123", position="Software Engineer", salary=80000, company_name="Google")
employee.introduce()
employee.work()
