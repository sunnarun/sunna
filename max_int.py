number = 0
max_number = 0

while number >= 0:
    number = int(input("Input a number: "))
    if max_number < number:
        max_number += number
else:
    print("The maximum is", max_int)