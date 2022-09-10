class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        int count = words.length;
        for (String word : words) {
            for (int i = 0; i < word.length(); i++) {
                if (allowed.indexOf(word.charAt(i)) == -1) {
                    count--;
                    break;
                }
            }
        }
        return count;
    }
}