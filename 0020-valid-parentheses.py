class Solution:
    def isValid(self, s: str) -> bool:
        left_map = {"(": ")", "{": "}", "[": "]"}
        right_map = {")": "(", "}": "{", "]": "["}

        stack = []

        for p in s:
            if p in left_map:
                stack.append(p)

            if p in right_map:
                if len(stack) == 0:
                    return False
                elif left_map[stack.pop()] != p:
                    return False

        return len(stack) == 0
