class Solution:
    def maxDifference(self, s: str) -> int:
        countDic = {}
        for c in s:
            if c in countDic:
                countDic[c] += 1
            else:
                countDic[c] = 1
        
        maxOdd, minEven = 0, 100
        for c in countDic:
            if countDic[c] % 2 == 0:
                minEven = min(minEven, countDic[c])
            else:
                maxOdd = max(maxOdd, countDic[c])
        return maxOdd - minEven