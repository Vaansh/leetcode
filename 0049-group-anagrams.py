class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for st in strs:
            s = "".join(sorted(st))
            temp = d.get(s, [])
            temp.append(st)
            d[s] = temp

        return d.values()