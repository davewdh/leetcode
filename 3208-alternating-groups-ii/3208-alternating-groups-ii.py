class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        temp = colors + colors
        l = 0
        r = 1
        ans = 0
        while r < (len(colors) + k - 1):
            if temp[r] == temp[r-1]:
                l = r
            if r - l + 1 >= k:
                ans += 1
            r += 1
        return ans


