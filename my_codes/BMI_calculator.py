weight = input("input your weight in 'kg': ")
height = input("input your height in 'm': ")
weight_convert = float(weight)
height_convert = float(height)
BMI = float(weight_convert / (height_convert ** 2))
final_bmi = (round(BMI, 2))

print("Your BMI is : " + str(final_bmi))
