class Solution {
    public int rob(int[] nums) {
        int rob1 = 0;
        int rob2 = 0;
       for(int i = 0; i < nums.length; i++) {
            int max = Math.max(nums[i] + rob1, rob2);
            rob1 = rob2;
            rob2 = max;
       }

       return rob2;
    }
}
