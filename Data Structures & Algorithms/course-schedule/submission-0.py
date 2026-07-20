class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make adjacency list of length numCourses
        adj_list = {i: [] for i in range(numCourses)}

        for u, v in prerequisites:
            adj_list[u].append(v)

        visited = set()
        rec_stack = set()

        def dfs(course):
            visited.add(course)
            rec_stack.add(course)

            for neighbor in adj_list[course]:
                if neighbor in rec_stack:
                    return True
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            
            rec_stack.remove(course)
            return False

        for course in adj_list:
            if course not in visited:
                if dfs(course):
                    return False

        return True