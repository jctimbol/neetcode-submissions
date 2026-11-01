class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        in_degree = [0] * (numCourses)
        for u, v in prerequisites:
            adj_list[u].append(v)
            in_degree[v] += 1
        
        q = deque([u for u in range(numCourses) if in_degree[u] == 0])
        res = []
        while q:
            u = q.popleft()
            res.append(u)
            for v in adj_list[u]:
                in_degree[v] -= 1

                if in_degree[v] == 0:
                    q.append(v)
        
        return True if len(res) == numCourses else False