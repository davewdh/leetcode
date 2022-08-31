class Solution {
    public int[][] largestLocal(int[][] grid) {
        int size = grid.length;
        int[][] result = new int[size-2][size-2];
        
        for (int i = 0; i < size-2; i++) {
            for (int j = 0; j < size-2; j++) {
                int max = 0;
                for (int k = i; k < i+3; k++) {
                    for (int l = j; l < j+3; l++) {
                        if (grid[k][l] > max)
                        max = grid[k][l];
                    }
                }
                result[i][j] = max;
            }
        }
        return result;
    }
}