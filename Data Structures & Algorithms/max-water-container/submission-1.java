class Solution {
    public int maxArea(int[] heights) {
        int highest = 0;
        /*for(int i = 0; i < heights.length; i++) {
            for(int j = i; j < heights.length; j++) {
                int curr = Math.min(heights[i], heights[j]) * (j-i);
                if(curr > highest) highest = curr;
            }
        }*/

        int ptr1 = 0;
        int ptr2 = heights.length - 1;
        while(ptr1 != ptr2) {
            int curr = Math.min(heights[ptr1], heights[ptr2]) * (ptr2 - ptr1);
            if(curr > highest) highest = curr;
            if(heights[ptr1] < heights[ptr2]) ptr1++;
            else ptr2--;
        }

        return highest;
    }
}
