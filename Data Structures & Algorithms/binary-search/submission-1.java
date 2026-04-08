class Solution {
    public int search(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        int mid = (high + low) / 2;
        int prevMid = -1;

        while(mid != prevMid) {
        if(nums[mid] > target) {
            high = mid - 1;
            prevMid = mid;
            mid = (high + low) / 2;
            continue;
        }
        else if(nums[mid] < target) {
            low = mid + 1;
            prevMid = mid;
            mid = (high + low) / 2;
            continue;
        }
        else {
            return mid;
        }
        }
    return -1;
    }
}
