class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        m = {0: 0}
        for j in range(len(wall)):
            count = 0
            for i in range(len(wall[j])):
                if i == len(wall[j])-1:
                    break
                count += wall[j][i]
                if m.get(count):
                    m[count] += 1
                else:
                    m[count] = 1
        return len(wall) - max(m.values())