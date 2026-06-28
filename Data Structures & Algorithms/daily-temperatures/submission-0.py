class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(0, len(temperatures)):
            count = 0
            found = False
            for j in range(i, len(temperatures)):
                print(temperatures[i], temperatures[j])
                if temperatures[j] > temperatures[i]:
                    found = True
                    break
                count += 1
            
            if found:
                result.append(count)
            else:
                result.append(0)
        return result
                