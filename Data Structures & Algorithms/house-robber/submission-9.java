class Solution {
    public int rob(int[] nums) {
        int max = 0;
        int twoBack = 0;
        int oneBack = 0;
        for(int i = 0; i < nums.length; i++) {
            max = Math.max(twoBack + nums[i], oneBack);
            twoBack = oneBack;
            oneBack = max;
        }
        return oneBack;
    }
}
