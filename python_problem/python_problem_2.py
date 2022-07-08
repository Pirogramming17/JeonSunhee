from numpy import append

students = []

##############  menu 1
def Menu1(stud) :
    students.append(stud)

##############  menu 2
def Menu2() :
    for stud in students:
        if len(stud) != 4:
            mean = (int(stud[1]) + int(stud[2])) / 2
            if mean >= 90:
                stud.append('A')
            elif mean >= 80:
                stud.append('B')
            elif mean >= 70:
                stud.append('C')
            else:
                stud.append('D')

##############  menu 3
def Menu3() :
    print('-----------------------------------')
    print('name  mid  final  grade')
    print('-----------------------------------')
    for stud in students:
        for i in stud:
            print(i, end='  ')
        print('\n')

##############  menu 4
def Menu4(i):
    print(students[i][0], 'student is deleted.')
    del(students[i])
    
# menu1에 해당하는 입력값 유효성 검사 함수
def isValid(temp, students):
    # 데이터 입력 갯수 체크
    if len(temp) != 3:
        return 1 
    # 입력값 타입 체크
    try:
        x = int(temp[1])
        y = int(temp[2])
        if x < 0 or y < 0:
            return 2 
    except ValueError:
        return 2
    # 이름 중복 체크
    for std in students:
        if temp[0] in std:
            return 3 
    return 4 # 유효성 검사 통과


#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        temp = input('Enter the name mid-score final-score : ').split()
        ck = isValid(temp,students)
        if ck == 1:
            print('Num of data is not 3!')
            continue
        elif ck == 2:
            print('Score is not positive integer!')
            continue
        elif ck == 3:
            print('Already exist name!')
        else:
            Menu1(temp)

    elif choice == "2" :
        if len(students):
            print('Grading to all students.')
            Menu2()
        else:
            print('No student data!')

    elif choice == "3" :
        if len(students):
            check = True
            for stud in students:
                if len(stud) != 4:
                    print('There is a student who didn\'t get grade.')
                    check = False
                    break
            if check:
                Menu3()
            else: 
                continue
        else:
            print('No student data!')

    elif choice == "4" :
        if len(students):
            find = False
            x = input('Enter the name to delete : ')
            for i in range(len(students)):
                if students[i][0] == x:
                    find = True
                    Menu4(i)
                    break
            if not find:
                print('Not exist name!')
                continue
        else:
            print('No student data!')

    elif choice == "5" :
        print('Exit Program!')
        break

    else :
        print('Wrong number. Choose again.')