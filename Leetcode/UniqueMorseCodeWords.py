class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = { "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.." }
        result = []

        for word in words:
            r = ''
            for w in word:
                r += morse[w]
            result.append(r)
        
        return len(set(result))