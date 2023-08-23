from random import choice


class RandomizedSet:
    def __init__(self):
        self.m, self.s = {}, []

    def insert(self, val: int) -> bool:
        if val in self.m:
            return False
        self.m[val] = len(self.s)
        self.s.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.m:
            self.m[self.s[-1]], self.s[self.m[val]] = self.m[val], self.s[-1]
            self.s.pop()
            self.m.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.s)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
