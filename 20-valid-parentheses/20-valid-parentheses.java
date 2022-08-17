class Solution {
    public boolean isValid(String s) {
        Stack<Character> aStack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[')
                aStack.push(s.charAt(i));
            if (s.charAt(i) == ')' || s.charAt(i) == '}' || s.charAt(i) == ']') {
                if (aStack.isEmpty())
                    return false;
            
                
                switch (s.charAt(i)) {
                    case ')' :
                        if (aStack.pop() != '(')
                            return false;
                        break;
                    case '}' :
                        if (aStack.pop() != '{')
                            return false;
                        break;
                    case ']' :
                        if (aStack.pop() != '[')
                            return false;
                        break;
                    default:
                            return false;
                }
            }
                
                
        
        }
        return aStack.isEmpty();
    }
}