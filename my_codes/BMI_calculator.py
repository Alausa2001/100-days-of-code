from ast import If


weight = input("input your weight in 'kg': ")
height = input("input your height in 'm': ")
weight_convert = float(weight)
height_convert = float(height)
BMI = float(weight_convert / (height_convert ** 2))
BMI = (round(BMI, 2))
if BMI < 18.5:
    print("Hi user, you're underweight")
elif BMI < 25:
    print("Hi user, you have a normal weight")
elif BMI < 30:
    print("Hi user, you are overweight\nTry registering in a gym ):")
elif BMI < 35:
    print("Hi user, you are obese\nWatch the kind of food you eat, try registering in a gym and see your doctor")
elif BMI > 35:
    print("Hi user, your clinically obese\nSee your doctor.")