# Name: Gabriel Seth B. Nabulay
# Grade & Section: 8 - Adelfa
# Long Test 1 - Part II

import math # Imports math library

inputted_radius = float(input("Please enter your garden's radius measurement (in meters): ")) # User inputs the garden's radius measurement

# Calculation of each values
garden_area = math.pi * (math.pow(inputted_radius, 2)) # Calculates the area of the garden using (A = pi * r^2)
garden_circumference = 2 * math.pi * inputted_radius # Calculates the circumference of the garden using (C = 2 * pi * r)
sqrt_of_area = math.sqrt(garden_area) # Calculates the square root of the garden's area
floor_of_area = math.floor(garden_area) # Calculates the value of the garden's area rounded down using math.floor
ceil_of_area = math.ceil(garden_area) # Calculates the value of the garden's area rounded up using math.ceil

# Output of each values
print("\n" + "=" * 50)
print(f"Area of the garden: {garden_area:.2f} square meters") # Outputs the value of the garden's area
print(f"Circumference of the garden: {garden_circumference:.2f} square meters") # Outputs the value of the garden's circumference
print(f"Square root of the area: {sqrt_of_area:.2f}") # Outputs the square root of the garden's area
print(f"Area rounded down: {floor_of_area} square meters") # Outputs the value of the garden's area rounded down
print(f"Area rounded up: {ceil_of_area} square meters") # Outputs the value of the garden's area rounded up
print("=" * 50)
