class Solution:
    def isPathCrossing(self, path: str) -> bool:
        start = (0, 0)
        cur = (0, 0)
        crosses = set()
        for p in path:
            crosses.add(cur)
            if p == "N":
                cur = (cur[0], cur[1]+1)
            elif p == "E":
                cur = (cur[0]-1, cur[1])
            elif p == "S":
                cur = (cur[0], cur[1]-1)
            else:
                cur = (cur[0]+1, cur[1])
            if cur in crosses:
                return True
            
        return False

