class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            
            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = l + 1
            elif nums[l] > nums[m]: 
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:        # 3 1 3 3 3
                l += 1

        return False
