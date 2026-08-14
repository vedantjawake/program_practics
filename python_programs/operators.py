a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("\n========== Arithmetic Operators ==========")
print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Division (/):", a / b)
print("Floor Division (//):", a // b)
print("Modulus (%):", a % b)
print("Exponent (**):", a ** b)

print("\n========== Comparison Operators ==========")
print("Equal (==):", a == b)
print("Not Equal (!=):", a != b)
print("Greater Than (>):", a > b)
print("Less Than (<):", a < b)
print("Greater Than or Equal (>=):", a >= b)
print("Less Than or Equal (<=):", a <= b)

print("\n========== Assignment Operators ==========")
x = a
print("Initial Value of x:", x)

x += b
print("x += b :", x)

x -= b
print("x -= b :", x)

x *= b
print("x *= b :", x)

x /= b
print("x /= b :", x)

x = a
x //= b
print("x //= b :", x)

x = a
x %= b
print("x %= b :", x)

x = a
x **= 2
print("x **= 2 :", x)

print("\n========== Logical Operators ==========")
print("(a > 5 and b > 5):", a > 5 and b > 5)
print("(a > 5 or b > 5):", a > 5 or b > 5)
print("not(a > b):", not(a > b))

print("\n========== Membership Operators ==========")
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("20 in numbers:", 20 in numbers)
print("100 in numbers:", 100 in numbers)
print("20 not in numbers:", 20 not in numbers)
print("100 not in numbers:", 100 not in numbers)

print("\n========== Identity Operators ==========")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 is list2 :", list1 is list2)
print("list1 is list3 :", list1 is list3)
print("list1 is not list2 :", list1 is not list2)

print("\n========== Bitwise Operators ==========")
print("Bitwise AND (&):", a & b)
print("Bitwise OR (|):", a | b)
print("Bitwise XOR (^):", a ^ b)
print("Bitwise NOT (~a):", ~a)
print("Left Shift (a << 1):", a << 1)
print("Right Shift (a >> 1):", a >> 1)

print("\n========== Program Completed ==========")