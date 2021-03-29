public class Solution 
{
    public int SumOfUnique(int[] nums) 
    {        
        int res=0;
        for(int i=0; i<nums.Length; i++)
        {            
            if(Array.IndexOf(nums, nums[i]) == Array.LastIndexOf(nums, nums[i]))
            {
                res+=nums[i];                
            }            
        }
        return res;
    }
}