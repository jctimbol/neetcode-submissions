class Solution {
    public int climbStairs(int n) {
        int[] arr = new int[n+1];
        return dp(arr, n);
    }
    int dp(int[] arr, int n) {
        if(n==0 || n==1) return 1;
        if(arr[n] != 0) return arr[n];
        arr[n] = dp(arr, n-1) + dp(arr, n-2);
        return arr[n];
    }
}
