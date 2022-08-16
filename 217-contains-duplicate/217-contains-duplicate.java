class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> aSet = new HashSet<>();
        for (int num : nums) {
            if (!aSet.add(num))
                return true;
        }
        return false;
    }
}