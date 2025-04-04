
class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = min(100, max(0, healthRate))  
    def sleep(self, hours):
        if hours == 7:
            self.mood = 'Happy'
        elif hours < 7:
            self.mood = 'Tired'
        else:
            self.mood = 'Lazy'

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        self.money -= items * 10  



class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = min(100, max(0, fuelRate))
        self.velocity = min(200, max(0, velocity))

    def run(self, velocity, distance):
        self.velocity = velocity
        requiredFuel = (distance / 10) * 10 

        if self.fuelRate >= requiredFuel:
            self.fuelRate -= requiredFuel
            self.stop(0)
        else:
            actual_distance = (self.fuelRate / 10) * 10
            self.fuelRate = 0
            self.stop(actual_distance)

    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance > 0:
            print(f"Stopped with {remaining_distance} km remaining.")
        else:
            print("Arrived at destination.")



class Employee(Person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.emp_id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = 'Happy'
        elif hours > 8:
            self.mood = 'Tired'
        else:
            self.mood = 'Lazy'

    def drive(self, distance, velocity):
        self.car.run(velocity, distance)

    def refuel(self, gasAmount):
        self.car.fuelRate = min(100, self.car.fuelRate + gasAmount)

    def send_mail(self, to, subject, body):
        print(f"Sending mail to {to}: {subject}\n{body}")



class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = {}

    def get_all_employees(self):
        return list(self.employees.values())

    def get_employee(self, emp_id):
        return self.employees.get(emp_id)

    def hire(self, employee):
        self.employees[employee.emp_id] = employee
        Office.employeesNum += 1

    def fire(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            Office.employeesNum -= 1

    def deduct(self, emp_id, deduction):
        employee = self.get_employee(emp_id)
        if employee:
            employee.salary -= deduction

    def reward(self, emp_id, reward):
        employee = self.get_employee(emp_id)
        if employee:
            employee.salary += reward

    def check_lateness(self, emp_id, moveHour):
        employee = self.get_employee(emp_id)
        if employee:
            is_late = Office.calculate_lateness(9, moveHour, employee.distanceToWork, employee.car.velocity)
            if is_late:
                self.deduct(emp_id, 10)
            else:
                self.reward(emp_id, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        required_time = distance / velocity
        arrival_time = moveHour + required_time
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num



car = Car(name="Fiat 128", fuelRate=100, velocity=60)
samy = Employee(name="Samy", money=1000, mood="Neutral", healthRate=80,
                emp_id=1, car=car, email="samy@iti.com", salary=5000, distanceToWork=20)
office = Office(name="ITI")
office.hire(samy)

# Samy's Morning Routine
samy.sleep(6)  
samy.eat(2)    
samy.buy(1)  

# Checking if Samy is late
office.check_lateness(samy.emp_id, 8)  

# Samy drives to work
samy.drive(20, 60)


# Showing Samy's status
print(f"Samy's mood: {samy.mood}")
print(f"Samy's health rate: {samy.healthRate}")
print(f"Samy's salary: {samy.salary}")
print(f"Samy's fuel rate: {samy.car.fuelRate}")
print(f"Samy's velocity: {samy.car.velocity}")
print(f"Number of employees: {Office.employeesNum}")
print(f"Samy's email: {samy.email}")
print(f"Samy's distance to work: {samy.distanceToWork}")
print(f"Samy's ID: {samy.emp_id}")
print(f"Office name: {office.name}")
