class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = {}
        for i in range(numCourses):
            map[i] = []

        for course, prere in prerequisites:
            map[course].append(prere)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if map[course] == []:
                return True

            visited.add(course)
            for pre in map[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
