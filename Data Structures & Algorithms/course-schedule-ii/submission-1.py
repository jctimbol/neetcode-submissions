class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            adj_list[u].append(v) #u is the class, v is prereq for u (v -> u)
        
        visited = set()
        rec_stack = set()
        valid = []

        #if has cycle -> not possible, return []
        #if not cycle detected, we can add it to valid path
        def has_cycle(course):
            visited.add(course)
            rec_stack.add(course)

            for prereq in adj_list[course]:
                if prereq in rec_stack:
                    # if already visited, reached cycle
                    return True
                if prereq not in visited:
                    if has_cycle(prereq): #dfs prereq
                        return True
                
            
            valid.append(course)
            rec_stack.remove(course)
            return False
        
        for course in range(numCourses):
            if course not in visited:
                if has_cycle(course):
                    return []
        return valid