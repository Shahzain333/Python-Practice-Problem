# program to calculate the area of a rectangle
print("----------------- Area of rectangle ---------------")
try:
    length = int(input("Enter length(m): "))
    width = int(input("Enter width(m): "))

    area_of_rectangle = length * width

    print(f'\nArea of rectangle is {area_of_rectangle} m²')

except ValueError:
    print("Invalid input! please enter an integer.")