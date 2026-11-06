class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        for u, v in prerequisites:
            adj_list[u].append(v)
            in_degree[v] += 1
        
        top = []
        # bfs
        q = deque([u for u in range(numCourses) if in_degree[u] == 0])
        while q:
            curr = q.popleft()
            top.append(curr)
            for v in adj_list[curr]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        
        return len(top) == numCourses