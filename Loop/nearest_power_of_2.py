n = int(input("Enter the number: "))
pwr = 0

i = 0
pwr = 2 ** i
lastpower = 0

while(pwr < n):
    lastpower = pwr
    pwr = 2 ** i
    i+=1

# Checking difference between the num and the both powers
diff1 = n - lastpower
diff2 = pwr - n
if diff2 >= diff1:
    pwr = lastpower
print("The", pwr, "is the power of 2 nearest to", n)





