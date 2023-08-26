import java.util.HashMap;
import java.util.Map;

class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        Map<Integer, Integer> memo = new HashMap<>();
        return helper(n, 0, nums, memo);
    }

    private int helper(int n, int i, int[] nums, Map<Integer, Integer> memo) {
        if (i >= n) return 0;
        if (memo.containsKey(i)) return memo.get(i);
        int res = Math.max(helper(n, i + 1, nums, memo), helper(n, i + 2, nums, memo) + nums[i]);
        memo.put(i, res);
        return res;
    }
}