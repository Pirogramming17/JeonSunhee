import random
num = 0

# 입력값 유효성 검사 함수
def isValid(x):
    try:
        x = int(x)
        if x==1 or x==2 or x==3:
            return 1
        return 2
    except ValueError:
        return 3

# 게임 함수
def brGame(player, num):
    if player == 'player': # 사람이라면, 직접 입력 받는다
        cnt = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')

        # 제대로 입력받을 때까지 반복
        while (isValid(cnt) != 1):
            if isValid(cnt) == 3:
                print('정수를 입력하세요')
            else:
                print('1,2,3 중 하나를 입력하세요')
            cnt = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')
    else: # 컴퓨터라면, 랜덤 값 할당
        cnt = random.randint(1,3)

    cnt = int(cnt)

    for i in range(cnt):
        num+=1
        print(player,num)
        if num == 31:
            return 999 # 게임 끝
    return num

# 반복 실행    
players = ['computer','player']
num = 0
while num < 31:
    for player in players:
        num = brGame(player,num)
        if num == 999: # 게임이 끝났다면
            players.remove(player)
            print(players.pop(), "win!")
            break