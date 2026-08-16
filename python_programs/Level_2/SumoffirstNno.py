n = int(input("Enter a number: "))

sum = 0
for i in range( 1 ,n + 1):
    sum = sum + i
    print("sum = ", sum)

n = int(input("Enter a number: "))

sum = n * (n + 1) // 2

print("Sum =", sum)