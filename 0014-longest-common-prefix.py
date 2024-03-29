class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for s in list(zip(*strs)):
            if len(set(s)) == 1:
                res += s[0]
            else:
                break
        return res
