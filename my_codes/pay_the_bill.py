import random
test_seed = int(input("Enter a seed: "))
random.seed(test_seed)


name_input = input("Enter the names of people at the table separated by a comma: ")
name = name_input.split(", ")

payerindex = random.randint(0, len(name) - 1)
print(f"{name[payerindex]} is going to pay the bill")
