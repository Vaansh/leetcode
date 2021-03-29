class Solution {
    public int[] twoSum(int[] nums, int target) {
        int pointer=0;
        int len=nums.length;                
        
        int[] sol = new int[2];                
        
        for(int i=pointer+1; i<len; i++){
            
            if(target==nums[pointer]+nums[i]){
                sol[0]=pointer;
                sol[1]=i;
                return sol;
            }
            
            if(i==len-1){
                pointer=pointer+1;
                i=pointer;
            }
        }
        return sol;
    }
}