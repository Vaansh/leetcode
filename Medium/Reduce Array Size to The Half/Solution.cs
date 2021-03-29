class Solution 
{
    public int MinSetSize(int[] arr) 
    {
        int count = 0;
        int threshold = arr.Sum()/2;        
        Dictionary<int, int> freq = new Dictionary<int, int>();

        foreach(int n in arr)
        {
            if(freq.ContainsKey(n))
            {
                freq[n]=freq[n]+1;
            }
            else
            {
               freq.Add(n, 1);
            }
        }        
        
        List<int> prod = new List<int>();    
        foreach(var n in freq)
        {
            prod.Add(n.Key*n.Value);
        }
        
        var descprod = prod.OrderByDescending(i => i);
        
        foreach(var n in descprod)
        {
            if(threshold<=0)
            {
                break;
            }
            threshold -= n;
            count++;
        }                                              
        
        return count;
    }        
}