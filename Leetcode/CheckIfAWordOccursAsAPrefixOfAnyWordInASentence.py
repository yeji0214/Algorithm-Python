class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentences = sentence.split()

        for i in range(len(sentences)):
            if searchWord in sentences[i] and sentences[i].index(searchWord) == 0:
                print(sentences[i].index(searchWord))
                return i + 1

        return -1