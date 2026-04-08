class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length==0) return 0;
        if(nums.length==1) return 1;
        int sequenceLength = 0;
        Set<Integer> set = new HashSet<Integer>();
        for(int num : nums) {
            set.add(num);
        }
        int currLength = 0;
        for(int num : set) {
            int toCompare = num;
            while(set.contains(toCompare)) {
                currLength++;
                toCompare++;
            }
            sequenceLength = Math.max(currLength, sequenceLength);
            currLength = 0;
        }
        return sequenceLength;
    }
}
