import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words_count = {}
        split_result = re.split("[ !?',;.]", paragraph)

        for r in split_result:
            if r:
                word = r.lower()
                words_count[word] = words_count.get(word, 0) + 1

        sorted_result = sorted(words_count.items(), key = lambda x: -x[1])

        for k, v in sorted_result:
            if k not in banned:
                return k