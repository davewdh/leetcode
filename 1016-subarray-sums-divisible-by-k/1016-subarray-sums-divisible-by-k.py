class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        m[0] = 1
        sum = 0
        ans = 0

        for n in nums:
            sum += n
            remain = sum % k

            ans += m[remain]
            m[remain] += 1
        return ans
