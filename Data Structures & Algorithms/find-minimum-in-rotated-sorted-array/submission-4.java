class Solution {
    public int findMin(int[] nums) {
       if(nums.length == 1) return nums[0];
        if(nums.length == 2) return Math.min(nums[0], nums[1]);
        int min = 0;
        int low = 0, high = nums.length - 1;

        while(low < high) {
            int mid = (low + high) / 2;
            if(nums[mid] > nums[high]) {
                int newLow = (low + high) / 2;
                if(newLow == low) low = newLow + 1;
                else low = newLow;
            }
            else {
                int newHigh = (low + high) / 2;
                if(newHigh == high) high = newHigh - 1;
                else high = newHigh;
            }
        }
        
        return Math.min(nums[low], nums[high]);
    }

}
