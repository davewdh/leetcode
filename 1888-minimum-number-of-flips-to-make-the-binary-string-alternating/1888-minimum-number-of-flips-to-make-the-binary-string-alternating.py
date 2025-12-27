class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        temp = s + s
        l = 0
        count1 = 0 #0101
        count2 = 0 #1010 
        ans1 = n
        ans2 = n

        for r in range(len(temp)):
            if r % 2 == 0:
                if temp[r] == "0":
                    count2 += 1
                else:
                    count1 += 1
            else:
                if temp[r] == "0":
                    count1 += 1
                else:
                    count2 += 1

            if r - l + 1 == n:
                ans1 = min(ans1, count1)
                ans2 = min(ans2, count2)
                if l % 2 == 0:
                    if temp[l] == "1":
                        count1 -= 1
                    else:
                        count2 -= 1
                else:
                    if temp[l] == "1":
                        count2 -= 1
                    else:
                        count1 -= 1
                l += 1
        return min(ans1, ans2)

        
        