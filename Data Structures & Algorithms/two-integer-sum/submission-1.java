class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int[] indices = new int[2];
        int remainder = 0;

        for(int i = 0 ; i < nums.length ; i++)
        {
            remainder = target - nums[i];

            for(int j = i + 1 ; j < nums.length && i < nums.length ; j++)
            {
                if(remainder == nums[j])
                {
                    indices[0] = i;
                    indices[1] = j;
                }
            
            }
        }
        return indices;
    }
}
