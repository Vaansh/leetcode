import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        int res = 1;
        int n = nums.length;
        if (n == 0) return 0;
        Arrays.sort(nums);

        int curr = 1;
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] == nums[i + 1]) continue;
            curr = (nums[i] + 1 == nums[i + 1]) ? curr + 1 : 1;
            res = Math.max(res, curr);
        }

        return Math.max(res, curr);
    }
}