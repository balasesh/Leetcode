class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        finalSum = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i])*int(num2[j])
                finalSum[i+j] += digit
                finalSum[i+j+1] += int(finalSum[i+j] / 10)
                finalSum[i+j] = finalSum[i+j] % 10

        finalSum = finalSum[::-1]
        beg = 0
        while beg < len(finalSum) and finalSum[beg] == 0:
            beg += 1
        return "".join(list(map(str, finalSum[beg:])))


s = Solution()
print(s.multiply('123', '456'))
