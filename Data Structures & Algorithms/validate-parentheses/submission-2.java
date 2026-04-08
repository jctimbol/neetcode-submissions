class Solution {
    public boolean isValid(String s) {
        Stack<Character> parStack = new Stack<>();

        String left = "({[";
        String right = ")}]";

        for(char par : s.toCharArray()) {
           //System.out.println("" + par);
            if(left.contains("" + par)) {
                parStack.push(par);
            }
            else {  
                if(parStack.isEmpty()) {
                    return false;
                }

                char topPar = parStack.pop();
                //System.out.println(topPar);
                int indexClosePar = right.indexOf(par);
                //System.out.println(indexClosePar +  " " + left.indexOf(topPar));
                
                if(indexClosePar != left.indexOf(topPar)) {
                    return false;
                }
            }
        }
        if(!parStack.isEmpty()) {
            return false;
        }

        return true;

    }
}
