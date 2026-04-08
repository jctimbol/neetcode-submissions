class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> result = new HashMap<>();
        for(String s : strs) {
            int[] count = new int[26];
            for(char ch : s.toCharArray()) {
                count[(int)ch - (int)'a'] += 1;
            }
            String key = Arrays.toString(count);
            result.putIfAbsent(key, new ArrayList<>());
            result.get(key).add(s);
        }
        return new ArrayList<>(result.values());
    }

}
