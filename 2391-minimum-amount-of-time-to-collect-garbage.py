class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        units = []

        for g in garbage:
            units.append([g.count("G"), g.count("P"), g.count("M")])

        for i, u in enumerate(units):
            res += sum(u)
            if i < len(travel):
                res += travel[i] * 3

        last_g, last_p, last_m = len(travel), len(travel), len(travel)

        while units[last_g][0] == 0 and last_g > 0:
            last_g -= 1

        while units[last_p][1] == 0 and last_p > 0:
            last_p -= 1

        while units[last_m][2] == 0 and last_m > 0:
            last_m -= 1

        res -= sum(travel[last_g:]) + sum(travel[last_p:]) + sum(travel[last_m:])

        return res
