# 파이썬 코테 기본문법

my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
value_to_find = 1
keys = [key for key, val in my_dict.items() if val == value_to_find]
print(keys)  # 출력: ['a', 'c']



temp = ['k', 'o', 'r', 'e', 'a']

for idx, value in enumerate(temp):
	print(idx, value)



dic = {'apple': 3, 'banana': 1, 'pear': 5}
lst = [['apple', 3], ['banana', 1], ['pear',5]]
print(sorted(lst, key= lambda x : (x[1], x[0])))



a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = list(zip(*a))[0]
print(b)
# (1, 4, 7)

c = list(zip(*a))[1]
print(c)
# (2, 5, 8)