weight = input("Enter weight in kg : ")
height = input("Enter height in mtr : ")

bmi = int(weight) / float(height) ** 2

if bmi < 18.5:
    print(f"Your BMI is : {bmi} and you are underweight")
elif bmi < 25:
    print(f"Your BMI is : {bmi} and you are normal weight")
elif bmi < 30:
    print(f"Your BMI is : {bmi} and you are overweight")
elif bmi < 35:
    print(f"Your BMI is : {bmi} and you are obese")
else:
    print(f"Your BMI is : {bmi} and you are kudrat ke bharosee")