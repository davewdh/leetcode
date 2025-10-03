class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 0
        total = 0
        for arrive, time in customers:
            if t > arrive:
                total += (t - arrive)
            else:
                t = arrive
            total += time
            t += time
        return total / len(customers)