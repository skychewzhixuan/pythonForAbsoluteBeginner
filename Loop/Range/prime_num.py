value = int(input("Enter a value: "))

countFactor = 0
for i in range(1, value+1):
    if value % i == 0:
        countFactor += 1

if countFactor == 2:
    print(value, "is a prime number")
else:
    print(value, "is not a prime number")