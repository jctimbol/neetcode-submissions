class Solution:
    def countBits(self, n: int) -> List[int]:
        oneList = []
        for i in range(0, n+1):
            curr = str(bin(i))
            currCount = 0
            for j in range(0, len(curr)):
                if curr[j] == '1':
                    currCount += 1
            oneList.append(currCount)
        
        return oneList