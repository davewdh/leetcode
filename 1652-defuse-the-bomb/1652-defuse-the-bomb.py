class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        code = code + code
        ans = []
        total = 0

        if k > 0:
            l = 1
            for r in range(1, len(code)):
                total += code[r]
                if r - l + 1 == k:
                    ans.append(total)
                    total -= code[l]
                    l += 1
                    if len(ans) == n:
                        return ans
        
        elif k < 0:
            k = abs(k)
            l = n - k
            for r in range(l, len(code)):
                total += code[r]
                if r - l + 1 == k:
                    ans.append(total)
                    total -= code[l]
                    l += 1
                    if len(ans) == n:
                        return ans
        else:
            return [0] * n


   

