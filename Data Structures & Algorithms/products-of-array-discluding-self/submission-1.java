class Solution {
    public int[] productExceptSelf(int[] nums) {
        int product = 1;
        int[] productArr = new int[nums.length];
        for(int i = 0; i < nums.length; i++) {
            for(int j=0;j<nums.length;j++) {
                if(i!=j) {
                    product *= nums[j];
                }
            }
            productArr[i]=product;
            product=1;
        }
        return productArr;
    }
}  
