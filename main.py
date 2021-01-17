print('대충 이름\n')
x = 4
while x < 5:
    print('Start: 1\nQuit: 2\nCredit: 3')
    start = int(input('>>'))
    if start == 1:
        x = 10
    elif start == 2:
        quit()
    elif start == 3:
        print('\n개발자: 안기겸\n\n')
        y = 10
        while y == 10:
            credit = input('exit을 입력하세요.\n>>\n')
            if credit == 'exit':
                x = 3
                y = 9
    else:
        print('잘못 입력된듯 합니다.')
