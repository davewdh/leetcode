class Solution:
    def minSwaps(self, s: str) -> int:
        l = list(s)
        count1, count2 = 0, 0
        ans = 0
        r = len(l)-1
        for i in range(len(l)):
            if l[i] == "[":
                count1 += 1
            else:
                count2 += 1
                if count2 > count1:
                    while l[r] != "]":
                        r -= 1
                    l[i], l[r] = l[r], l[i]
                    count1 += 1
                    count2 -= 1
                    ans += 1
        return ans
            


