#u = [1,2,3,4,5,6,7,8,9,10,11,12,21,11,10,9,8,7,6,5,4,3,2,1]
u = [1,2,3,5,3,2,1]
end = len(u)
mid = end // 2
print(end, mid)
isPalindrome = True;
for index in range(len(u)):
    if index < mid:
        if u[index] != u[end-1-index]:
           print(u,"is not a palindrome")
           isPalindrome=False
           break
if isPalindrome:
    print(u, "is a palindrome")