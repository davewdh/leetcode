class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        newArr = [False] * n 
        for i in range(n):
            if not newArr[nums[i]-1]:
                newArr[nums[i]-1] = True
        for i in range(n):
            if not newArr[i]:
                ans.append(i+1)
        return ans
        
