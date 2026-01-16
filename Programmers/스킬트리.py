def solution(skill, skill_trees):
    ans = 0
    skill = list(skill)
    
    for sk in skill_trees:
        idx = 0
        ok = True
        for s in sk:
            if s in skill:
                if skill.index(s) == idx:
                    idx += 1
                else:
                    ok = False
                    break
        if ok:
            ans += 1
            
    return ans