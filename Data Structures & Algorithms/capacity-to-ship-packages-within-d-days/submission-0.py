class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # cant exceed max weight capacity.
        # return lowest capacity to ship within [days] days
        # ceil(sum of weights / days) -> weights to ship per day?

        # space of capacities: max(weights) -> sum(weights)
        # binary search on this search space?
        # if curr_days < days -> go lower on capacity
        # if curr_days > days -> increase capacity

        # how to find number of days required?

        # 26 weight, 4 days -> 7 required per day. if max(weights) > required, then res == max
        # if less, then we can optimize

        sum_weights = sum(weights)

        required = math.ceil(sum_weights/days)
        if max(weights) > required:
            return max(weights)

      
    
        l, r = max(weights), sum_weights
        min_capacity = r

        while l <= r:
            mid = (l+r) // 2

            curr_days = 1
            curr_ship = 0

            for weight in weights:
                if curr_ship + weight > mid:
                    curr_days += 1
                    curr_ship = 0
                curr_ship += weight

            if curr_days > days:
                l = mid + 1
            elif curr_days <= days:
                min_capacity = min(mid, min_capacity)
                r = mid - 1
        
        return min_capacity