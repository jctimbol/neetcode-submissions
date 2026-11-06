class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #hash map from task -> frequency
        frequencies = Counter(tasks)

        #heapify frequencies, where most frequent at top
        heap = [-frequency for frequency in frequencies.values()]
        heapq.heapify(heap) 

        q = deque([])
        time = 0

        while heap or q:
            if heap:
                curr = heapq.heappop(heap)
                if curr+1 != 0:
                    q.append((curr+1, time+n))

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
            
            time += 1
        return time