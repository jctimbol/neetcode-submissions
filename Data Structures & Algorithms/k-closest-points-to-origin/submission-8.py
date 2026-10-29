class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use max heap, and remove if length > k
        # by the end, the entire heap will have the k closest points
        
        heap = []
        res = []
        distance_to_point = defaultdict(list)

        for x, y in points:
            neg_distance = -1 * math.sqrt((x ** 2) + (y ** 2))
            heapq.heappush(heap, (neg_distance, x, y))
        
            if len(heap) > k:
                heapq.heappop(heap)

        for _, x, y in heap:
            res.append([x, y])
        
        return res
