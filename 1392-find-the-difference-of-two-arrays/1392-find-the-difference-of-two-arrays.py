class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr1, arr2 = [], []
        for n in nums1:
            if (n not in nums2) and (n not in arr1):
                arr1.append(n)
        for n in nums2:
            if n not in nums1 and n not in arr2:
                arr2.append(n)
        return [arr1, arr2]