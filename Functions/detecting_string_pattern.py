###
# In this coding exercise, you are asked to write the body of a function called detect_pattern that returns true or false depending upon whether two strings have the same pattern of characters. More precisely, two strings have the same pattern if they are of the same length and if two characters in the first string are equal if and only if the characters in the corresponding positions in the second string are also equal.
#
# Below are some examples of patterns that are the same and patterns that differ:
#
###

# You are allowed to create new strings,
# but otherwise you are not allowed to construct
# extra data structures to solve this problem (no list, set, dictionary, etc).

# You are allowed to create new strings,
# but otherwise you are not allowed to construct
# extra data structures to solve this problem (no list, set, dictionary, etc).

def detect_pattern(str1, str2):  # this function takes two parameters as strings to compare.
    # Keep in mind that this method should return the same value
    # no matter what order the two strings are passed

    # Insert your code here
    indx1 = 0
    indx2 = 0
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    if len(str1) != len(str2):
        return False
    else:
        for i in range(len(str1)):
            for I in range(i + 1, len(str1)):
                if str1[I] == str1[i]:
                    print(str1[i],i,I)
                    indx1 = I
                if str2[I] == str2[i]:
                    print(str2[i],i, I)
                    indx2 = I
            if indx1 != indx2:
                print(indx1, indx2)
                return False
    return True


print(detect_pattern("- - - ", "aaa"))