class Solution {
    public int rob(int[] nums) {
        int oneBack = 0;
        int twoBack = 0;
        int current = 0;

        for(int i = 0; i < nums.length; i++) {
            current = Math.max(nums[i] + twoBack, oneBack);
            twoBack = oneBack;
            oneBack = current;
        }
        return oneBack;
    }
}
