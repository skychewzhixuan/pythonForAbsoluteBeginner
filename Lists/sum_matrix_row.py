m = [[10,20,30],
 [40,50,60]]

sum=0

for row in range(len(m)):
    for col in range(len(m[row])):
        sum+=m[row][col]

    print("Sum of row", row+1, "is", sum)
    sum=0
