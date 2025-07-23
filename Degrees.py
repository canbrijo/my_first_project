#changing degree to kelvin
def celsius_to_kelvin(celsius):
    kelvin = celsius+273.15
    return kelvin

celsius = float(input("Enter tempereature in celsius:"))
kelvin = celsius_to_kelvin(celsius)
print(f"{celsius}degrees is equal to {kelvin}k")