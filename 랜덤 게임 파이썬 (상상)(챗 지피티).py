'''
import random as rd

a = rd.randint(1,100)

while True :
    b = int(input())
    if b > a :
        print("a가 더 작아요")
    elif b < a :
        print("a가 더 커요")
    else :
        print("와우!정답이에요!")
        break

name = input("이름을 입력하세요: ")
reversed_name = name[::-1]
print("결과:", reversed_name)

import random

secret = random.randint(1, 10)
chances = 3

while chances > 0:
    guess = int(input(">>>"))
    
    if guess == secret:
        print("정답입니다!")
        break
    else:
        chances -= 1
        print("틀렸습니다. 다시 시도하세요.")

if chances == 0:
    print("실패! 정답은", secret, "였습니다.")

n = input("숫자들을 입력하세요 (예: 5 10 3 8): ").split()

numbers = []
for i in n:
    numbers.append(int(i))

print("가장 큰 수는", max(numbers), "입니다.")
print("가장 작은 수는", min(numbers), "입니다.")

limit = int(input("숫자를 입력하세요: "))
n= 0

for i in range(1, limit + 1):
    if i % 2 == 0:
        n += i

print("짝수의 합은:", n)
'''
text = input("문자열을 입력하세요: ")
result = ""

for char in text :
    result = char + result

print("거꾸로 출력:", result)
