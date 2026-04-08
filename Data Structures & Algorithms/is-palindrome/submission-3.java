class Solution {
    public boolean isPalindrome(String s) {
        String str = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        if(str.length() <= 1) return true;
        System.out.println(str);
        int ptr1 = 0;
        int ptr2 = str.length() - 1;
        for(int i = 0; i < str.length() /  2; i++) {
            if(str.charAt(ptr1) != str.charAt(ptr2)) return false;
            ptr1++;
            ptr2--;
        }
        return true;
    }
}
