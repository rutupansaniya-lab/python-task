import random

# function to calculate BMI with file logging
def calculate_bmi(weight, height):  
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        s="You are underweight."
    elif 18.5 <= bmi < 24.9:
        s="You have a normal weight."             
    elif 25 <= bmi < 29.9:
        s="You are overweight."
    else:
        s="You are obese."
    # log the BMI calculation to a file 
    with open("bmi_log.txt", "a") as file:
        file.write(f"Weight: {weight}, Height: {height}, BMI: {bmi}, {s} \n")
    return bmi, s

    # function to user to input weight and height and validate them
def get_user_input():
    weight = input("Please enter your weight in number: ")
    # Validate weight input
    while(True):
        try:
            weight = float(weight)
            break
        except ValueError:
            weight = input("Invalid input. Please enter a numeric weight value: ") 

    weight_unit = input("Is this in kg, g, lb, or oz ").strip().lower()  
    # validate weight unit
    while True:
        if weight_unit in ['kg', 'g', 'lb', 'oz']:
            break
        else:
            weight_unit = input("Invalid unit. Please enter kg, g, lb, or oz: ").strip().lower()

    # for converting weight 
         
    conversion_factors = {
        'kg': 1,
        'g': 1000,
        'lb': 2.20462,
        'oz': 35.274 }

    # Convert from the original unit to kilograms
    weight_in_kg = weight / conversion_factors[weight_unit]


    height = input("Please enter your height : ").strip()
    # Validate height input
    while(True):
        try:
            height=float(height)
            break
        except ValueError:
            height = input("Invalid input. Please enter a numeric height value: ").strip()
        
    # enter height unit
    while True:
        height_unit = input("Is this in m, cm, ft, or in ").strip().lower()
        if height_unit in ['m', 'cm', 'ft', 'in']:
            break
        else:
            height_unit = input("Invalid unit. Please enter m, cm, ft, or in: ").strip().lower()

    # Convert height to meters if needed
    height_conversion_factors = {
        'm': 1,
        'cm': 100,
        'ft': 3.28084,
        'in': 39.3701
    }
    height_in_meters = height / height_conversion_factors[height_unit]

    return weight_in_kg, height_in_meters

# main function to run the BMI calculator

def main():  
    print("Welcome to the BMI Calculator!")
    weight, height = get_user_input()
    bmi, s = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}, {s}")
# run the main function
if __name__ == "__main__":
    #call the main function
    main()  
