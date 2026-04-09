class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        int[] ans = new int[2];

        for(int i = 0; i < nums.length; i++) {
            int comp = target - nums[i];
            if(map.containsKey(comp) && map.get(comp) != i) {
                ans[0] = map.get(comp);
                ans[1] = i;
                break;
            }
            
        }
        Arrays.sort(ans);
        return ans;
    }
}
