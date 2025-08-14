class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        aMap = {}
        for num in nums:
            if aMap.get(num):
                aMap[num] += 1
            else:
                aMap[num] = 1
        
        for v in aMap.values():
            if v % 2 != 0:
                return False
        return True
