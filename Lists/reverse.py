v = ['a','e','i','o','u','w','h','y']
result = []
lengthOfList = len(v)
for i in range(lengthOfList, 0, -1):
    result.append(v[i-1])

print("Original List: ", v)
print("Reversed List: ", result)