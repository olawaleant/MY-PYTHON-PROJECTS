unit = input("Is this temperature in Celsius or Fahreheit (C/F): ")
temp = float(input("Enter the temperature:  "))

if unit == "F":
    temp = round((temp -32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°C")
elif unit == "C":
     temp = round((9 * temp) / 5 + 32, 1)
     print(f"The temperature in Celsius is: {temp}°F")

else:
    print(f"{unit} is an invalid unit of measurement")









