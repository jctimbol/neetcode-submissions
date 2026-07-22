class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(numCourses)}

        for u, v in prerequisites:
            adj_list[u].append(v)

        visited = set()
        rec_stack = set()
        valid = []

        def has_cycle(course):
            visited.add(course)
            rec_stack.add(course)

            for next_course in adj_list[course]:
                if next_course in rec_stack:
                    return True
                if next_course not in visited:
                    if has_cycle(next_course):
                        return True
            
            valid.append(course)
            rec_stack.remove(course)
            return False

        for i in range(numCourses):
            if i not in visited:
                if has_cycle(i):
                    return []
        
        return valid