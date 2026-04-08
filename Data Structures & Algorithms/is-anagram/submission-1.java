class Solution {
    public boolean isAnagram(String s, String t) {
        boolean anagram = true;

        char[] word1 = s.toCharArray();
        char[] word2 = t.toCharArray();

        Arrays.sort(word1);
        Arrays.sort(word2);

       if(!Arrays.equals(word1, word2))
       {
        anagram = false;
       }
       
        return anagram;
    }
}
