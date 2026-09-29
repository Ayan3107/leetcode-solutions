class Solution {
    public:
    bool hasValidPath(vector<vector<char>>& grid) {
        int m =grid.size();
        ont n =grid[0].size();

        // A valid parentheses string must have even length
        if ((m + n - 1)%2 == 1)
        return False;


        // Start must be'(' and end must be')'
        if(grid[0][0] ==')' || grid[m-1][n-1]=='(')
        return false;

        vector<vector<unordered_set<int>>> dp(
            m, vector<unordered_set<int>>(n)
        );

        dp[0][0].insert(1);

        for (int i =0; i<m; i++) {
            for (int j =0; j<n; j++) {

                for (int balance : dp[i][j]) {

                    // Move down
                    if (i+1 < m) {
                        if (grid[i+1][j] == '(') {
                            dp[i+1][j].insert(balance + 1);
                        } else if (balance > 0) {
                            dp[i + 1][j].insert(balance - 1);
                        }
                    }

                    // Move right
                    if (j + 1 < n){
                        if (grid[i][j+1] == '(') {
                            dp[i][j+1].insert(balance + 1)
                        } else if(balance >0) {
                            dp[i][j+1].insert(balance - 1);
                        }
                    }
                }
            }
        }
        return dp[m - 1][n - 1].count(0) >0;
    }
};