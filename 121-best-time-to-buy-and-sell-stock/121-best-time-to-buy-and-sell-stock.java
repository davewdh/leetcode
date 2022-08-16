class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int minPrice = prices[0];
        for (int i = 0; i < prices.length; i++) {
            max = Math.max(max, prices[i] - minPrice);
            minPrice = Math.min(minPrice, prices[i]);
        }
        return max;
        
    }
}