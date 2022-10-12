def isValid(s):
    if len(s) % 2  != 0:
        return False

    bracket_map = []
    for b in s:
        if b in ['(','{','[']:
            bracket_map.append(b)
        elif b == ')' and len(bracket_map) > 0 and bracket_map[-1] == '(':
            bracket_map.pop()
        elif b == '}' and len(bracket_map) > 0 and bracket_map[-1] == '{':
            bracket_map.pop()
        elif b == ']' and len(bracket_map) > 0 and bracket_map[-1] == '[':
            bracket_map.pop()
        else:
            return False
    return bracket_map == []

s = "()"
print(isValid(s))
s = "(]"
print(isValid(s))
s = "()[]{}"
print(isValid(s))
s = "({([({[]})])})[]{}"
print(isValid(s))