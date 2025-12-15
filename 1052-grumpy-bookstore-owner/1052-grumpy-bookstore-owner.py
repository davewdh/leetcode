class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        sat = 0
        not_sat = 0
        max_not_sat = 0
        l, r = 0, 0
        while r < len(customers):
            if grumpy[r] == 0:
                sat += customers[r]
            else:
                not_sat += customers[r]
            if r - l + 1 > minutes:
                if grumpy[l] == 1:
                    not_sat -= customers[l] 
                l += 1
            max_not_sat = max(max_not_sat, not_sat)
            r += 1
            
        return sat + max_not_sat

        