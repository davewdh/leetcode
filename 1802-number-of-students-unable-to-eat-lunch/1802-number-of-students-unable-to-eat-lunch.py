class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        m = {}
        for stu in students:
            if m.get(stu):
                m[stu] += 1
            else:
                m[stu] = 1
        e = 0
        for s in sandwiches:
            if m.get(s) and m.get(s) > 0:
                m[s] -= 1
                e += 1
            else:
                break
        return len(students) - e

