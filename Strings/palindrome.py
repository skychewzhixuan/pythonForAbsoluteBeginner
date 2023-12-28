str = "addA"
str = str.lower()

if len(str) >= 4 and len(str) <=5:
    reversed_str = str[::-1]

    if str.__eq__(reversed_str):
        print("Palindrome")
    else:
        print("Not Palindrome")
else:
    print("String is more than 5 characters or less than 4 characters")
