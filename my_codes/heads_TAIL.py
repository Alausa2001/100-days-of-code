import random
seeding = int(input("Enter a seed: "))
random.seed(seeding)
rand = random.randint(0, 1)
if rand < 1:
    print("Heads")
else:
    print("Tails")