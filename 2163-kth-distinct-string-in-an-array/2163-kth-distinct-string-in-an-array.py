class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        map = {}
        for s in arr:
            if s in map:
                map[s] += 1
            else:
                map[s] = 1
        for s in arr:
            if map[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""