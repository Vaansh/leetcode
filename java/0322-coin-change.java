import java.util.Arrays;

class Solution {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0) return 0;
        int n = coins.length;
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < n; j++) {
                if (i - coins[j] >= 0) dp[i] = Math.min(1 + dp[i - coins[j]], dp[i]);
            }
        }

        return dp[amount] == amount + 1 ? -1 : dp[amount];
    }
}


// class Solution {
//     public int coinChange(int[] coins, int amount) {
//         int[] memo = new int[amount + 1];
//         Arrays.fill(memo, -1);
//         int res = helper(coins, amount, 0, memo);
//         return res == Integer.MAX_VALUE ? -1 : res;
//     }
//     private int helper(int[] coins, int n, int number, int[] memo) {
//         if (n == 0) return 0;
//         int res = Integer.MAX_VALUE;
//         for (int coin : coins) {
//             if (n < coin) continue;
//             int temp = 0;
//             temp = memo[n - coin] == -1 ? helper(coins, n - coin, number + 1, memo) : memo[n - coin];
//             if (temp != Integer.MAX_VALUE) res = Math.min(res, temp + 1);
//         }
//         return memo[n] = res;
//     }
// }

// class Solution {
//     public int coinChange(int[] coins, int amount) {
//         Map<Integer, Integer> map = new HashMap<Integer, Integer>();
//         return helper(coins, amount, map);    
//     }
//     private int helper(int[] coins, int amount, Map<Integer, Integer> map) {
//         if (amount == 0) return 0;
//         if (map.containsKey(amount)) return map.get(amount);
//         int max = Integer.MAX_VALUE;
//         for (int coin: coins) {
//             int remainder = amount - coin;
//             if (remainder < 0) continue;
//             int temp = helper(coins, remainder, map);
//             if (temp != -1) max = Math.min(max, temp);
//         }
//         map.put(amount, max != Integer.MAX_VALUE ? max + 1 : -1);
//         return map.get(amount);
//     }
// }