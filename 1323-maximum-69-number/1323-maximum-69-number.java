class Solution {
    public int maximum69Number (int num) {
        String s = (num + "").replaceFirst("6", "9");
        return Integer.parseInt(s);
    }
}