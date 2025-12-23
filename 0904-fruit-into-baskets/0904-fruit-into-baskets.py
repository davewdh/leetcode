class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        ans = 0
        aMap = {}

        for r in range(len(fruits)):
            if aMap.get(fruits[r]):
                aMap[fruits[r]] += 1
            else:
                aMap[fruits[r]] = 1
            
            while len(aMap) > 2:
                aMap[fruits[l]] -= 1
                if aMap[fruits[l]] == 0:
                    aMap.pop(fruits[l])
                l += 1
            ans = max(ans, r-l+1)

                
        return ans