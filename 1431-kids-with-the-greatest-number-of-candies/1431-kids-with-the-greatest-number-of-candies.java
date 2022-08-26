class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> aList = new ArrayList<>(candies.length);
        int max = candies[0];
        for (int i = 1; i < candies.length; i++) 
            max = Math.max(max, candies[i]);
    
        for (int i = 0; i < candies.length; i++) 
            aList.add(candies[i] + extraCandies >= max);    
        return aList;
        
    }
}