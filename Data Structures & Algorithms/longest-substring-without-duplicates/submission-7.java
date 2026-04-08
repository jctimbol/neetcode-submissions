class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length() == 0) return 0;
        if(s.length() == 1 || (s.length() == 2 && s.charAt(0) == s.charAt(1))) return 1;
        if(s.length() == 2 && s.charAt(0) != s.charAt(1)) return 2; 
        
        int left = 0;
        int maxLength = 0;
        String currString = "";
        for(int right = 0; right < s.length(); right++) {
            while(currString.contains("" + s.charAt(right))) {
                if(currString.length() > maxLength) maxLength = currString.length();
                currString = currString.substring(1, currString.length());
                left++;
            }
            currString += "" + s.charAt(right);
        }
        if(currString.length() > maxLength) maxLength = currString.length();
        return maxLength;
    }
}
