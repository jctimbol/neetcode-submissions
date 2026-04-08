class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean containsDup = false;

        ArrayList<Integer> arrayMap = new ArrayList<>();

        for(int num : nums)
        {
            if(arrayMap.contains(num))
            {
                containsDup = true;
            }
            else
            {
                arrayMap.add(num);
            }
        }


        return containsDup;
    }
}
