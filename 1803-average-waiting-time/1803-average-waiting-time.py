class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        count_time = customers[0][0]
        total = 0
        for i in range(len(customers)):
            wait_time = count_time - customers[i][0]
            if wait_time > 0:
                total += wait_time
            else:
                count_time += abs(wait_time)
            total += customers[i][1]
            count_time += customers[i][1]
            print(count_time, total)
        return total / len(customers)