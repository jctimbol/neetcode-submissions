class Solution:
    def hammingWeight(self, n: int) -> int:
        oneCount = 0
        num = str(bin(n))
        for i in range(0, len(num)):
            if num[i] == '1':
                oneCount += 1

        return oneCount