class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() < 1)
            return 0;
        if (s.length() == 1)
            return 1;
        int max = 0;
        for (int i = 0; i < s.length()-1; i++) {
            Set<Character> aSet = new HashSet<>();
            aSet.add(s.charAt(i));
            int count = 1;
            for (int j = i+1; j < s.length(); j++) {
                if (aSet.add(s.charAt(j))) 
                    count++;  
                else
                    break;
            }
            if (count > max)
                max = count;
        }
        return max;
    }
}