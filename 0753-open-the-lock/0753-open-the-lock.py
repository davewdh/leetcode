class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        q = deque() 
        q.append(("0000", 0))
        visited = set(deadends)

        def children(lock):
            arr = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                arr.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                arr.append(lock[:i] + digit + lock[i+1:])
            return arr

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child in visited:
                    continue
                visited.add(child)
                q.append((child, turns + 1))

        return -1

