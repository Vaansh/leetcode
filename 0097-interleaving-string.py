class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        memo = {}

        if n + m != len(s3):
            return False

        def helper(i, j, curr_str, curr_size):
            if (i, j) in memo:
                return memo[(i, j)]

            if i >= n:
                res = curr_str + s2[j:] == s3
            elif j >= m:
                res = curr_str + s1[i:] == s3
            else:
                res = (
                    s1[i] == s3[curr_size]
                    and helper(i + 1, j, curr_str + s1[i], curr_size + 1)
                ) or (
                    s2[j] == s3[curr_size]
                    and helper(i, j + 1, curr_str + s2[j], curr_size + 1)
                )

            memo[(i, j)] = res
            return res

        return helper(0, 0, "", 0)
