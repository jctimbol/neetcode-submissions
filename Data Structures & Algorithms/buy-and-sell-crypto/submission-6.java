class Solution {
    public int maxProfit(int[] prices) {
        int ptr1 = 0;
        int ptr2 = 1;
        int max = 0;
        while(ptr2 < prices.length) {
           int profit = prices[ptr2] - prices[ptr1];
           max = Math.max(profit, max);

           if(prices[ptr1] > prices[ptr2]) {
            ptr1 = ptr2;
           }
           ptr2++;
        }
        return max;
    }
}
