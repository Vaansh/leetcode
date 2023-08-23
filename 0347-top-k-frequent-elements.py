from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums).most_common()
        for (c, _) in count:
            if c in res:
                continue
            elif k == 0:
                break
            else:
                res.append(c)
                k -= 1
        return res
