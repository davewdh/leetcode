class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for n in nums1:
            greatNum = n
            startIndex = nums2.index(n)
            for n1 in nums2[startIndex:]:
                if n1 > greatNum:
                    ans.append(n1)
                    greatNum = n1
                    break
                else:
                    continue
            if n == greatNum:
                ans.append(-1)
        return ans
                    
