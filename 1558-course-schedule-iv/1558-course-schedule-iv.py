class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = []
        map1 = defaultdict(list)

        for prere, course in prerequisites:
            map1[course].append(prere)

        def dfs(course):
            if not course in map2:
                map2[course] = set()
                for prere in map1[course]:
                    map2[course] |= dfs(prere)
                map2[course].add(course)
            return map2[course]

        map2 = {} # key: course, value: hashset
        for course in range(numCourses):
            dfs(course)

        for u, v in queries:
            ans.append(u in map2[v])
        return ans
