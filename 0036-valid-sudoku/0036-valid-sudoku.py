class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            nums_r = []
            nums_c = []
            for j in range(len(board[i])):
                n_r = board[i][j]
                n_c = board[j][i]
                if n_r != ".":
                    nums_r.append(n_r)
                if n_c != ".":
                    nums_c.append(n_c)
            if len(set(nums_r)) != len(nums_r):
                return False
            if len(set(nums_c)) != len(nums_c):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                nums = []
                for q in range(i, i+3):
                    for w in range(j, j+3):
                        n = board[q][w]
                        if n != ".":
                            nums.append(n)
                if len(set(nums)) != len(nums):
                    return False
        return True
        
        

            