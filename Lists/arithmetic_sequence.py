list1 = [5,8,11,13,17]
list1 = [2,4,6,8,10]

idx = -1
l = len(list1)

if l < 5:
    idx = 0
    print('The list has less than five elements.')
else:
    diff = list1[1] - list1[0]

    for i in range(2, l):
        if list1[i] - list1[i-1] != diff:
            idx = i
            print('The outlier value is at the index:', i)
            break

    if idx == -1:
        print('There is no outlier in the list.')