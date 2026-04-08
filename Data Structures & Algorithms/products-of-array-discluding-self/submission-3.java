class Solution {
    public int[] productExceptSelf(int[] nums) {
        int product = 1;
        int zeroCount = 0;
        int[] productArr = new int[nums.length];
       
        for(int i = 0; i < nums.length; i++) {
           if(nums[i] == 0) zeroCount++;
           else product *= nums[i];
        }
        if(zeroCount > 1) return productArr;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] != 0 && zeroCount > 0) productArr[i] = 0;
            else if(nums[i] == 0) productArr[i] = product;
            else productArr[i] = product / nums[i];
        }
        return productArr;
    }
}  
