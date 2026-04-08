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
