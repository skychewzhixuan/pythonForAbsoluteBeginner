# Write a program that takes a number from the user as input. If it’s between 10 and 99 both inclusive,
# then it will display two digits. Otherwise, it will display not two digits.

number=int(input ("Enter a number: "))
if (number >=10 and number <=99):
    print("Two digit")
else:
    print("no two digit")