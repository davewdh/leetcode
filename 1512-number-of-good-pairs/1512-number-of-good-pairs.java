class Solution {
    public int numIdenticalPairs(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i]))
                map.put(nums[i], map.get(nums[i])+1);
            else 
                map.put(nums[i], 1);
        }
        int count = 0;
        for (int num : map.values()) {
            count += (num * (num - 1))/2;
        }
        return count;
    }
}