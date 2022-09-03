class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int col = image[0].length;
        for (int i = 0; i < image.length; i++) {
            
            for (int j = 0, k = col - 1; j < col/2; j++, k--) {
                int temp = 1 - image[i][j];
                image[i][j] = 1 - image[i][k];
                image[i][k] = temp;
            }
            if (col % 2 != 0)
                    image[i][col/2] = 1 - image[i][col/2];
        }
        
        return image;
    }
}