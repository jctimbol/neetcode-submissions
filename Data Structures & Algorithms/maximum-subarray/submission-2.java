class Solution {
    public int maxSubArray(int[] nums) {
        if(nums.length == 1) return nums[0];
        int max = nums[0];
        int cmax = nums[0];
        for(int i = 1; i < nums.length; i++) {
            cmax = Math.max(cmax + nums[i], nums[i]);
            max = Math.max(max, cmax);
        }
        return max;
    }
}
