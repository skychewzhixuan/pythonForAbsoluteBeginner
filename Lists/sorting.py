u = [5,2,7,9,1]


for i in range(len(u)):
    for j in range(0, len(u) - 1 - i):
        if u[j] > u[j+1]:
            temp = u[j+1]
            u[j+1] = u[j]
            u[j] = temp

print(u)
