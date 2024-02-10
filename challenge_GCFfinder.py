
def GCF(m,n):
    if n == 0:
        return m
    else:
        return GCF(n, m%n)
    
m = int(input("Enter your first number:"))
n = int(input("Enter your second number:"))

print("Your GCF between the two numbers are", GCF(m,n))