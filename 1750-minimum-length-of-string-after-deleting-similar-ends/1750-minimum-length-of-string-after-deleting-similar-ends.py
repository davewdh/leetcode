class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        ans = n
        l, r = 0, n - 1
        while l < r:
            if s[l] == s[r]:
                temp = s[l]
                countl = 0
                while l < r:
                    if s[l] == temp:
                        countl += 1
                        l += 1
                    else:
                        break
                countr = 0
                while l < r:
                    if s[r] == temp:
                        countr += 1
                        r -= 1
                    else:
                        break
                ans = ans - countl - countr
                if l == r and s[l] == temp:
                    ans -= 1
                print(ans)
            else:
                return ans
        return ans