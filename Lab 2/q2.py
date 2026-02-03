class Employee:
  def __init__ (self, name, emp_id):
    self.name = name
    self.emp_id = emp_id

  def calculate_salary(self):
   pass

class FullTimeEmployee(Employee):
  def __init__(self, name, emp_id, monthly_salary):
    self.name = name
    self.emp_id = emp_id
    self.monthly_salary = monthly_salary

  def calculate_salary(self):
    return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, hourly_rate):
        self.name = name
        self.emp_id = emp_id
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

e1 = FullTimeEmployee("Ashar", 101, 80000)
e2 = PartTimeEmployee("Rameez", 102, 150, 600)

print("Name:",e1.name)
print("Id:",e1.emp_id)
print("Salary:",e1.calculate_salary())

print("Name:",e2.name)
print("Id:",e2.emp_id)
print("Salary:",e2.calculate_salary())
