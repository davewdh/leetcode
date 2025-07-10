class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = []
        for i in range(len(edges)+1): # 0,1,2..n
            parent.append(i)

        def find(node): # find the root of parent node and return
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        #check if n.parent == v.parent, return false(redundant),         
        # v.parent = u.parent, return true   
        def union(u, v): 
            uParent = find(u)
            vParent = find(v)
            if uParent == vParent:
                return False
            parent[vParent] = uParent
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []
