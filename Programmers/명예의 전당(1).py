def solution(k, score):
    the_hall_of_fame = []
    answer = []
    
    for s in score:
        the_hall_of_fame.append(s)
        the_hall_of_fame.sort(reverse=True)
        if len(the_hall_of_fame) > k:
            the_hall_of_fame = the_hall_of_fame[:k]
        answer.append(the_hall_of_fame[-1])
            
    return answer