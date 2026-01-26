name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))

print("Student Name:",name)
print("Marks:",marks)

if marks >= 85:
  print("Grade: A")
elif marks >=70:
  print("Grade: B")
elif marks >=50:
  print("Grade: C")
else:
  print("Grade: Fail")
