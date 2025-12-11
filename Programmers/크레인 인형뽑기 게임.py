def solution(board, moves):
    stack = []
    ans = 0
    
    for m in moves:
        lst = [b[m - 1] for b in board]
        for i in range(len(lst)):
            if lst[i] == 0:
                continue
            else:
                board[i][m - 1] = 0
                if len(stack) > 0 and stack[-1] == lst[i]:
                    stack.pop()
                    ans += 1
                else:
                    stack.append(lst[i])
                break
                    
    return ans * 2

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))