from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        s1_freq, s2_freq = Counter(s1), Counter(s2[:n])

        for i in range(n, m):
            if s1_freq == s2_freq:
                return True
            s2_freq[s2[i - n]] -= 1
            s2_freq[s2[i]] += 1

        return s1_freq == s2_freq
