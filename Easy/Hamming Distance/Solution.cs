public class Solution 
{
    public int HammingDistance(int x, int y) 
    {        
        string[] bins = equalize(Convert.ToString(x, 2), Convert.ToString(y, 2));              
        int dist=0, n=0;
        while(n<bins[0].Length)
        {
            if(!bins[0][n].Equals(bins[1][n]))
            {
                dist++;                        
            }
            n++;            
        }
        return dist;
    }
    
    public string[] equalize(string x, string y)
    {
        int len = x.Length - y.Length;
        if(len>0)
        {
            return new string[] {x, y.PadLeft(len+y.Length,'0')};
        }
        else if(len<0)
        {
            return new string[] {x.PadLeft(-1*len+x.Length,'0'), y}; 
        }
        else
        {
            return new string[] {x,y};
        }
    }
}