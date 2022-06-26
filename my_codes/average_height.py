sum = 0
student = (input("Enter the list of student height: ")).split(", ")


for n in range(0, len(student)):
    student[n] = float(student[n])

for p in range(0, n+1):
    sum += student[p]
average = round(sum / (n+1), 2)
print(f"Their average height is {average}")