class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] products = new int[nums.length];
        for(int i = 0; i < nums.length; i++) {
            int ptr1 = i-1;
            int ptr2 = i+1;
            int product = 1;
            while(ptr1 >= 0 && ptr2 <= nums.length - 1) {
                product *= nums[ptr1] * nums[ptr2];
                ptr1--;
                ptr2++;
            }
            while(ptr1 >= 0) {
                product *= nums[ptr1];
                ptr1--;
            }
            while(ptr2 <= nums.length - 1) {
                product *= nums[ptr2];
                ptr2++;
            }
            products[i] = product;
        }
        return products;
    }
}  
