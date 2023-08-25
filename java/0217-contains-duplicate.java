import java.util.*;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        
        for (var n : nums) {
            if (set.contains(n)) return true;
            set.add(n);
        }

        return false;
    }
}