class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        for v, u in prerequisites:
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
        
        return top if len(top) == numCourses else []