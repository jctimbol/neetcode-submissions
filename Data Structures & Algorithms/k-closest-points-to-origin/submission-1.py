class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        distances=defaultdict(list)
        # make min heap of distances
        for x, y in points:
            distance = math.sqrt((x**2)+(y**2))
            heap.append(distance)
            distances[distance].append([x, y])
        
        heapq.heapify(heap)
        print(heap)

        for i in range(k):
            popped_distance = heapq.heappop(heap)
            res.append(distances[popped_distance][0])
            distances[popped_distance].pop(0)
        return res