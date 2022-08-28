class Solution {
    public int[] decompressRLElist(int[] nums) {
        int size = 0;
        for (int i = 0; i < nums.length; i+=2) 
            size += nums[i];
        
        int[] arr = new int[size];
        
        int count = 0;
        for (int j = 0; j < nums.length; j+=2) 
            Arrays.fill(arr, count, count += nums[j], nums[j+1]);
        
        
        return arr;
        
    }
}