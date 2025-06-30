class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;
    public MinStack() {
        stack = new Stack<>();   //1 3 5 2
        minStack = new Stack<>();//1. 1 1 1
    }
    
    public void push(int val) {
        stack.push(val);
        int curMin = val;
        if (!minStack.isEmpty()){
            if (curMin > minStack.peek()){
                curMin = minStack.peek();
            }
        }
        minStack.push(curMin);
    }
    
    public void pop() {
       stack.pop();
       minStack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */