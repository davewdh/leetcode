class Solution {
    public int subtractProductAndSum(int n) {
        int sum = 0;
        int product = 1;
        while (n != 0) {
            int temp = n%10;
            if (temp == 0)
                product = 0;
            sum += temp;
            product *= temp;
            
            n /= 10;
        }
        
        return product - sum;
    }
}