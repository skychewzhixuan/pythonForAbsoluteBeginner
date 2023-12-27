numberOfValue = int(input("Enter the number of value: "))

sum=0


for i in range(numberOfValue):
    inputNumber = int(input("Enter the number: "))
    sum+=inputNumber

if numberOfValue > 0:
    avg = sum / numberOfValue
    print("The average", avg)
else:
    print("Wrong input")
