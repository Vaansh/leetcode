from collections import Counter

# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         return min(
#             text.count("b"),
#             text.count("a"),
#             text.count("l") // 2,
#             text.count("o") // 2,
#             text.count("n"),
#         )


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter_text = Counter(text)
        return min(
            counter_text.get("b", 0),
            counter_text.get("a", 0),
            counter_text.get("l", 0) // 2,
            counter_text.get("o", 0) // 2,
            counter_text.get("n", 0),
        )
