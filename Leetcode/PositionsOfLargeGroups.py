class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start_index = 0
        end_index = 1
        prev_c = s[0]
        result = []

        for i in range(1, len(s)):
            if prev_c == s[i]:
                end_index += 1
                if i == len(s) - 1 and end_index - start_index >= 3:
                    result.append([start_index, end_index - 1])
                    
            else:
                if end_index - start_index >= 3:
                    result.append([start_index, end_index - 1])
                start_index = i
                end_index = i + 1
                prev_c = s[i]

        return result