def get_positive_float(prompt):
    while True:
        try:
            value =float(input(prompt))
            if value <= 0:
                print("Please enter a positive number greater than zero.")
            else:
                return value
        except Exception as e:
            print("Invalid input! Please enter a valid number." , e)
print()
print("=============== BMI CALCULATOR ===============")
print()

weight = get_positive_float("Enter your weight ⚖️  in kilograms :")
height= get_positive_float("Enter your height 📏 in meters    : ")

bmi = weight / (height ** 2)
bmi = round(bmi , 2)

if bmi <= 18.5:
    category = "Underweight ❌ "
    print()
    print("Tip:🍲 Consider consulting a doctor or nutritionist.")
elif bmi <= 25:
    category = "Normal weight ✅ "
    print()
    print("Great!💪 You are in a healthy range.")
elif bmi <= 30:
    category = "Overweight ⚠️ "
    print()
    print("Tip:🥗 A balanced diet and regular exercise can help.")
else:
    category = "Obese 🚨 "
    print()
    print("Tip:🩺 Please consider speaking with a healthcare professional.")

print()
print("------------------- RESULTS ------------------")
print(f"Your BMI is : {bmi}.")
print(f"Your are classified as : {category}.")
print("----------------------------------------------")


            