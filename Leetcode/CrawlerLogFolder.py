class Solution:
    def minOperations(self, logs: list[str]) -> int:
        folder = []

        for log in logs:
            if log == "../":
                if folder:
                    folder.pop()
            elif log != "./":
                folder.append(log)

        return len(folder)