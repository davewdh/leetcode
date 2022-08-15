class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0)
            return false;
        else {
            String str = Integer.toString(x);
            int index = str.length()-1;
            for (int i = 0; i < str.length()/2; i++) {
                if (str.charAt(i) != str.charAt(index))
                    return false;
                index--;
            }
            
        }
        return true;
            

    }
}