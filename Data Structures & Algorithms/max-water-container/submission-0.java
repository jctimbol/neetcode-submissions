class Solution {
    public int maxArea(int[] heights) {
        int highest = 0;
        for(int i = 0; i < heights.length; i++) {
            for(int j = i; j < heights.length; j++) {
                int curr = Math.min(heights[i], heights[j]) * (j-i);
                if(curr > highest) highest = curr;
            }
        }
        return highest;
    }
}
