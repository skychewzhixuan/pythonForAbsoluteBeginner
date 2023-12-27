
num1 = int(input("Enter a number: "))

for x in range(num1):
    for y in range(num1):
        if x == 0 or x == num1-1:
            print("*", end="")
        else:
            if y == 0 or y == num1 - 1:
                print("*", end="")
            else:
                print(" ", end="")
    print()