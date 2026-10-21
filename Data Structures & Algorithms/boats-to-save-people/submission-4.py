class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # minimum number of boats to save all people, given one-boat limit
        # if person2 >= limit or person1+person2 >= limit -> two separate boats
        
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            boats += 1
            r -= 1
        
        return boats

