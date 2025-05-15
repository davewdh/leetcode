class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-s for s in stones]
        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            first = heapq.heappop(minHeap)
            second = heapq.heappop(minHeap)
            if first != second:
                heapq.heappush(minHeap, -((-first) - (-second)))

        if minHeap:
            return abs(minHeap[0])
        else:
            return 0