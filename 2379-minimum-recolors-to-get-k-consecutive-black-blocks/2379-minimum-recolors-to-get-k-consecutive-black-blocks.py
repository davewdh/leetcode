class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        count_w = 0
        for r in range(k):
            if blocks[r] == "W":
                count_w += 1
        ans = count_w
        
        for r in range(k, len(blocks)):
            if blocks[r] == "W":
                count_w += 1
            if blocks[l] == "W":
                count_w -= 1
            ans = min(ans, count_w)
            l += 1

        return ans
            
            