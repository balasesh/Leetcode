# Python3 program to find sum of
# two large numbers.

# Function for finding sum of
# larger numbers
def findSum(str1, str2):

    if (len(str1) > len(str2)):
        temp_s = str1
        str1 = str2
        str2 = temp_s

    carry = 0
    strsum = []
    str1 = str1[::-1]
    str2 = str2[::-1]

    for i in range(len(str1)):
        sum = int(str1[i]) + int(str2[i]) + carry
        strsum += chr((sum % 10) + 48)
        carry = int(sum / 10)
    
    for i in range(len(str1),len(str2)):
        sum = int(str2[i]) + carry
        strsum += chr((sum % 10) + 48)
        carry = int(sum / 10)

    if (carry > 0):
        strsum += chr(carry + 48)

    return ("").join(strsum[::-1])


# Driver code
str1 = "6876132464621321"
str2 = "6549843213264646"
print(findSum(str1, str2))
str1 = "2654654654686"
str2 = "465465465425"
print(findSum(str1, str2))
