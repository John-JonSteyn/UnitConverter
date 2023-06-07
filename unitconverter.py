def get_conversion_type():
    while True:
        print("\nSelect the type of conversion:")
        print("1. Temperature")
        print("2. Distance")
        print("3. Mass")
        print("4. Speed")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice in ["1", "2", "3", "4"]:
            return choice
        
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
        
        choice = input(f"Enter your choice (1-{len(choices)}): ")
        
        if choice in choices:
            return choices[choice]
        
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
    conversion_factor = conversion_factors[from_unit][to_unit]
    return distance * conversion_factor

def convert_mass(mass, from_unit, to_unit):
    conversion_factors = {
        "mg": {"mg": 1, "g": 0.001, "kg": 0.000001, "t": 0.000000001,
               "ounce": 0.000035274, "pounds": 0.00000220462},
        "g": {"mg": 1000, "g": 1, "kg": 0.001, "t": 0.000001,
              "ounce": 0.035274, "pounds": 0.00220462},
        "kg": {"mg": 1000000, "g": 1000, "kg": 1, "t": 0.001,
               "ounce": 35.274, "pounds": 2.20462},
        "t": {"mg": 1000000000, "g": 1000000, "kg": 1000, "t": 1,
              "ounce": 35274, "pounds": 2204.62},
        "ounce": {"mg": 28349.5, "g": 28.3495, "kg": 0.0283495, "t": 0.0000283495,
                  "ounce": 1, "pounds": 0.0625},
        "pounds": {"mg": 453592, "g": 453.592, "kg": 0.453592, "t": 0.000453592,
                   "ounce": 16, "pounds": 1}
    }
    conversion_factor = conversion_factors[from_unit][to_unit]
    return mass * conversion_factor

def convert_speed(speed, from_unit, to_unit):
    conversion_factors = {
        "m/s": {"m/s": 1, "km/h": 3.6, "yards/s": 1.09361, "miles/h": 2.23694, "knots": 1.94384},
        "km/h": {"m/s": 0.277778, "km/h": 1, "yards/s": 0.000911344, "miles/h": 0.621371, "knots": 0.539957},
        "yards/s": {"m/s": 0.9144, "km/h": 1093.61, "yards/s": 1, "miles/h": 1.46667, "knots": 0.868976},
        "miles/h": {"m/s": 0.44704, "km/h": 1.60934, "yards/s": 0.682227, "miles/h": 1, "knots": 0.868976},
        "knots": {"m/s": 0.514444, "km/h": 1.852, "yards/s": 1.15078, "miles/h": 1.15078, "knots": 1}
    }
    conversion_factor = conversion_factors[from_unit][to_unit]
    return speed * conversion_factor

def main():
    conversion_type = get_conversion_type()
    measurement_unit = get_measurement_unit(conversion_type)
    value = get_float_input(f"Enter the value in {measurement_unit}: ")

    if conversion_type == "1":  # Temperature
        if measurement_unit == "°C":
            fahrenheit = celsius_to_fahrenheit(value)
            print(f"{value}°C is equal to {fahrenheit}°F")
        else:
            celsius = fahrenheit_to_celsius(value)
            print(f"{value}°F is equal to {celsius}°C")
    elif conversion_type == "2":  # Distance
        units = ["mm", "cm", "m", "km", "inch", "feet", "yard", "mile"]
        for unit in units:
            converted_distance = convert_distance(value, measurement_unit, unit)
            print(f"{value} {measurement_unit} is equal to {converted_distance} {unit}")
    elif conversion_type == "3":  # Mass
        units = ["mg", "g", "kg", "t", "ounce", "pounds"]
        for unit in units:
            converted_mass = convert_mass(value, measurement_unit, unit)
            print(f"{value} {measurement_unit} is equal to {converted_mass} {unit}")
    elif conversion_type == "4":  # Speed
        units = ["m/s", "km/h", "yards/s", "miles/h", "knots"]
        for unit in units:
            converted_speed = convert_speed(value, measurement_unit, unit)
            print(f"{value} {measurement_unit} is equal to {converted_speed} {unit}")

main()
