class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        res = 0
        ratio_map = {}

        for r in rectangles:
            ratio = r[0] / r[1]
            ratio_map[ratio] = ratio_map.get(ratio, 0) + 1

        for n in ratio_map.values():
            res += n**2 - sum(range(n + 1))
        return res


# (MLE)
# class Solution:
#     def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
#         d = defaultdict(list)
#         for r in rectangles:
#             d[r[0]/r[1]].append(r)
#         return sum(len(list(combinations(v, 2))) for v in d.values())
