# num = int(input())

# for i in range(num):
#     word =  input()
#     print(word[0]+word[-1])

# print(len(word))


# 아스키 코드로 변환하는 함수
# word =  input()
# print(ord(word))

#chr() 함수를 통해 아스키코드를 문자로 바꿀 수 있다.

# num1 = int(input())
# num2 = input()
# sum = 0
# for i in range(num1):
#     sum += int(num2[i])
# print(sum)

# 단어에 들어간 알파벳 개수 찾기 실패
# word = input()
# num_len = len(word)

# for j in range(26):
#     count = -1
#     for i in range(num_len):
#         if word[i] == chr(j + 97):
#             count += 1
#     print(count , end=" ")

#단어에 들어간 알파벳 위치 찾기
# word = input()
# num_len = len(word)

# for j in range(26):
#     for i in range(num_len):
#         spot = word.find(chr(j+97))
#     print(spot, end=" ")

# 문자열 반복

# num = int(input())

# for i in range(num):
#     R, S = input().split()
#     R = int(R)
#     count = len(S)
#     for j in range(count):
#         print(S[j]*R, end="")
#     print("")

# 다이얼

# ring = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
# word = input()
# lenth = len(word)
# time = 0
# for i in range(lenth):
#     for j in range(8):
#         ans = ring[j].find(word[i])
#         if ans == -1:
#             continue
#         else:
#             time += j + 3
# print(time)

#그대로 출력하기
# while 1:
#     try:
#         word = input()
#         print(word)
#     except:
#         break

#올바른 체스말 개수 구하기
# co_chess = [1, 1, 2, 2, 2, 8]
# now_chess = list(map(int, input().split(" ")))
# ans = []

# for i in range(6):
#     ans.append(co_chess[i] - now_chess[i])
# print(*ans, sep=" ")

#문장속 단어의 개수 찾기
# words = input().split(" ")
# a = len(words)
# b = words.count("")
# print(a-b)


#x보다 작은 수 찾기
# a, b = map(int, input().split(" "))
# num = list(map(int, input().split(" ")))
# ans = []
# for i in range(a):
#     if b > num[i]:
#         ans.append(num[i])
# print(*ans, sep=" ")

#ox퀴즈 점수내기
# count = int(input())
# ans = ""

# for i in range(count):
#     bb = 0
#     point = 1
#     ans = input()
#     for j in range(len(ans)):
#         if ans[j] == "O":
#             bb += point
#             point += 1
#         elif ans[j] == "X":
#             point = 1
#     print(bb)

#호텔 호수 구하기
# test = int(input())
# for i in range(test):
#     H, W, N = map(int, input().split(" "))
#     loc = [0, 1]
#     for j in range(N):
#         if loc[0] == H:
#             loc[0] = 1
#             loc[1] += 1
#         else:
#             loc[0] += 1

#     if loc[1] < 10:
#         print(str(loc[0]) + "0" + str(loc[1]))
#     else:
#         print(str(loc[0]) + str(loc[1]))

#다이아몬드 그리기
# num = int(input())
# star = 0
# for i in range(num*2-1):
#     if i < num:
#         star = 1 + 2*i
#         st = "{0:^{1}}".format("*"*star,num*2-1)
#         print(st.rstrip())
#     else:
#         star = num*2-1 - 2*(i - num + 1)
#         st = "{0:^{1}}".format("*"*star,num*2-1)
#         print(st.rstrip())

#중복된 문자의 개수 찾기
# word = input()
# word = word.upper()
# # word = list(word)
# # word.sort()
# many = []
# count = word.count(chr(65))
# many.append(chr(65))

# for i in range(1, 26):
#     a = word.count(chr(65 + i))
#     if a > count:
#         many = []
#         count = a
#         many.append(chr(65 + i))
#     elif a < count:
#         pass
#     else:
#         many.append(chr(65 + i))

# if len(many) == 1:
#     print(many[0])
# else:
#     print("?")


#거듭제곱의 일의자리
# ro = [[0], [1], [2, 4, 8, 6],[3, 9, 7, 1],[4, 6],[5],[6],[7, 9, 3, 1],[8, 4, 2, 6],[9, 1]]

# T = int(input())

# for i in range(T):
#     a, b = map(int, input().split(" "))
#     last_a = a % 10
#     if last_a == 5 or last_a == 6:
#         print(last_a)
#     elif last_a == 0:
#         print(10)
#     else:
#         if b % len(ro[last_a]) == 0:
#             print(ro[last_a][-1])
#         else:
#             print(ro[last_a][b % len(ro[last_a]) - 1])

#1052번을 풀어보려는 똥꼬쇼
# N, K =  map(int, input().split())
# count = 0
# li = []
# if N == 1:
#     print(1)
# else:
#     while True:
#         a = 2
#         while True:
#             if a >= N:
#                 a = a // 2
#                 break
#             a = a * 2
#         li.append(a)
#         N -= a
#         if N <= 2:
#             li.append(N)
#             break
              
# if len(li) <= K:
#     print(0)
# else:
#     while len(li) > K:
#         if li[-1] == li[-2]:
#             li.pop()
#             li.append(li.pop()*2)
#         else:
#            li.append(li[-1])
#            count += li[-1]
#     print(count)

# N, K =  map(int, input().split())
# count = 0

# while bin(N).count('1') > K:
#     count += 1
#     N += 1
# print(count)
# import math

# case = int(input())
# for i in range(case):
#     N, M = map(int, input().split())
#     print(math.factorial(M) // (math.factorial(N) * math.factorial(M - N)))

case = int(input())
ans = 0
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
b.reverse()
for i in range(case):
    ans += a[i] * b[i]
print(ans)