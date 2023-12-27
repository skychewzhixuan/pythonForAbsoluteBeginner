
sum=0
count=0
value=1

while value !=0:
    value = int(input("Enter value, 0 to quit: "))
    if value != 0:
        count+=1
        sum+=value
if count != 0:
    avg = sum/count
    print("The average is", avg)


