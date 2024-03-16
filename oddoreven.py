# ODD OR EVEN

message = ("Enter number below:")
print(message)
x = input()
int(x)

remainder = int(x)%2
print(remainder)


if remainder == 0:
    print("even")
else:
    print("odd")