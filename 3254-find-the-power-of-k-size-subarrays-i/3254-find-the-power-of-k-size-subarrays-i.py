class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l = 0
        ans = []
        count = 1

        for r in range(len(nums)):
            if r > 0 and nums[r] == nums[r-1] + 1:
                count += 1

            if  r - l + 1 > k:
                if nums[l] + 1 == nums[l+1]:
                    count -= 1
                l += 1
            
            if (r - l + 1) == k:
                if count == k:
                    ans.append(nums[r])
                else:
                    ans.append(-1)
        
        return ans