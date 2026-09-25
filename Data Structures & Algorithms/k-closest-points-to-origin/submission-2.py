class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # map distance -> point list 
        distances = defaultdict(list)
        heap = []
        res = []

        for x, y in points:
            distance = math.sqrt((x**2)+(y**2))
            distances[distance].append([x,y])
            heapq.heappush(heap, distance)
        
        for i in range(k):
            # pop distance, get point
            distance = heapq.heappop(heap)
            res.append(distances[distance].pop())
        print(res)
        return res