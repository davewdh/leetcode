class Solution {
    private ArrayList<String> ans;
    private int n;
    public List<String> generateParenthesis(int n) {
        this.ans = new ArrayList<>();
        this.n = n;
        backTracking("", 0, 0);
        return ans;
    }

    private void backTracking(String s, int leftN, int rightN) {
        if (s.length() == 2 * n) {
            ans.add(s);
            return;
        }
        if (leftN < n) {
            backTracking(s + "(", leftN + 1, rightN);
        }
        if (rightN < leftN) {
            backTracking(s + ")", leftN, rightN + 1);
        }
    }
}