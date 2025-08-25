class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        start = 1
        temp = []
        ans = []
        for i in range(len(nums)-1):
            temp.append(start)
            start += 1
            if nums[i] == nums[i+1]:
                ans.append(nums[i])
        temp.append(start)
        for i in range(len(nums)):
            if temp[i] not in nums:
                ans.append(temp[i])
                return ans
        
        
            

                
                    