class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<Integer> sortedNums = new ArrayList<>();
        for(int num : nums) sortedNums.add(num);
        List<List<Integer>> triplets = new ArrayList<>();
        for(int i = 0; i < nums.length; i++) {
            int j = i + 1;
            int k = nums.length - 1;
            while(j < k) {
                int sum = sortedNums.get(j) + sortedNums.get(k);
                if(sum == -1 * sortedNums.get(i)) {
                    List<Integer> trips = new ArrayList<>();
                    trips.add(sortedNums.get(i));
                    trips.add(sortedNums.get(j));
                    trips.add(sortedNums.get(k));
                    if(!triplets.contains(trips)) triplets.add(trips);
                    //break;
                }
                if(sum > -1 * sortedNums.get(i)) k--;
                else j++;
            }
        }
        return triplets;
    }
}
