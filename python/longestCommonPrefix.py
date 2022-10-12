def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    if len(strs) == 1:
        return strs[0]
    
    common_str = ''
    for i in range(1,len(strs)):
        #1 Get the common of the first 2 words
        if i == 1:
            first = strs[0]
            sec = strs[1]
            word_len = 0
            if len(first) < len(sec):
                word_len = len(first)
            else:
                word_len = len(sec)
            for j in range(word_len):
                if first[j] == sec[j]:
                    common_str += first[j]
                else:
                    break
        #2 check if the substring is part of the length f the first part of the every str
        elif i > 1:
            while len(common_str) > 0:
                if strs[i].startswith(common_str):
                    break
                else:
                    common_str = common_str[:-1]
    return common_str

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))