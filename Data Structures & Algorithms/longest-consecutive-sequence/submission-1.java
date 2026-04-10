class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        Arrays.sort(nums);
        for(int num : nums) set.add(num);
        int max = 0;
        for(int i = 0; i < nums.length; i++) {
            if(!set.contains(nums[i] - 1)) { //if set doesnt contain prev number, then the sequence can only start here
                int curr = 1;
                for(int j = i + 1; j < nums.length; j++) {
                    if(nums[j] == nums[j-1]+1) curr++;
                    else if(nums[j] == nums[j-1]) continue;
                    else if(nums[j] > nums[j-1]+1) break;
                }
                max = Math.max(curr, max);
            } else {
                continue;
            }
        }
        return max;
        
    }
}
