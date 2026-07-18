import random

marks = []
low_marks = []
medium_marks = []
high_marks = []

for i in range(20):
    mark = random.randint(0, 100)
    marks.append(mark)

    if mark <= 30:
        low_marks.append(mark)
    elif mark <= 69:
        medium_marks.append(mark)
    else:
        high_marks.append(mark)
    
print("All marks: ")
print(marks)

print("Marks <= 30: ")
print(low_marks)

print("Marks between 31 and 69: ")
print(meduim_marks)

print("Marks > 69: ")
print(high_marks)