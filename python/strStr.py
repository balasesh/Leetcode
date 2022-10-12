def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    return -1

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))
haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))