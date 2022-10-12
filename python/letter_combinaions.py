def keypad_letters(digit):
    keypad = {
        2: ('a','b','c'),
        3: ('d','e','f'),
        4: ('g','h','i'),
        5: ('j','k','l'),
        6: ('m','n','o'),
        7: ('p','q','r','s'),
        8: ('t','u','v'),
        9: ('w','x','y','z')
    }
    return keypad.get(digit)

def letterCombinations(digits):
    combs = []
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return list(keypad_letters((ord(digits) - 48)))
    for d in digits:
        if(combs):
            temp = []
            keys = keypad_letters(ord(d) - 48)
            for c in combs:
                for k in keys:
                    temp.append(c+k)
            combs = temp
        else:
            combs = keypad_letters(ord(d) - 48)

    return combs

digits = "23456789"
print(letterCombinations(digits))
# ["ad","ae","af","bd","be","bf","cd","ce","cf"]