class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, l = 0, 0
        freq = {}

        for r, r_char in enumerate(s):
            freq[r_char] = freq.get(r_char, 0) + 1
            window_len = r - l + 1
            max_freq = max(freq.values())
            if window_len - max_freq <= k:
                res = max(res, window_len)
            else:
                freq[s[l]] -= 1
                l += 1

        return res
