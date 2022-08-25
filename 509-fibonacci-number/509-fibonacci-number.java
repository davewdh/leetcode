class Solution {
    public int fib(int n) {
        if ( n <= 1)
            return n;
        return fib(n-1) + fib(n-2);
        // if (n <= 1)
        //     return n;
        // int a = 0;
        // int b = 1;
        // int sum = 0;
        // int i = 2;
        // while (i <= n) {
        //     sum = a + b;
        //     a = b;
        //     b = sum;
        //     i++;
        // }
        // return sum;
    }
}