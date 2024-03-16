#TIP SERVICE

message = ("Please enter bill:")
print(message)
a = input()

message = ("Please enter the service if it was: bad (0%), okay (15%), good (20%), or great (25%)")
print(message)

choice = input()

if choice == "bad":
    x = (int(a) * 1.0)
    print(f"Your total is ${x}")


if choice == "okay":
    y = (int(a) * 1.15)
    print(f"Your total is ${y}")


if choice == "good":
    z = (int(a) * 1.2)
    print(f"Your total is ${z}")


if choice == "great":
    w = (int(a) * 1.25)
    print(f"Your total is ${w}")

else:
    print()