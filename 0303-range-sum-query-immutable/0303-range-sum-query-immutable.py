class NumArray:

    def __init__(self, nums: List[int]):
        self.sumArr = []
        total = 0
        for n in nums:
            total += n
            self.sumArr.append(total)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sumArr[right]
        return self.sumArr[right] - self.sumArr[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)