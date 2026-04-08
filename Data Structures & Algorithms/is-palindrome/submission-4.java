class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        for(char ch : s.toCharArray()) {
            if(Character.isLetterOrDigit(ch)) sb.append(ch);
        }
        String result = sb.toString().toLowerCase();
        return (result.equals(new StringBuilder(result).reverse().toString()));
    }
}
