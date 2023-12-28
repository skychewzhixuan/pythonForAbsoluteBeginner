list = [10,20,30,40,50]


for i in range(len(list)):
    if i != len(list)-1:
        list[i] = list[i] + list[i+1]

print(list)
