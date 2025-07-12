# temperature convert
#-------------------------------------------------------
def convert_temperature(temp, from_unit, to_unit):
    if from_unit == to_unit:
        return temp
    elif from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (temp * 9/5) + 32
        elif to_unit == 'Kelvin':
            return temp + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (temp - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (temp - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return temp - 273.15
        elif to_unit == 'Fahrenheit':
            return (temp - 273.15) * 9/5 + 32
    return None

def main():
    print("Temperature Converter")
    print("Supported units: Celsius, Fahrenheit, Kelvin\n")

    try:
        temp = float(input("Enter the temperature value: "))
    except ValueError:
        print(" Error: Please enter a valid numeric temperature.")
        return

    from_unit = input("Convert from (Celsius/Fahrenheit/Kelvin): ").capitalize()
    to_unit = input("Convert to (Celsius/Fahrenheit/Kelvin): ").capitalize()

    valid_units = ['Celsius', 'Fahrenheit', 'Kelvin']
    if from_unit not in valid_units or to_unit not in valid_units:
        print(" Error: Invalid unit. Use 'Celsius', 'Fahrenheit', or 'Kelvin'.")
        return

    result = convert_temperature(temp, from_unit, to_unit)
    if result is not None:
        print(f"\n {temp} {from_unit} is equal to {result:.2f} {to_unit}")
    else:
        print(" Error in conversion.")

if __name__ == "__main__":
    main()

