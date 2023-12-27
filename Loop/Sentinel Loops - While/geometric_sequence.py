
# Solution 1 using count
count = 1
value = 1

while value <= 1000:
    print(value)
    value = 3 ** count
    count+=1


# Solution 2 using 1 variable
a = 1
while a < 1000:
    print(a)
    a = a * 3