class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        ans = [0] * n
        l, r = 0, n - 1

        for i in range(n):
            if nums[i] < pivot:
                ans[l] = nums[i]
                l += 1

        for j in range(n-1, -1, -1):
            if nums[j] > pivot:
                ans[r] = nums[j]
                r -= 1

        while l <= r:
            ans[l] = pivot
            l += 1
        
        return ans