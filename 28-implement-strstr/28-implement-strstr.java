class Solution {
    public int strStr(String haystack, String needle) {
        if ((needle == "") ||(needle.equals(haystack)))
            return 0;
        for (int i = 0; i < haystack.length(); i++) {
            int count = 0;
            if ((haystack.charAt(i) == needle.charAt(0)) && (needle.length() <= haystack.length()-i)) {
                if (needle.length() == 1)
                    return i;
                for (int j = 1; j < needle.length(); j++) {
                    if (haystack.charAt(i+j) != needle.charAt(j))
                        break;
                    count++;
                    if (count == needle.length()-1)
                        return i;
                }
            }
        }
        return -1;
        
        
        
        
        
        
        // return haystack.indexOf(needle);
    }
}