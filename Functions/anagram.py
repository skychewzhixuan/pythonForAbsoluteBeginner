def check_anagram(str1, str2):
    num = 0

    lower_str1 = sorted(str1.lower())
    lower_str2 = sorted(str2.lower())

    if lower_str1 == lower_str2:
        num = 1
    else:
        num = -1
    # Write you code here

    return num


output = check_anagram("catS", "Actd")

if output == 1:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
