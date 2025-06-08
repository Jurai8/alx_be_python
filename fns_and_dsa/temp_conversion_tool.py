
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

    print(f"{fahrenheit}°F is {celsius}°C")

    return celsius


def convert_to_fahrenheit(celsius):
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

    print(f"{celsius}°C is {fahrenheit}°F")

    return fahrenheit



def main():
    temperature = int(input("Enter the temperature to convert: "))

    temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if temperature_type == 'F':
        convert_to_celsius(temperature)
    elif temperature_type == 'C':
        convert_to_fahrenheit(temperature)
    else:
        print("Invalid temperature type. ")
    return


if __name__ == "__main__":
    main()
