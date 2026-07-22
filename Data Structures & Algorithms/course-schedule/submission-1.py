class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        visited = set()
        rec_stack = set()

        for u, v in prerequisites:
            adj_list[u].append(v)
        
        def dfs(course):
            visited.add(course)
            rec_stack.add(course)

            # go through each in list
            for next_course in adj_list[course]:
                if next_course in rec_stack:
                    return True
                if next_course not in visited:
                    if dfs(next_course):
                        return True
            
            # no cycle detected
            rec_stack.remove(course)
            return False
        
        for course in adj_list:
            if course not in visited:
                if dfs(course):
                    return False

        return True