name = input("Enter your name ")
partner = input("Enter your partner's name ")
name = name.lower()
partner = partner.lower()
name = name + " " + partner
truecount = str(name.count("t") + name.count("r") + name.count("u") + name.count("e"))
lovecount = str(name.count("l") + name.count("o") + name.count("v") + name.count("e"))
lovescore = int(truecount + lovecount)
if lovescore < 10 or lovescore > 90:
    print(f"Your lovescore is {lovescore}, you go together like coke and mentos.\nI bet you will love eachother just like pepper and eye do")
elif lovescore > 40 and lovescore < 50:
    print(f"Your lovescore is {lovescore}, you are perfect for eachother.\nI'm rooting for you!!\nDon't forget to invite me to your wedding too.")
else:
    print(f"Your lovescore is {lovescore}. I'm sorry, your destiny ain't clear. It is unpredictable.")
