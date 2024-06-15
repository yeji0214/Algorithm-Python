equations = input().split()
answers = []

for i in equations:
	answers.append(eval(i))
	
print(max(answers))