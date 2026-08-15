# principal amount (when the final amount, rate, time are given to find PA)
amount = float(input("Enter the final amount : "))
rate = float(input("Enter the Rate (%) : ")) 
time = float(input("Enter the time(years) : "))

principal = amount /((1 + rate / 100 ) ** time )
print("principal amount = " , principal)

#simple interest
principal = float(input("Enter the principal amount : "))
rate = float(input("Enter the reat of interest "))
time =  float(input("Enter the time (in years) : "))

simple_interest = (principal * rate * time) / 100
print("Simple Interest = ", simple_interest)

#compound interest 
principal = float(input("Enter the principal amount : "))
rate = float(input("Enter the rate (%) : "))
time = float(input("Enter the time (in years) : "))

amount = principal * ((1 + rate / 100) ** time)
compound_interest = amount - principal

print("Final amount :", amount)
print("compound interest :", compound_interest)
    