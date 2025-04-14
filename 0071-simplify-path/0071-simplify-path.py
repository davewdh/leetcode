class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split('/') # home, ,foo
        for p in paths:
            if p == '..':
                if stack:
                    stack.pop()
            else:
                if p != '' and p != '.':
                    stack.append(p)
        
        return '/' + '/'.join(stack)


            
        