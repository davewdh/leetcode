class Solution {
    public int mostWordsFound(String[] sentences) {
        int max = 0;
        for (String s : sentences) {
            String[] splied = s.split("\\s+");
            max = Math.max(max, splied.length);
        }
        return max;
    }
}