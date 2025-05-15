class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        ans = []
        for x, y in points:
            distance = x**2 + y**2
            minHeap.append([distance, x, y])
        heapq.heapify(minHeap)

        while k > 0:
            dis, x, y = heapq.heappop(minHeap)
            ans.append([x, y])
            k -= 1
        
        return ans