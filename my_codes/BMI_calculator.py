from ast import If


weight = input("input your weight in 'kg': ")
height = input("input your height in 'm': ")
weight_convert = float(weight)
height_convert = float(height)
BMI = float(weight_convert / (height_convert ** 2))
BMI = (round(BMI, 2))
if BMI < 18.5:
    print(f"Hi user, your BMI is {BMI} and you're underweight")
elif BMI < 25:
    print(f"Hi user, your BMI is {BMI} and you have a normal weight")
elif BMI < 30:
    print(f"Hi user, your BMI is {BMI} and you're overweight\nTry registering in a gym ):")
elif BMI < 35:
    print(f"Hi user, your BMI is {BMI} and you're obese\nWatch the kind of food you eat, try registering in a gym and see your doctor")
else:
    print(f"Hi user, your BMI is {BMI} and you're clinically obese\nSee your doctor.")
