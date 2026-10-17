class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        frequencies = {}

        for num in hand:
            if num not in frequencies:
                frequencies[num] = 1
            else:
                frequencies[num] += 1
            
        for num in sorted(frequencies.keys()):
            if frequencies[num] == 0:
                continue
            while frequencies[num] > 0:
                curr = num
                for i in range(groupSize):
                    if curr not in frequencies or frequencies[curr] == 0:
                        return False
                    frequencies[curr] -= 1
                    curr += 1
        
        return True
