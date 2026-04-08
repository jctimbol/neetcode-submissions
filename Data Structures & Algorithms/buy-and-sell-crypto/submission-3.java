class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int currProfit = 0;
        int l = 0;
        int r = 1;
        while(r<prices.length) {
            if(prices[l]>prices[r]) {
                l = r;
            }
            else {
                currProfit = prices[r] - prices[l];
                max = Math.max(currProfit, max);
            }
            r++;
        }   
        return max;

    }
}
