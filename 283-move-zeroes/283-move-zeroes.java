class Solution {
    public void moveZeroes(int[] nums) {
        int i = 0;
        int j = 1;
        for(i=0,j=1;j<nums.length;i++,j++){
            if (nums[i] == 0 & nums[j] != 0) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
            if (nums[i] == 0 & nums[j] == 0) {
                i--;
            }
        }
    }
}