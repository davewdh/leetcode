class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        temp = colors + colors
        l = 0
        r = 1
        ans = 0
        while r < (len(colors) + k - 1):
            if temp[r] == temp[r-1]:
                temp1 = r - 1 - l + 1
                if temp1 >= k:
                    ans += temp1 - k + 1
                l = r
            r += 1

        if r - 1 - l + 1 >= k:
            ans += r - 1 - l + 1 - k + 1
        return ans


