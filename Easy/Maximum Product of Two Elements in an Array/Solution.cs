public class Solution 
{
    public int MaxProduct(int[] nums) 
    {
        int pointer = 0, max = 0;
        int len = nums.Length;        
        for(int i = pointer + 1; i < len; i++)
        {
            int temp = (nums[pointer]-1)*(nums[i]-1);
            if(temp > max)
            {
                max = temp;
            }
            
            if (i == len - 1)             
            {
                pointer++;
                i = pointer;
            }
        }
        return max;
    }
}