student = {}

for i in range (3):
  name = input("Enter student name: ")
  marks = int (input("Enter marks: "))
  student[name] = marks;

print("\nStudent Records:")
for name, marks in student.items():
  print(name ,":", marks);
