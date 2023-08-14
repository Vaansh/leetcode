class Solution:
    def encode(self, strs):
        return "".join([str(len(s)) + "#" + s] for s in strs)

    def decode(self, str):
        i, res = 0, []
        while i < len(str):
            j = i
            while str[i] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + length])
            i = j + 1 + length