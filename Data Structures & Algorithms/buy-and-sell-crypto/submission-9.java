class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int max = 0;
        while(r < prices.length) {
            if(prices[l] < prices[r]) { //if profit -> check theres higher sell
                max = Math.max(max, prices[r] - prices[l]);
            } else { //not profit -> move buy ptr to lower val
                l = r;
            }
            r++;
        }
        return max;
    }
}
