class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 != len2:
            return False

        if s1 == s2:
            return True

        if Counter(s1) == Counter(s2):
            count = 0
            for i in range(len1):
                if s1[i] != s2[i]:
                    count += 1
                    if count > 2:
                        break
            return count == 2

        return False
