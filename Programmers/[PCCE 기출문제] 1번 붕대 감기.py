def solution(bandage, health, attacks):
    successive = 0
    maxHealth = health
    t, x, y = bandage[0], bandage[1], bandage[2]
    
    for i in range(1, attacks[-1][0] + 1):
        if attacks[0][0] == i:
            health -= attacks[0][1]
            successive = 0
            del attacks[0]
            if health <= 0:
                return -1
        else:
            health += x
            if health > maxHealth:
                health = maxHealth
            successive += 1
            if successive == t:
                health += y
                if health > maxHealth:
                    health = maxHealth
                successive = 0
                
    return health

# 연속 성공 횟수 저장 변수 (successive)
# attacks가 빌 때까지 반복 (1초 ~ attacks[-1][0])
# 해당 초에 공격이 없으면
    # 초당 회복량 만큼 체력 증가
    # 연속 성공 횟수 증가
    # 연속 성공 횟수와 시전 시간이 같다면
        # 추가 회복량 만큼 체력 증가
        # 연속 성공 횟수 초기화
    # cf) 체력 증가 시 최대 체력을 초과하지 못함
# 해당 초에 공격이 있으면
    # 피해량만큼 체력 감소
    # 체력이 0 이하가 되면 즉시 -1 리턴
# 현재 체력 리턴