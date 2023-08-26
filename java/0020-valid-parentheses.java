import java.lang.*;
import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> openMap = Map.of('(', ')', '{', '}', '[', ']');
        Map<Character, Character> closeMap = Map.of(')', '(', '}', '{', ']', '[');

        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (openMap.containsKey(c)) {
                stack.push(c);
            } else if (closeMap.containsKey(c)) {
                if (stack.isEmpty() || openMap.get(stack.pop()) != c) return false;
          }
        }
        
        return stack.isEmpty();
    }
}