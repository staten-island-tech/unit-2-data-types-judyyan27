n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

if  n1 > n2:
    x = n2
    y = n1

elif n2 > n1:
    x = n1
    y = n2

elif n2 == n1:
    x = n2
    y = n1

possible_gcf = []
list = []

def number():
    for i in range (1,x+1):
        if x%i == 0:
            possible_gcf.append(i)
number()

for i in possible_gcf:
    if y%i == 0:
        list.append(i)
        
else:
    print(f"The GCF is: {list[-1]}")