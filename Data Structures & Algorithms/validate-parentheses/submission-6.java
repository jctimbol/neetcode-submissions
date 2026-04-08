class Solution {
    public boolean isValid(String s) {
      Stack<Character> parStack = new Stack<>();
      HashMap<Character, Character> parMap = new HashMap<>();
      parMap.put(')', '(');
      parMap.put(']', '[');
      parMap.put('}', '{');
      for(char ch : s.toCharArray()) {
        if(parMap.containsValue(ch)) {
            parStack.push(ch);
        }
        if(parMap.containsKey(ch)) {
            if(parStack.isEmpty() || parStack.pop() != parMap.get(ch)) {
                return false;
            }
        }
      }
      return parStack.isEmpty();
    }
}

/***
class Solution {
    public boolean isValid(String s) {
       String openPar = "([{";
       String closePar = ")]}";
       Stack<String> parStack = new Stack<>();

        for(int i = 0; i < s.length(); i++) {
            String currChar = "" + s.charAt(i);
            if(openPar.contains(currChar)) {
                parStack.push(currChar);
            }
            if(closePar.contains(currChar)) {
                if(parStack.isEmpty() || openPar.indexOf(parStack.pop()) != closePar.indexOf(currChar)) {
                        return false;
                }
            }
        
        }
        return parStack.isEmpty();
    }
}
*///