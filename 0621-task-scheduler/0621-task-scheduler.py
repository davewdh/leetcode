class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks) # return a map, eg. A : -3, B : -3
        maxHeap = [-c for c in counts.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque() # (-c, waiting time)

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    q.append((cnt, time + n))

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time



