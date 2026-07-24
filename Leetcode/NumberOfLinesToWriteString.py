class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        pixel = 0
        line = 1
        
        for S in s:
            w = widths[ord(S) - 97]

            if pixel + w <= 100:
                pixel += w
            else:
                pixel = w
                line += 1

        return [line, pixel]