class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        temp = []
        for i in range(0, len(nums), 3):
            temp = nums[i: i+3]
            if temp[2] - temp[0] > k:
                return []
            else:
                ans.append(temp)
        return ans
            