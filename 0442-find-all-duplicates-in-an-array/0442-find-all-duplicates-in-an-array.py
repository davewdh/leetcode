class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        aSet = set()
        ans = []
        for n in nums:
            if n in aSet:
                ans.append(n)
            aSet.add(n)
        return ans