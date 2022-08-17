class Solution {
    public int mySqrt(int x) {
        if (x == 0)
            return 0;
        if (x == 1)
            return 1;
        
        for (int i = 1; i <= x/i; i++) {
            if ((i <= x/i) && ( i+1 > (x / (i+1))))
                return i;  
        }
        return -1;
        
        // int i = 1;
        // while (i <= x/2) {
        //     if ((i <= x/i) && ( i+1 > (x / (i+1))))
        //         break;  
        //     i++;
        // }
        // return i;
    }
}