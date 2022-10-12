from re import L


def roman_to_number(argument):
    switcher = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if argument in switcher:
        return switcher.get(argument)
    else:
        return -1

def romanToInt(s):
    num_int = 0
    s = s[::-1]
    prev = ''
    num_roman = ''
    for i in range(len(s)) :
        if i == 0 :
            num_int += roman_to_number(s[i])
        else:
            num_roman = s[i]
            prev = s[i-1]
            if(roman_to_number(prev) > roman_to_number(num_roman)):
                num_int -= roman_to_number(num_roman)
            else:
                num_int += roman_to_number(num_roman)
    return num_int

print('Original: 3, Answer:' + str(romanToInt('III')))
print('Original: 4, Answer:' + str(romanToInt('IV')))
print('Original: 5, Answer:' + str(romanToInt('V')))
print('Original: 6, Answer:' + str(romanToInt('VI')))
print('Original: 9, Answer:' + str(romanToInt('IX')))
print('Original: 10, Answer:' + str(romanToInt('X')))
print('Original: 14, Answer:' + str(romanToInt('XIV')))
print('Original: 1994, Answer:' + str(romanToInt('MCMXCIV')))