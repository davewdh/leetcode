class Solution {
    private ArrayList<String> ans;
    private int n;
    public List<String> generateParenthesis(int n) {
        this.ans = new ArrayList<>();
        this.n = n;
        backTracking("", 0, 0);
        return ans;
    }
    private void backTracking(String s, int left, int right){
        if (s.length() == 2 * n) {
            ans.add(s);
            return;
        }
        if (left < n) {
            backTracking(s + "(", left+1, right);
        } 
        if (right < left) {
            backTracking(s + ")", left, right+1);
        }
        
    }
}