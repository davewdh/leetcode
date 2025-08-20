class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        m = {}
        for p in paths:
            m[p[0]] = p[1]
            if p[1] not in m:
                m[p[1]] = ""
        for k, v in m.items():
            if v == "":
                return k                
                
