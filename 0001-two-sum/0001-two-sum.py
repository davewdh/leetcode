class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            differ = target - num
            if differ in dic:
                return [dic[differ], i]
            dic[num] = i
        return []