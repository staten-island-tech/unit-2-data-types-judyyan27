message = "Enter a number:"
print(message)

number1 = int(input())

message = "Enter another number:"
print(message)
number2 = int(input())

factors_1 = []
factors_2 = []

for i in range (1,number1+1):
    if number1%i == 0:
        factors_1.append(i)

for i in range (2,number2+1):
    if number2%i == 0:
        factors_2.append(i)

else:
    print(f"Factors of {number1}: {factors_1[-1]}")
    print(f"Factors of {number2}: {factors_2[-1]}")    

