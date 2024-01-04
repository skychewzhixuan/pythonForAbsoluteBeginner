

def search_number(list, num):
    index = -1
    for i in range(len(list)):
        if list[i]  == num:
            index = i
    if index != -1:
        print(num,  "is found at index", index)
    else:
        print(num,"is not found in the list")


search_number([1, 2, 3, 4, 5], 3)