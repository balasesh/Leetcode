import math
def divide(dividend, divisor):
    result = 0
    dd = abs(dividend)
    dv = abs(divisor)
    if dv == 1:
        result = dd
    elif dv == dd:
        result = 1
    else:
        temp = 0
        for i in range(31, -1, -1):
            if (temp + (dv << i) <= dd):
                temp += dv << i
                result |= 1 << i
    if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
        return min(result, math.pow(2, 31) -1)
    else:
        return -min(result,math.pow(2, 31))

dividend = 10
divisor = 3
print(divide(dividend, divisor))
dividend = 7
divisor = -3
print(divide(dividend, divisor))