class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        temp = []
        ans = []

        while l <= r:
            if abs(nums[l]) <= abs(nums[r]):
                temp.append(nums[r] * nums[r])
                r -= 1
            else:
                temp.append(nums[l] * nums[l])
                l += 1
        
        for i in range(len(temp)-1, -1, -1):
            ans.append(temp[i])
        return ans