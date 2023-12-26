x = int(input("Enter X: "))
y = int(input("Enter Y: "))

if x > 0 and y > 0:
    print("The point lies in the 1st Quadrant")
else:
    if x < 0 and y > 0:
        print("The point lies in the 2nd Quadrant")
    else:
        if x < 0 and y < 0:
            print("The point lies in the 3rd Quadrant")
        else:
            if x > 0 and y < 0:
                print("The point lies in the 4th Quadrant")
