class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        whole = []
        start = []

        for p in paths:
            whole.append(p[0])
            whole.append(p[1])

            if p[0] not in start:
                start.append(p[0])

        for w in list(set(whole)):
            if w not in start:
                return w
