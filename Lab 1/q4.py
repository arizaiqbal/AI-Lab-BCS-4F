choice = 0

while(choice != 3):
  print("1. Add two numbers")
  print("2. Subtract two numbers")
  print("3. Exit")

  choice = int(input("\nEnter your choice :"))

  if choice == 1:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    result = num1 + num2
    print("Result:", result);
  elif choice == 2:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    result = num1 - num2
    print("Result: ", result);
  elif choice == 3:
    print("Exiting")
  else:
    print("Invalid choice. Try again")
