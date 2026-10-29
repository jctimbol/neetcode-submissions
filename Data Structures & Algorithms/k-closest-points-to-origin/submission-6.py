class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # k closest points from points arr to origin
        # distance = sqrt(x_i^2 + y_i^2)

        heap = []
        res = []
        distance_to_point = defaultdict(list)

        for x, y in points:
            distance = math.sqrt((x ** 2) + (y ** 2))
            heapq.heappush(heap, distance)
            distance_to_point[distance].append([x, y])
        
        for i in range(k):
            curr_distance = heapq.heappop(heap)
            res.append(distance_to_point[curr_distance].pop())
                
        return res

        
