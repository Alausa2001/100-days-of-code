#THIS PROGRAMMME CALCULATE THE NO OF DAYS, WEEKS AND MONTH LEFT FOR THE USER IF THEY WERE TO LIVE FOR 90YEARS
no_of_days90 = 365 * 90
no_of_months90 = 12 * 90
no_of_weeks90 = 52 * 90
age_of_user = input(" Enter your age in years\n")
age_of_userconvert = int(age_of_user)
no_of_daysuser = 365 * age_of_userconvert
noofweeksuser = 52 * age_of_userconvert
noofmonthuser = 12 * age_of_userconvert
print(f"You have {no_of_days90 - no_of_daysuser} days,  {no_of_weeks90 - noofweeksuser} weeks and {no_of_months90 - noofmonthuser} months left.\nSpend it wisely.")
