#include<iostream>
using namespace std;

class Solution {
public:
    int numTrees(int n) {
        int dp[n + 1]; 
        fill_n(dp, n + 1, 0); 
        dp[0] = 1; 
        dp[1] = 1; 
        for (int i = 2; i <= n; i++) { 
            for (int j = 1; j <= i; j++) { 
                dp[i] = dp[i] + (dp[i - j] * dp[j - 1]); 
            } 
        } 
        return dp[n]; 
    }
};

int main() {
    Solution solution;
    solution.numTrees(3);
}