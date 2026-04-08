class Solution {
    public boolean isPalindrome(String s) {
        //if(s.length() == 0 || s.length() == 1) return true;
        int ptr1 = 0;
        int ptr2 = s.length() - 1;

        while(ptr1<ptr2) {
            if(!Character.isLetterOrDigit(s.charAt(ptr1))) {
                ptr1++;
                continue;
            }
            if(!Character.isLetterOrDigit(s.charAt(ptr2))) {
                ptr2--;
                continue;
            }
            if(s.toLowerCase().charAt(ptr1) != s.toLowerCase().charAt(ptr2)) return false;
            ptr1++;
            ptr2--;
        }
        return true;
    }
}
