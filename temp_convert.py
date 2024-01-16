import argparse


def convert(unit: str) -> float:
    match unit:
        case 'f':
            return ()


def temp_convert():
    '''
    Temperature Converter
    ---
    This script converts temperatures between Fahrenheit and Celsius. It takes a temperature value and its unit as command-line arguments and performs the conversion accordingly.
    '''
    parser = argparse.ArgumentParser(
        description='Converts Fahrenheit to Celsius and vice versa.', 
        usage= '''
            py ./temp_convert.py 32 c (This means convert it to fahrenheit FROM celsius.)
            py ./temp_convert.py 0  f (This means convert it to celsius FROM fahrenheit.)

            If your command doesn't follow this structure, nothing happens.
        ''')

    parser.add_argument("Temparature", type=float, help='The value of temperature to convert.')
    parser.add_argument("Unit", type=str, help='The unit of temperature, the value is in.')

    arguments = parser.parse_args()

    temperature_to_convert = arguments.Temparature
    unit_to_convert_from: str = arguments.Unit

    converted_temperature: float

    match unit_to_convert_from.strip().lower():
        case 'f':
            converted_temperature = (temperature_to_convert - 32) * 5/9
            print(f"{temperature_to_convert} Fahrenheit in Celsius is {converted_temperature}")
        case 'c':
            converted_temperature = (temperature_to_convert * 9/5) + 32
            print(f"{temperature_to_convert} Celsius in Fahrenheit is {converted_temperature}")
        case _:
            print("I can't convert that.")


if __name__ == '__main__':
    temp_convert()
