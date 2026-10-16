class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        frequencies = {}
        for i in range(len(hand)):
            if hand[i] in frequencies:
                frequencies[hand[i]] += 1
            else:
                frequencies[hand[i]] = 1

        for num in frequencies.keys():
            if frequencies[num] == 0:
                continue

            while frequencies[num] > 0:
                curr = num
                for j in range(groupSize):
                    if curr not in frequencies or frequencies[curr] == 0:
                        return False
                    frequencies[curr] -= 1
                    curr += 1
         
        return True

#[1, 2, 2, 3, 3, 4, 4, 5] -> 1, 2, 3, 4 and 2, 3, 4, 5

          