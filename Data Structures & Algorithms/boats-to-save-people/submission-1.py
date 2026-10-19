class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:
            if l == r and people[l] <= limit:
                boats += 1
            elif people[r] >= limit or people[l] + people[r] > limit:
                boats += 1
            elif people[l] + people[r] <= limit:
                boats += 1
                l += 1
            r -= 1
        return boats
