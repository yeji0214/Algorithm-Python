class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

        d, m, y = date.split()
        d = f"{int(d[:-2]):02d}"
        m = f"{month[m]:02d}"
        y = int(y)

        return f"{y}-{m}-{d}"