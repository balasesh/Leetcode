import math
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num, sign, stack = 0,'+',[]
        for i in s+'+':
            if i.isdigit():
                num = num*10 + int(i)
            elif i in "+-*/":
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop() * num)
                if sign == '/':
                    stack.append(stack.pop() / num)
                sign = i
                num = 0 
        return sum(stack)



s = Solution()
st = "14-3/2"
print(s.calculate(st))