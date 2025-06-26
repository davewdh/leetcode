class Solution {
    public int[] getConcatenation(int[] nums) {
        int len = nums.length;
        int[] newArr = new int[2 * nums.length];
        for (int i = 0; i < len; i++ ) {
            newArr[i] = newArr[i+len] = nums[i];
        }
        return newArr;
    }
}