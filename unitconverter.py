def get_conversion_type():
    while True:
        print("\nSelect the type of conversion:")
        print("1. Temperature")
        print("2. Distance")
        print("3. Mass")
        print("4. Speed")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice in ["1", "2", "3", "4"]:
            return choice
        elif choice == "5":
            return None
        
        print("Invalid choice. Please try again.")


def get_measurement_unit(conversion_type):
    units = {
        "1": {
            "1": "°C",
            "2": "°F"
        },
        "2": {
            "1": "mm",
            "2": "cm",
            "3": "m",
            "4": "km",
            "5": "inch",
            "6": "feet",
            "7": "yard",
            "8": "mile"
        },
        "3": {
            "1": "mg",
            "2": "g",
            "3": "kg",
            "4": "t",
            "5": "ounce",
            "6": "pounds"
        },
        "4": {
            "1": "m/s",
            "2": "km/h",
            "3": "yards/s",
            "4": "miles/h",
            "5": "knots"
        }
    }
    
    choices = units[conversion_type]
    
    while True:
        print(f"\nSelect the {conversion_type.lower()} unit:")
        for i, unit in enumerate(choices.values(), start=1):
            print(f"{i}. {unit}")
        print(f"{len(choices) + 1}. Return")
        
        choice = input(f"Enter your choice (1-{len(choices) + 1}): ")
        
        if choice in choices:
            return choices[choice]
        elif choice == str(len(choices) + 1):
            return None
        
        print("Invalid choice. Please try again.")

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def convert_distance(distance, from_unit, to_unit):
    conversion_factors = {
        "mm": {"mm": 1, "cm": 0.1, "m": 0.001, "km": 0.000001,
               "inch": 0.0393701, "feet": 0.00328084, "yard": 0.00109361, "mile": 0.000000621371},
        "cm": {"mm": 10, "cm": 1, "m": 0.01, "km": 0.00001,
               "inch": 0.393701, "feet": 0.0328084, "yard": 0.0109361, "mile": 0.00000621371},
        "m": {"mm": 1000, "cm": 100, "m": 1, "km": 0.001,
              "inch": 39.3701, "feet": 3.28084, "yard": 1.09361, "mile": 0.000621371},
        "km": {"mm": 1000000, "cm": 100000, "m": 1000, "km": 1,
               "inch": 39370.1, "feet": 3280.84, "yard": 1093.61, "mile": 0.621371},
        "inch": {"mm": 25.4, "cm": 2.54, "m": 0.0254, "km": 0.0000254,
                 "inch": 1, "feet": 0.0833333, "yard": 0.0277778, "mile": 0.0000157828},
        "feet": {"mm": 304.8, "cm": 30.48, "m": 0.3048, "km": 0.0003048,
                 "inch": 12, "feet": 1, "yard": 0.333333, "mile": 0.000189394},
        "yard": {"mm": 914.4, "cm": 91.44, "m": 0.9144, "km": 0.0009144,
                 "inch": 36, "feet": 3, "yard": 1, "mile": 0.000568182},
        "mile": {"mm": 1609340, "cm": 160934, "m": 1609.34, "km": 1.60934,
                 "inch": 63360, "feet": 5280, "yard": 1760, "mile": 1}
    }
    
    return distance * conversion_factors[from_unit][to_unit]

def convert_mass(mass, from_unit, to_unit):
    conversion_factors = {
        "mg": {"mg": 1, "g": 0.001, "kg": 0.000001, "t": 0.000000001, "ounce": 0.000035274, "pounds": 0.00000220462},
        "g": {"mg": 1000, "g": 1, "kg": 0.001, "t": 0.000001, "ounce": 0.035274, "pounds": 0.00220462},
        "kg": {"mg": 1000000, "g": 1000, "kg": 1, "t": 0.001, "ounce": 35.274, "pounds": 2.20462},
        "t": {"mg": 1000000000, "g": 1000000, "kg": 1000, "t": 1, "ounce": 35274, "pounds": 2204.62},
        "ounce": {"mg": 28349.5, "g": 28.3495, "kg": 0.0283495, "t": 0.0000283495, "ounce": 1, "pounds": 0.0625},
        "pounds": {"mg": 453592, "g": 453.592, "kg": 0.453592, "t": 0.000453592, "ounce": 16, "pounds": 1}
    }
    
    return mass * conversion_factors[from_unit][to_unit]

def convert_speed(speed, from_unit, to_unit):
    conversion_factors = {
        "m/s": {"m/s": 1, "km/h": 3.6, "yards/s": 1.0936133, "miles/h": 2.2369363, "knots": 1.9438445},
        "km/h": {"m/s": 0.2777778, "km/h": 1, "yards/s": 0.9113444, "miles/h": 0.6213712, "knots": 0.5399568},
        "yards/s": {"m/s": 0.9144, "km/h": 1.09728, "yards/s": 1, "miles/h": 0.6818182, "knots": 0.5924838},
        "miles/h": {"m/s": 0.44704, "km/h": 1.609344, "yards/s": 1.4666667, "miles/h": 1, "knots": 0.8689762},
        "knots": {"m/s": 0.5144444, "km/h": 1.852, "yards/s": 1.6878099, "miles/h": 1.1507794, "knots": 1}
    }
    
    return speed * conversion_factors[from_unit][to_unit]

def main():
    print("Welcome to the Unit Converter!")

    while True:
        conversion_type = get_conversion_type()

        if conversion_type is None:
            print("Exiting the program...!")
            break

        from_unit = get_measurement_unit(conversion_type)

        if from_unit is None:
            continue

        to_unit = get_measurement_unit(conversion_type)

        if to_unit is None:
            continue

        value = get_float_input("Enter the value to convert: ")

        if conversion_type == "1":
            if from_unit == "°C" and to_unit == "°F":
                result = celsius_to_fahrenheit(value)
                print(f"{value}°C = {result}°F")
            elif from_unit == "°F" and to_unit == "°C":
                result = fahrenheit_to_celsius(value)
                print(f"{value}°F = {result}°C")

        elif conversion_type == "2":
            result = convert_distance(value, from_unit, to_unit)
            print(f"{value}{from_unit} = {result}{to_unit}")

        elif conversion_type == "3":
            result = convert_mass(value, from_unit, to_unit)
            print(f"{value}{from_unit} = {result}{to_unit}")

        elif conversion_type == "4":
            result = convert_speed(value, from_unit, to_unit)
            print(f"{value}{from_unit} = {result}{to_unit}")

if __name__ == "__main__":
    main()
