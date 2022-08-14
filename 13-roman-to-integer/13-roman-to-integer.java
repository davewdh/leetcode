class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> aMap = new HashMap<>();
        aMap.put('I', 1);
        aMap.put('V', 5);
        aMap.put('X', 10);
        aMap.put('L', 50);
        aMap.put('C', 100);
        aMap.put('D', 500);
        aMap.put('M', 1000);
        int count = 0;
        for (int i = 1; i < s.length(); i++) {
            if (aMap.get(s.charAt(i-1)) >= aMap.get(s.charAt(i)))
                count += aMap.get(s.charAt(i-1));
            else
                count -= aMap.get(s.charAt(i-1));
        }
        return count + aMap.get(s.charAt(s.length()-1));
    }
    
}