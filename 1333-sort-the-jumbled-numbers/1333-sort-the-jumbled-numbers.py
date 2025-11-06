class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        ans = []
        for i, n in enumerate(nums):
            temp = ""
            for digit in str(n):
                temp += str(mapping[int(digit)])
            ans.append((int(temp), i))

        ans.sort()

        temp = []
        for n1, index in ans:
            temp.append(nums[index])
        return temp
