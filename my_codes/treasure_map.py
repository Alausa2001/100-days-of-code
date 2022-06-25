row1 = ["🙂", "🙂", "🙂"]
row2 = ["🙂", "🙂", "🙂"]
row3 = ["🙂", "🙂", "🙂"]

print(f"{row1}\n{row2}\n{row3}")

map = [row1, row2, row3]
location = (input("Enter the location, the 1st no is the column while the second digit is the row "))
map[int(location[1]) - 1][int(location[0]) - 1] = 1


#map[1][2] = 2
#print(map)
print(f"{row1}\n{row2}\n{row3}")

