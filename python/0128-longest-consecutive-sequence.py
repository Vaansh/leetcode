class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len, num_set = 0, set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                curr_num, curr_len = num, 1
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)

        return max_len
