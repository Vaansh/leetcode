class Solution {
    public int maxProduct(int[] nums) {
        int res = nums[0];
        int currMin = 1, currMax = 1;
        
        for (int n : nums) {
            int tmpMin = n * currMin, tmpMax = n * currMax;
            currMin = Math.min(n, Math.min(tmpMin, tmpMax));
            currMax = Math.max(n, Math.max(tmpMin, tmpMax));
            res = Math.max(res, currMax);
        }
        
        return res;
    }
}