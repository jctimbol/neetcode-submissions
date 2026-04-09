class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> triplets = new ArrayList<>();
        Arrays.sort(nums);
        for(int i = 0; i < nums.length - 1; i++) {
            int ptr1 = i+1;
            int ptr2 = nums.length - 1;
            int toSearch = -1 * nums[i];
            
            while(ptr1 < ptr2) {
                int curr = (nums[ptr1] + nums[ptr2]);
                if(curr == toSearch) {
                    ArrayList<Integer> triplet = new ArrayList<>();
                    triplet.add(nums[i]);
                    triplet.add(nums[ptr1]);
                    triplet.add(nums[ptr2]);
                    if(!triplets.contains(triplet))triplets.add(triplet);
                }
                if(toSearch < curr) ptr2--;
                else ptr1++;
            }
            
        }
        return triplets;
    }
}
