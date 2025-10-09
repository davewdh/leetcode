class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        m = {0: 0}
        for row in wall:
            count = 0
            for i in range(len(row) - 1):
                count += row[i]
                if m.get(count):
                    m[count] += 1
                else:
                    m[count] = 1
        return len(wall) - max(m.values())