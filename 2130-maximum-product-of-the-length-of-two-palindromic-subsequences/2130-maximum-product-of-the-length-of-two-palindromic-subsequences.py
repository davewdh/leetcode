class Solution:
    def maxProduct(self, s: str) -> int:
        m = {} # mask : len(subseq)
        N = len(s)
        ans = 0

        for mask in range(1, 2**N): #1 << N
            subseq = ""
            for i in range(N):
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:
                m[mask] = len(subseq)

        for m1 in m:
            for m2 in m:
                if m1 & m2 == 0:
                    ans = max(ans, m[m1] * m[m2])
        return ans
