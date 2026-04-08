class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> myset = new HashSet<Integer>();
        for(int num : nums) {
            if(myset.contains(num)) return true;
            else myset.add(num);
        }
        return false;
    }
}