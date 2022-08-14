class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        if (ransomNote.length() > magazine.length())
            return false;
        
        HashMap<Character, Integer> aMap = new HashMap<>();
        for (int i = 0; i < magazine.length(); i++) {
            if (!aMap.containsKey(magazine.charAt(i))) {
                aMap.put(magazine.charAt(i), 1);
            } else {
                aMap.put(magazine.charAt(i), aMap.get(magazine.charAt(i)) + 1);
            }
        }
        
        for (int i = 0; i < ransomNote.length(); i++) {
            if (!aMap.containsKey(ransomNote.charAt(i))) {
                return false;
            } else {
                aMap.put(ransomNote.charAt(i), aMap.get(ransomNote.charAt(i)) - 1);
                if (aMap.get(ransomNote.charAt(i)) < 0) 
                    return false;
            }
        }
        return true;
        
        
    }
}