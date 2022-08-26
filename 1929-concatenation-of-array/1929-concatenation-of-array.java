class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] arr = new int[2 * n];
        for (int i = 0, j = 0; i < 2 * n; i++, j++) {
            arr[i] = nums[j];
            if (j == n-1)
                j = -1;
        }
        return arr;
        
    }
}