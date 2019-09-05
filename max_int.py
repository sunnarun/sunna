number = 1
max_int = 0

while number >= 0:
    number = int(input("Input a number: "))
    if max_int < number:
        max_int = number
else:
    print("The maximum is", max_int)