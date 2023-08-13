class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        return "".join([str(len(s)) + "#" + s] for s in strs)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        i, res = 0, []
        while i < len(str):
            j = i
            while str[i] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + length])
            i = j + 1 + length
