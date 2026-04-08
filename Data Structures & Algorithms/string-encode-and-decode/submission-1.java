class Solution {

    public String encode(List<String> strs) {
        String encoded = "";
        for(String str : strs) {
            encoded += str.length() + "#" + str;
        }
        return encoded;
    }

    public List<String> decode(String str) {
        List<String> strs = new ArrayList<String>();
        int i = 0;

        while(i < str.length()) {
            int strLength = 0;
            int j = i;
            while(str.charAt(j) != '#') {
                j++;
            }
            strLength = Integer.parseInt(str.substring(i,j));
            i=j+1;
            strs.add(str.substring(i, i+strLength));
            i += strLength;
        }
        return strs;
    }
}
