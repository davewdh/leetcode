class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        income = defaultdict(int)
        outcome = defaultdict(int)

        for a, b in trust:
            outcome[a] += 1
            income[b] += 1

        for i in range(1, n+1):
            if outcome[i] == 0 and income[i] == n - 1:
                return i

        return -1

