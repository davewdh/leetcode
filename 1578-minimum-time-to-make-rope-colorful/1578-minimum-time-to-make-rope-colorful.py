class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l, r = 0 , 0
        ans = 0
        while l < len(colors):
            temp = neededTime[l]
            count = 1
            total = 0
            while r < len(colors) and colors[l] == colors[r]:
                temp = max(temp, neededTime[r])
                count += 1
                total += neededTime[r]
                r += 1

            if count > 1:
                ans += (total - temp)
            l = r

        return ans