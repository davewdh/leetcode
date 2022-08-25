class Solution {
    public int missingNumber(int[] nums) {
        int num = (nums.length * (nums.length + 1))/2;
        for (int i : nums) 
            num -= i;
        return num;
    }
}