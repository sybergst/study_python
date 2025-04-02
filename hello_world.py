# print("{0:.>30}".format("understand?"))

# y = 3.421534352
# print("{0:0.4f}".format(y))

# name = "홍길동"
# age = 19
# print(f"나의 이름은 {name}이고 나이는 {age}입니다.")

# 리스트는 어떤 지료형도 구성 요소로 받을 수 있다.
# a = [1, 2, 3, 4, [1, 2, 3]]
# print(a[0] + a[3])
# print(a[-1])
# print(a[-1][2])

# print("\n{0:=>10}".format("분리선\n"))

#리스트의 슬라이싱 기법
# print(a[0:3])

# a.clear
# a = [1, 2, 3]
# b = [2, 3, 4]
# print(a+b)
# print(a*3)
# print(len(a))

# del a[2]
# print("리스트a 의 3변째 요소값이 삭제됨")
# print(a)
# print("다시 3번째 요소 자리에 4가 들어감")
# a.append(4)
# print(a)

# sort함수는 리스트의 요소를 순서대로 정렬해준다.
# a.clear()
# a = [3, 2, 4, 1]
# a.sort()
# print(a)

#딕셔너리 다료형
# dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

# 딕셔너리 추가
# dic[1] = "hello"
# print(dic)
# del dic[1]
# print(dic)
# b = dic.keys()
# print(b)

# for문 활용
# a = [1, 2, 3, 4]
# b = [num * 2 for num in a]
# print(b)

#파일 활용
# f = open("/workspaces/study_python/new_file.txt", "w")
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# f = open("/workspaces/study_python/new_file.txt", "r")

# line = f.readlines()
# print(line)
# f.close()

# f = open("/workspaces/study_python/new_file.txt",'a')
# for i in range(11, 20):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

#class제작
# class FourCal:
#     def __self__(self, first, second):
#         self.first = first
#         self.second = second
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#          result = self.first * self.second
#          return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result

# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result

#메서드 오버라이딩
# class SafeFourCal(FourCal):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first / self.second

# 모듈을 불러올 시 의도치 않은 실행 방지
# if __name__ == "__main__":

# class MyError(Exception):
#     def __str__(self): # 오류 메시지를 출력하는 경우 호출되는 method
#         return "허용되지 않는 별명입니다."

# def say_nick(nick):
#     if nick == '바보':
#         raise MyError()
#     print(nick)

# try:
#     say_nick("천사")
#     say_nick("바보")
# except MyError as e:
#     print(e)

