class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        arr = []
        for num, count in dic.items():
            arr.append((count, num))
        arr.sort()

        ans = []
        while k > len(ans):
            ans.append(arr.pop()[1])
        return ans
