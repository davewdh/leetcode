class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        s = 0
        for o in operations:
            if o == '+':
                s += st[-1] + st[-2]
                st.append(st[-1] + st[-2])
            elif o == 'D':
                s += 2 * st[-1]
                st.append(2 * st[-1])
            elif o == 'C':
                s -= st[-1]
                st.pop()
            else:
                st.append(int(o))
                s += int(o)

        return s