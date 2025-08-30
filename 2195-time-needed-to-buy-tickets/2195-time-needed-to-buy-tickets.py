class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        cur = 0
        while tickets[k] > 0:
            if cur == k:
                ans += 1
                tickets[k] -= 1
            else:
                if tickets[cur] > 0:
                    ans += 1
                    tickets[cur] -= 1
            cur += 1
            if cur >= len(tickets):
                cur = cur % len(tickets)
            
        return ans
