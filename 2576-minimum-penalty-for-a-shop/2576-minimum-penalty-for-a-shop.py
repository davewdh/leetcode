class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix_n, postfix_y = [0] * (n + 1), [0] * (n + 1)
        ans, count = 0, 0

        for i in range(1, n+1):
            if customers[i-1] == "N":
                count += 1
            prefix_n[i] = count

        count = 0
        for i in range(n-1, -1, -1):
            if customers[i] == "Y":
                count += 1
            postfix_y[i] = count 

        m = prefix_n[0] + postfix_y[0]
        for i in range(1, n+1):
            penalty = prefix_n[i] + postfix_y[i]
            if penalty < m:
                m = penalty
                ans = i
        return ans
