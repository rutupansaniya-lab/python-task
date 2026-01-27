import math
def convert_weight(weight, from_unit, to_unit): 

    # Conversion factors
    conversion_factors = {
        'kg': 1,
        'g': 1000,
        'lb': 2.20462,
        'oz': 35.274

    }

    # Convert from the original unit to kilograms
    weight_in_kg = weight / conversion_factors[from_unit]

    # Convert from kilograms to the target unit
    converted_weight = weight_in_kg * conversion_factors[to_unit]

    return converted_weight


if __name__ == "__main__":

    # while loop for another conversion
    while(True): 
        weight = input("Enter weight value: ")

        # Input validation for weight
        while(True):
            try:
                float(weight)
                break
            except ValueError:
                weight = input("Invalid input. Please enter a numeric weight value: ") 
        
        # Input validation for units
        while(True):
            # convert user input to lower case for validation
            from_unit = input("Enter the unit of the weight (kg, g, lb, oz): ").lower()
            if from_unit in ['kg', 'g', 'lb', 'oz']:
                break
            else:
                print("Invalid unit. Please enter one of the following units: kg, g, lb, oz.").lower() 

        # Input validation for target unit
        while(True):
            to_unit = input("Enter the unit to convert to (kg, g, lb, oz): ").lower()
            if to_unit in ['kg', 'g', 'lb', 'oz']:
                break
            else:
                to_unit = input("Invalid unit. Please enter one of the following units: kg, g, lb, oz.").lower()
       
        converted_weight = convert_weight(float(weight), from_unit, to_unit)
        print(f"{weight} {from_unit} is equal to {converted_weight} {to_unit}.")

        # Ask if the user wants to perform another conversion
        another = input("Do you want to convert another weight? (yes/no): ")
        # Break the loop if the user does not want another conversion
        if another.lower() != 'yes':
            break