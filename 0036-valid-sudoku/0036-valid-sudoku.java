class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer, HashSet<Character>> rows = new HashMap<>();
        HashMap<Integer, HashSet<Character>> cols = new HashMap<>();
        HashMap<String, HashSet<Character>> squares = new HashMap<>();
        
        for (int r = 0; r < 9; r++){
            for (int c = 0; c < 9; c++) {
                char val = board[r][c];
                if (val == '.') {
                    continue;
                }
                String squareKey = (r / 3) + "," + (c / 3);
                rows.putIfAbsent(r, new HashSet<>());
                cols.putIfAbsent(c, new HashSet<>());
                squares.putIfAbsent(squareKey, new HashSet<>());

                if (rows.get(r).contains(val) || cols.get(c).contains(val) || squares.get(squareKey).contains(val)) {
                    return false;
                } 
                rows.get(r).add(val);
                cols.get(c).add(val);
                squares.get(squareKey).add(val);
            }
        }
        return true;
    }
}