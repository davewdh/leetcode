class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        aSet = set()
        ans = 0
        for num in arr1:
            temp = str(num)
            for i in range(len(temp)):
                aSet.add(temp[0:i+1])

        for num2 in arr2:
            temp2 = str(num2)
            for i in range(len(temp2)):
                if temp2[0:i+1] in aSet:
                    ans = max(ans, len(temp2[0:i+1]))

        return ans