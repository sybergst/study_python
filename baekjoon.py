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

count = int(input())
ans = ""

for i in range(count):
    bb = 0
    point = 1
    ans = input()
    for j in range(len(ans)):
        if ans[j] == "O":
            bb += point
            point += 1
        elif ans[j] == "X":
            point = 1
    print(bb)


