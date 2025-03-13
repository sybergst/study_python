# num = int(input())

# for i in range(num):
#     word =  input()
#     print(word[0]+word[-1])

# print(len(word))


# 아스키 코드로 병환하는 함수
# word =  input()
# print(ord(word))

num1 = int(input())
num2 = input()
sum = 0
for i in range(num1):
    sum += int(num2[i])
print(sum)