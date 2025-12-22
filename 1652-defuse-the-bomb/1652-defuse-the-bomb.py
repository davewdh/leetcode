class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        code1 = code + code[:k+1]
        code2 = code[len(code) - abs(k):] + code
        l1 = 0
        l2 = 0
        ans = []
        total1 = 0
        total2 = 0

        if k > 0:
            for r in range(len(code1)):
                total1 += code1[r]
                if r >= k:
                    total1 -= code1[l1]
                    ans.append(total1)
                    l1 += 1
                    if len(ans) == len(code):
                        return ans
        
        elif k < 0:
            for r in range(len(code2)):
                total2 += code2[r]
                if r >= abs(k) - 1:
                    ans.append(total2)
                    total2 -= code2[l2]
                    l2 += 1
                    if len(ans) == len(code):
                        return ans
        else:
            return [0] * len(code)


   

