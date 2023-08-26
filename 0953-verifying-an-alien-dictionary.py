class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        a = {}
        for i, o in enumerate(order):
            a[o] = i + 1

        for i in range(1, len(words)):
            prev_word, word = words[i - 1], words[i]
            for l1, l2 in zip(prev_word, word):
                if a[l1] > a[l2]:
                    return False
                elif a[l1] < a[l2]:
                    break
            else:
                if len(prev_word) > len(word):
                    return False

        return True
