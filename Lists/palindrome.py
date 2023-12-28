#list = ['ab','cd','ef','cd','ab']
list = ['a','c','e','d','a']


if list[0] == list[-1] and list[1] == list[-2]:
    print(list," is a palindrome")
else:
    print(list," is not a palindrome")