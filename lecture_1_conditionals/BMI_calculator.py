# bmi_calculator.py

def calculate_bmi(weight, height):
#Calculate BMI using the formula: BMI = weight (kg) / height (m)^2
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
#Return BMI category based on value
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
#main function
def main():
    print("BMI Calculator")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
        
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print(f"\nYour BMI is {bmi}. You are categorized as: {category}")

#Executing main
if __name__ == "__main__":
    main()
