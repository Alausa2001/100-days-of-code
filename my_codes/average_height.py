sum = 0
student = (input("Enter the list of student height: ")).split(", ")


for n in range(0, len(student)):
    student[n] = float(student[n])

sum = 0
for height in student:
    sum += height
length = 0
for height in student:
    length += 1
average = round(sum / length, 2)
print(f"Their average height is {average}")