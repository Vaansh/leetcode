class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        
        return Math.max(helper(nums, 0, n - 2), helper(nums, 1, n - 1));
    }

    private int helper(int[] nums, int start, int end) {
        int robCurr = 0;
        int robPrev = 0;
        
        for (int i = start; i <= end; i++) {
            int temp = robCurr;
            robCurr = Math.max(robCurr, robPrev + nums[i]);
            robPrev = temp;
        }
        
        return robCurr;
    }
}
