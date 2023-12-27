# Solution 1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcp = 1
count= 1
max = num1
if num2 > num1:
    max = num2

while count < max:
    if num1 % count == 0 and num2 % count == 0:
        gcp = count
    count += 1


print("Greatest common divisor of", gcp)

# Solution 2
a = int(input("Enter number 1 :"))
b = int(input("Enter number 2 :"))
while b != 0:
    r = a % b
    a = b
    b = r

print ("The greatest common divisor is:", a)