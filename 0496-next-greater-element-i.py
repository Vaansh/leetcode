class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, num_map = [], {}
        
        for n in nums2:
            while len(stack) > 0 and stack[-1] < n:
                num_map[stack.pop()] = n
            stack.append(n)

        for i in range(len(nums1)):
            nums1[i] = num_map.get(nums1[i], -1)
        return nums1