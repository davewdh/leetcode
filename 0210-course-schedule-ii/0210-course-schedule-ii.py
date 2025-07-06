class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        map = {}
        for course in range(numCourses):
            map[course] = []
        for course, prere in prerequisites:
            map[course].append(prere)
        visited = set()
        cycle = set()
        ans = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for prere in map[course]:
                if not dfs(prere):
                    return False
            
            cycle.remove(course)
            visited.add(course)
            ans.append(course)
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return []
        return ans