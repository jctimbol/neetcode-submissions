class Solution {
    public boolean isValid(String s) {
        Stack<Character> p = new Stack<>();
        String b = "([{";
        for(char ch : s.toCharArray()) {
            if(b.contains("" + ch)) p.push(ch);
            else {
                if(p.isEmpty()) return false;
                char par = p.peek();
                if(ch == ')' && par != '(') return false;
                else if(ch == '}' && par != '{') return false;
                else if(ch == ']' && par != '[') return false;
                p.pop();
            }
        }
        return p.isEmpty();
    }
}
