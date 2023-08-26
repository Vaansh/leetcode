import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            char[] cs = s.toCharArray();
            Arrays.sort(cs);

            String anagram = new String(cs);
            List<String> val = map.getOrDefault(anagram, new ArrayList<String>());
            val.add(s);
            map.put(anagram, val);
        }
        
        return new ArrayList<>(map.values());
    }
}