import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        def compare(x, y):
            return int(y + x) - int(x + y)
        
        nums.sort(key=functools.cmp_to_key(compare))
        largest_num = ''.join(nums).lstrip('0')
        return largest_num if largest_num else '0'
