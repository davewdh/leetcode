class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curMax = 0
        for i in range(len(arr)):
            maxNum = 0
            if i != 0:
                if arr[i] != curMax:
                    arr[i] = curMax
                    continue
            for j in range(i+1, len(arr)):
                if maxNum < arr[j]:
                    maxNum = arr[j]
            arr[i] = maxNum
            curMax = maxNum
        arr[-1] = -1
        return arr