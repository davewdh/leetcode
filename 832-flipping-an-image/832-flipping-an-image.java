class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        for (int i = 0; i < image.length; i++) {
            
            for (int j = 0, k = image[0].length - 1; j < image[0].length/2; j++, k--) {
                int temp = 1 - image[i][j];
                image[i][j] = 1 - image[i][k];
                image[i][k] = temp;
            }
            if (image[0].length % 2 != 0)
                    image[i][image[0].length/2] = 1 - image[i][image[0].length/2];
        }
        
        return image;
    }
}