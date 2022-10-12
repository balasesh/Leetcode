
import math

def lengthOfLongestSubstring(str):
    test = ""
    # Result
    maxLength = -1
     
    # Return zero if string is empty
    if (len(str) == 0):
        return 0
    elif(len(str) == 1):
        return 1
    for c in list(str):
        if (c in test):
            test = test[test.index(c) + 1:]
        test = test + "".join(c)
        maxLength = max(len(test), maxLength)
    return maxLength

s = "bbbbb"
print(lengthOfLongestSubstring(s))
s = "pwwkew"
print(lengthOfLongestSubstring(s))
s = "abcabcbb"
print(lengthOfLongestSubstring(s))