class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces_count = text.count(' ')
        if spaces_count == 0:
            return text
        if len(words) == 1:
            return words[0] + ' ' * spaces_count
        space, remain = spaces_count // (len(words) - 1), spaces_count % (len(words) - 1)
        ans = ''

        for i in range(len(words)):
            if i == len(words) - 1:
                ans += words[i]
            else:
                ans += words[i]
                ans += (' ' * space)

        ans += (' ' * remain)
        return ans