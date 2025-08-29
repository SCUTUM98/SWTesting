# print('Hello World!')

# #fruit = input('과일을 입력하세요')
# #num = int(input('횟수 입력'))
# #print(fruit*num)

# # list = ['henry', 25, False]
# # list.append(170.5)
# # print(list[0])

# # t = ("henry", 25, 39.5)
# # print(t[1])


# id = "050101-3212123"

# if id[7] == '1' or id[7] == '3':
#     print('Male')
# elif id[7] == '2' or id[7] == '4':
#     print('Female')
# else:
#     print('WTF?')
    
# file = 'hello.py'

# splitName = file.split(sep='.')
# #print(splitName)

# if splitName[1] == 'py':
#     print('Python File')
# else:
#     print('Not Python')
    
    
# for i in range(1,11):
#     print(i, '마리 코끼리가 거미줄에 걸렸네')
    
    
# dan = input('단을 입력하세요: ')
# danInt = int(dan)

# for i in range(1,10):
#     print(f'{danInt} * {i} =', danInt * i)
    

# # 사용자한테 비밀번호 입력받기
# # 비밀번호가 같으면 성공 출력 후 종료
# # 비밀번호가 다르면 실패 출력 후 재 입력
# # 비밀번호 = 1234

# pw = '1234'


# while 1:
#     userInput = input("비밀번호를 입력해주세요.")
#     if userInput == pw:
#         print("PW Correct")
#         break
#     else:
#         print("PW Wrong. Try Again")
        

# def rect_area(x, y):
#     # print(f'사각형의 가로는 {x}cm 입니다.')
#     # print(f'사각형의 높이는 {y}cm 입니다.')
#     # print(f'사각형의 넓이는 {x * y} 입니다.')
#     result = x*y
#     return x, y, x*y
    
# x = input('가로 길이를 입력해주세요: ')
# y = input('높이를 입력해 주세요: ')
# weight, height, result = rect_area(int(x),int(y))

# print(f'사각형의 가로는 {weight}cm 입니다.')
# print(f'사각형의 높이는 {height}cm 입니다.')
# print(f'사각형의 넓이는 {result} 입니다.')


def div(a,b):
    if b == 0:
        raise ZeroDivisionError("Idiot")
    return a/b

a = int(input())
b = int(input())

result = div(a,b)
print(result)