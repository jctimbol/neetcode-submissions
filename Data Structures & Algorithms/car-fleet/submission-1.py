class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        
        # start w/ car closest to target
        stack = []
        for p, s in sorted(cars)[::-1]:
            ETA = (target - p) / s
            stack.append(ETA)

            # earlier car has same/earlier ETA -> collision
            # if collision, has same ETA as later car
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)