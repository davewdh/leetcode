class Solution {
    public boolean isValid(String s) {
        Stack<Character> aStack = new Stack<>();
        char c;
        for (int i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            switch(c) {
                case '(':
                case '{':
                case '[':
                    aStack.push(c);
                    break;
                case ')':
                    if ((aStack.isEmpty()) || (aStack.pop() != '(')) 
                        return false;
                    break;
                case '}':
                    if ((aStack.isEmpty()) || (aStack.pop() != '{')) 
                        return false;
                    break;
                case ']':
                    if ((aStack.isEmpty()) || (aStack.pop() != '[')) 
                        return false;
                    break;
            }
        }
        return aStack.isEmpty();
        
        // Stack<Character> aStack = new Stack<>();
        // char c;
        // for (int i = 0; i < s.length(); i++) {
        //     c = s.charAt(i);
        //     if (c == '(' || c == '{' || c == '[')
        //         aStack.push(c);
        //     if (c == ')' || c == '}' || c == ']') {
        //         if (aStack.isEmpty())
        //             return false;
        //         char top = aStack.pop();
        //         if ((top != '(') && (c == ')') || ((top != '{') && (c == '}')) || ((top != '[') && (c == ']')))
        //             return false;
        //     }
        // }
        // return aStack.isEmpty();
    }
}