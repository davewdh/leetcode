class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # loop the array
    # whenever the next price is bigger than the current price, we get the difference
    #  And cumulate the diff to get the max profit
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += (prices[i] - prices[i-1])
        return maxProfit