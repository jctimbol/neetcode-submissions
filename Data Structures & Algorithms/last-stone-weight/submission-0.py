class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = stones
        heapq.heapify_max(stones_heap)
        while(len(stones_heap)>1):
            first = heapq.heappop_max(stones_heap)
            second = heapq.heappop_max(stones_heap)
            diff = abs(first-second)
            if diff > 0:
                heapq.heappush_max(stones_heap, diff)
        if len(stones_heap) == 0:
            return 0
        else:
            return stones_heap[0]
        