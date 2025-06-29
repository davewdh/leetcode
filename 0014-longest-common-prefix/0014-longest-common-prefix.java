class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = strs[0];
        for (String s : strs) {
            while (!s.startsWith(prefix)){
                prefix = prefix.substring(0, prefix.length()-1);
                if (prefix == ""){
                    return "";
                }
            }
        }
        return prefix;
    }
}