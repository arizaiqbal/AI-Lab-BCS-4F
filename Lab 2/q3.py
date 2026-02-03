class Student:
  def __init__(self, name):
    self.name = name

  def set_marks(self,marks):
    self.__marks = marks
    
  def get_marks(self):
    return self.__marks

  def calculate_grade(self):
      if self.__marks >= 85:
          return "A"
      elif self.__marks >= 70:
          return "B"
      elif self.__marks >= 50:
          return "C"
      else:
          return "F"


s1 = Student("Mariam")
s2 = Student("Armeen")

s1.set_marks(88)
s2.set_marks(63)

print("Name:",s1.name)
print("Marks:",s1.get_marks())
print("Grade:", s1.calculate_grade())
print("Name:",s2.name)
print("Marks:",s2.get_marks())
print("Grade:", s2.calculate_grade())
