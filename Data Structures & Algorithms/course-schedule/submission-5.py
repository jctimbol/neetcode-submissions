class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for u, v in prerequisites:
            adj_list[u].append(v)
            in_degree[v] += 1
        
        q = deque()

        # enqueue courses w/o prereqs
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        topological_order = []

        while q:
            curr = q.popleft()
            topological_order.append(curr)

            for v in adj_list[curr]:
                in_degree[v] -= 1

                if in_degree[v] == 0:
                    q.append(v)

        if len(topological_order) != numCourses:
            return False # if cycle, then will never enter queue
        return True
        