import java.util.Arrays;

class Solution {
    public boolean isAnagram(String s, String t) {
        char[] cs = s.toCharArray(), ct = t.toCharArray();
        Arrays.sort(cs);
        Arrays.sort(ct);
        String ss = new String(cs), st = new String(ct);
        return ss.equals(st);
    }
}

// class Solution {
//     public boolean isAnagram(String s, String t) {
//         char[] charS = s.toCharArray(), charT = t.toCharArray();
//         Arrays.sort(charS);
//         Arrays.sort(charT);
//         return Arrays.equals(charS, charT);
//     }
// }

// class Solution {
//     public boolean isAnagram(String s, String t) {
//         if (s.length() != t.length()) {
//             return false;
//         }
//         HashMap<Character, Integer> sMap = new HashMap<>(), tMap = new HashMap<>();
//         for (char c : s.toCharArray()) {
//             sMap.put(c, sMap.getOrDefault(c, 0) + 1);
//         }
//         for (char c : t.toCharArray()) {
//             tMap.put(c, tMap.getOrDefault(c, 0) + 1);
//         }
//         return sMap.equals(tMap);
//     }
// }