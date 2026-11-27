class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        miss = 0

        while True:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                miss = 0
            else:
                miss += 1
                if len(students) > 1:
                    students = students[1:] + [students[0]]
                else:
                    return 1

            if miss >= len(students):
                break

        return len(students)


# print(Solution.countStudents(Solution, [1,1,0,0], [0,1,0,1]))
print(Solution.countStudents(Solution, [1,1,1,0,0,1], [1,0,0,0,1,1]))