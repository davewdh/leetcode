class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] output = new int[2];
        HashMap<Integer, Integer> aMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            if (aMap.containsKey(target - nums[i])) {
                output[1] = i;
                output[0] = aMap.get(target - nums[i]);
                return output;
            }
            aMap.put(nums[i], i); 
        }
        return output;
    }
}