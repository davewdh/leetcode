class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int majority = nums[0];
        int max = 0;
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i]) + 1);
                if (map.get(nums[i]) > max) {
                    max = map.get(nums[i]);
                    majority = nums[i];
                    if (max > nums.length/2)
                        return majority;
                    
                }
            } 
            else
                map.put(nums[i], 1);
        }
        return majority;
    }
}