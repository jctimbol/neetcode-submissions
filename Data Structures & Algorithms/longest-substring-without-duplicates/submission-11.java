class Solution {
    public int lengthOfLongestSubstring(String s) {
       if(s.length() == 0 || s.length() == 1) return s.length();
       int max = 0;
       int left = 0;
       int right = 1;
        String curr = "" + s.charAt(left);
       while(right < s.length()) {
        if(curr.length() > max) max = curr.length();

        if(curr.contains("" + s.charAt(right))) {
            left++;
            curr = curr.substring(1, curr.length());
            continue;
        }

         curr += s.charAt(right);
         if(curr.length() > max) max = curr.length();
         right++;
       }
        return max;
    }
}
