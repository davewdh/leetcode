class Solution {
    public int minimumSum(int num) {
        String s = String.valueOf(num);
        int[] nums = new int[4];
        for (int i= 0; i < 4; i++) 
            nums[i] = s.charAt(i) - '0';
        Arrays.sort(nums);
        return ((nums[0] * 10 + nums[2]) + (nums[1] * 10 + nums[3]));        
    }
}