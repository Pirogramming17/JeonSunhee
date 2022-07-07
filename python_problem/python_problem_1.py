num = 0

cnt = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')

# 입력값 유효성 검사 함수
def isValid(x):
    try:
        x = int(x)
        if x==1 or x==2 or x==3:
            return 1
        return 2
    except ValueError:
        return 3
# 제대로 입력받을 때까지 반복
while (isValid(cnt) != 1):
    if isValid(cnt) == 3:
        print('정수를 입력하세요')
    else:
        print('1,2,3 중 하나를 입력하세요')
    cnt = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')

cnt = int(cnt)

for i in range(cnt):
    num+=1
    print("PlayerA :", num)

cnt2 = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')

# 제대로 입력받을 때까지 반복
while (isValid(cnt2) != 1):
    if isValid(cnt2) == 3:
        print('정수를 입력하세요')
    else:
        print('1,2,3 중 하나를 입력하세요')
    cnt2 = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')

cnt2 = int(cnt2)

for i in range(cnt2):
    num+=1
    print("PlayerB :", num)