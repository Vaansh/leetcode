from collections import Counter


class Solution:
    def findAnagrams(self, s: str, t: str):
        res = []

        if len(t) > len(s):
            return res

        freq = Counter(t)
        required = len(freq)
        
        l, r = 0, 0
        while r < len(s):
            if s[r] in freq:
                freq[s[r]] -= 1
                if freq[s[r]] == 0:
                    required -= 1
            r += 1
            
            while required == 0:
                if s[l] in freq:
                    freq[s[l]] += 1
                    if freq[s[l]] > 0:
                        required += 1
                if r - l == len(t):
                    res.append(l)
                l += 1
            
        return res
