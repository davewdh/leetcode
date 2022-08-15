class Solution {
    public int singleNumber(int[] nums) {
        int num = nums[0];
        if (nums.length <= 1)
            return num;
        Map<Integer,Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i]))
                map.remove(nums[i]);
            else
                map.put(nums[i], 1);
        }
        return (int) map.keySet().toArray()[0];
    }
}