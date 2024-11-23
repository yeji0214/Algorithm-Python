N, K = map(int, input().split())
conveyor = list(map(int, input().split()))
stage = 0
robots = [] # 로봇 좌표

while True:
    # 종료 조건
    if conveyor.count(0) >= K:
        print(stage)
        exit(0)

    # 1단계 (벨트와 로봇 회전)
    conveyor = [conveyor[-1]] + conveyor[0:2 * N - 1]
    robots = [r + 1 for r in robots if r + 1 < N - 1]

    # 2단계 (로봇 이동 & 내구도 감소)
    if len(robots) > 0:
        for i in range(len(robots) - 1, -1, -1):
            next = robots[i] + 1
            if next not in robots:
                # 내리는 위치여도 내구도는 감소해야 함
                if next < N and conveyor[next] > 0:
                    conveyor[next] -= 1
                    robots[i] += 1

    robots = [r for r in robots if r < N - 1]
                
    # 3단계 (로봇 올리기)
    if conveyor[0] > 0 and 0 not in robots:
        robots.insert(0, 0)
        conveyor[0] -= 1

    stage += 1