class Solution {
    public int search(int[] nums, int target) {
        if(nums.length == 0) return -1;
       if(nums.length == 1 && target == nums[0]) return 0;
       int low = 0;
        int high = nums.length - 1;
        
        for(int i = 0; i < nums.length; i++) {
            int mid = (low + high) / 2;
            System.out.println(nums[mid]);
            if(target>nums[mid]) low = mid + 1;
            else if(target<nums[mid]) high = mid - 1;
            else return mid;
        }
        return -1;
    }
}
