class Solution {
    public boolean isValid(String s) {
        Stack<Character> aStack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(' || c == '{' || c == '[')
                aStack.push(c);
            if (c == ')' || c == '}' || c == ']') {
                if (aStack.isEmpty())
                    return false;
                char top = aStack.pop();
                if ((top != '(') && (c == ')') || ((top != '{') && (c == '}')) || ((top != '[') && (c == ']')))
                    return false;
            }
        }
        return aStack.isEmpty();
    }
}