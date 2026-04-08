class Solution {
    public boolean isPalindrome(String s) {
        boolean pal = true;
        String word = s.toLowerCase().replaceAll("[^A-Za-z0-9]", "");
        System.out.println(word);
        for(int i = 0; i < word.length() / 2; i++)
        {
            if(word.charAt(i) != word.charAt(word.length() - 1 - i))
            {
                pal = false;
                break;
            }
        }
        return pal;
    }
}
