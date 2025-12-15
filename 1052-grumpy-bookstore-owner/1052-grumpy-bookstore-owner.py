class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        sat = 0
        not_sat = 0
        for i in range(minutes):
            if grumpy[i] == 0:
                sat += customers[i]
            else:
                not_sat += customers[i]
        max_not_sat = not_sat
        l = 0
        r = minutes
        while r < len(customers):
            if grumpy[r] == 0:
                sat += customers[r]
            else:
                not_sat += customers[r]
            if grumpy[l] == 1:
                not_sat -= customers[l] 
            max_not_sat = max(max_not_sat, not_sat)
            r += 1
            l += 1

        return sat + max_not_sat

        