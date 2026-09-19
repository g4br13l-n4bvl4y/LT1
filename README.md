# Calculation of a Circular Garden's Measurements

## Description
This program's objective is to calculate a circular garden's measurements using the math library in Python. It calculates the:
* Area of the circular garden
* Circumference of the circular garden
* Square root of the circular garden's area
* The circular garden's area rounded up
* The circular garden's area rounded down

## How to Run
Using a valid Python IDE like PyCharm, make sure to:
* Download the file in the repository
* Open using the File Explorer
* And hit the play button above or hit RUN.

## Input Needed
The user should only enter the circular garden's radius in meters.

## Sample Output
Input: Please enter your garden's radius measurement (in meters): 8\

Output: 
<br>Area of the garden: 201.06 square meters\
Circumference of the garden: 50.27 square meters\
Square root of the area: 14.18\
Area rounded down: 201 square meters\
Area rounded up: 202 square meters<br>


## Computational Thinking
- **Problem Identification**
  - Get the area, circumference, square root of the area, area's floor value and ceiling value of the circular garden.
- **Problem Decomposition**
  - Ask the user for the circular garden's radius in meters.
  - Calculate the area, circumference, square root of the area, area's floor value and ceiling value of the circular garden using the math library.
  - Display the calculated values.
- **Pattern Recognition**
  - For every value needed to calculate the circular garden's values:
    - area = pi * radius^2
    - circumference = 2 * pi * r
    - square root of the area = sqrt(area)
    - area rounded down = floor(area)
    - area rounded up = ceil(area)
- **Data Representation**
  - Data is represented in real form.
- **Algorithm Development**
```commandline
Function Main
    Declare Real GardenRadius, GardenArea, GardenCircumference, AreaSqrt, AreaRoundDown, AreaRoundUp
    
    Output "Please enter your garden's radius measurement in meters: "
    Input GardenRadius
    
    Assign GardenArea = pi * pow(GardenRadius, 2)
    Assign GardenCirumference = 2 * pi * GardenRadius
    Assign AreaSqrt = sqrt(GardenArea)
    Assign AreaRoundDown = floor(GardenArea)
    Assign AreaRoundUp = ceil(GardeArea)
    
    Output "Area of the garden: ", GardenArea
    Output "Circumference of the garden: ", GardenCircumference
    Output "Square root of the area: ", AreaSqrt
    Output "Area rounded down: ", AreaRoundDown
    Output "Area rounded up: ", AreaRoundUp   
```

## Author
**Name**: Gabriel Seth B. Nabulay\
**Grade and Section**: 8 - Adelfa

