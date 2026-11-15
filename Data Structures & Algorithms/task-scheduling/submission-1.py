class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # priority: frequency
        # heap: (frequency, task)
        # you don't need to track the task name

        frequencies = Counter(tasks)
        q = deque()

        heap = [-f for f in frequencies.values()]
        heapq.heapify(heap)
        res = 0

        while heap or q:
            if heap:
                curr = heapq.heappop(heap)
                if curr+1 < 0:
                    q.append((curr+1, res+n))

            if q and q[0][1] == res:
                heapq.heappush(heap, q.popleft()[0])
            
            res += 1
        
        return res

