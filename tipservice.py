message = ("Please enter bill:")
print(message)
a = input()
bill = int(a)

message = ("Please enter the service if it was: bad (0%), okay (15%), good (20%), or great (25%)")
print(message)

choice = input()

if choice == "bad":
    x = (bill * 1.0)
    print(f"Your total is ${x}")

else:
    print( )


if choice == "okay":
    y = print(bill * 1.15)
    print(f"Your total is ${y}")

else:
    print( )


if choice == "good":
    z = print(bill * 1.2)
    print(f"Your total is ${z}")

else:
    print( )


if choice == "great":
    w = print(bill * 1.25)
    print(f"Your total is ${w}")

else:
    print( )