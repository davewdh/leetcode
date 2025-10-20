class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        m = {}
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            remain = count % k
            if (remain == 0):
                if i+1 >= 2:
                    return True
                else:
                    if m.get(remain):
                        continue
                    else:
                        m[remain] = i
            else:
                if remain in m:
                    if i - m[remain] > 1:
                        return True
                else:
                    m[remain] = i
        return False