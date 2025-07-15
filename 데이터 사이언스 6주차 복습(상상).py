'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_html("https://ko.wikipedia.org/wiki/2021%EB%85%84_%EA%B0%80%EC%98%A8_%EB%94%94%EC%A7%80%ED%84%B8_%EC%B0%A8%ED%8A%B8_1%EC%9C%84_%EB%AA%A9%EB%A1%9D")

week = pd.DataFrame(df[0])
df_cnt = pd.DataFrame(week.가수.value_counts())
print(df_cnt)

plt.rc("font",family = "Malgun Gothic")
df_cnt.plot(title = "<<<노래 순위>>>",kind = "bar")
plt.show()
'''
import random as rd

scores = [
    {"이름": "지민", "점수": rd.randint(0,100)},
    {"이름": "민서", "점수": rd.randint(0,100)},
    {"이름": "서준", "점수": rd.randint(0,100)},
    {"이름": "하린", "점수": rd.randint(0,100)},
    {"이름": "도윤", "점수": rd.randint(0,100)},
    {"이름": "수아", "점수": rd.randint(0,100)}
]

total = 0
for student in scores:
    total += student["점수"]

average = total / len(scores)
print(f"1. 평균 점수: {average:.2f}점")

top_student = scores[0]
for student in scores:
    if student["점수"] > top_student["점수"]:
        top_student = student

print(f"2. 가장 높은 점수: {top_student['점수']}점 - {top_student['이름']}")

print("3. 60점 이상 받은 학생들:")
for student in scores:
    if student["점수"] >= 60:
        print(f"- {student['이름']} ({student['점수']}점)")
