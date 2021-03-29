class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
                                                                                   
        ArrayList<Integer> temp =  new ArrayList<Integer>();
                
        for(int x : nums1){
            temp.add(x);
        }
        
        for(int x : nums2){
            temp.add(x);
        }
        
        Collections.sort(temp);        
        int m = temp.size()/2;
                        
        if(temp.size()%2 == 0){
            float result = (temp.get(m) + temp.get(m-1));
            return result/2;
        }
        else{            
            return temp.get(m);                        
        }
    }
}
