class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        ans = 0
        while l <= r:
            if leftMax < rightMax:
                leftMax = max(leftMax, height[l])
                ans += (leftMax - height[l])
                l += 1
            else:
                rightMax = max(rightMax, height[r])
                ans += (rightMax - height[r])
                r -= 1
        return ans