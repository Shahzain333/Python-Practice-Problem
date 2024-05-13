# Program to cheack if a number is even or odd
try:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f'Given number {num} is even')
    else:
        print(f'Given number {num} is odd')
except ValueError:
    print("Invalid input! Please enter a valid integer.")
    