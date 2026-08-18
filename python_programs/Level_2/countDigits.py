number = int(input("Enter a Number: "))

if number == 0:
    print("Total Digits = 1")
else:
    count = 0

    while number > 0:
        number = number // 10
        count = count + 1

    print("Total Digits =", count)