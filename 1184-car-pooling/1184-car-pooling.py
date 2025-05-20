class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        minHeap = [] # [end, numPassengers]
        count = 0
        # loop the sorted trips
        for t in trips:
            numPassengers, start, end = t
            # check if the prev end <= cur_start, count -= prev_numPassengers
            while minHeap and minHeap[0][0] <= start:
                count -= minHeap[0][1]
                heapq.heappop(minHeap)
            count += numPassengers
            if count > capacity:
                return False

            # push t to minHeap
            heapq.heappush(minHeap, [end, numPassengers])
        return True