# Given a list of numbers, find the max and min values.

try:
    lst = []
    number_of_int = int(input("How many number to you want to inert in the list: "))
    
    for i in range(number_of_int):
        num = int(input("Enter an integer: "))
        lst.append(num)
        
    max_value = lst[0]
    min_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
        elif num < min_value:
                min_value = num

    print(f'\nMax value is {max_value}\nMin value is {min_value}')
    
except ValueError:
    print("Invalid input! please enter an integer.")
    

   