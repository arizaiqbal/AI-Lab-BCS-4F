def calculate_average (marks_list):
  total = 0
  count = 0

  for num in marks_list:
    total += num
    count += 1

  average = total/count
  return average;

marks = [70, 80, 90];
print("Marks:", marks)
print("Average Marks:", calculate_average(marks))
