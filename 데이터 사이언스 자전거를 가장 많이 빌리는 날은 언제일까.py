import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv("train.csv",parse_dates = ["datetime"]) #"자료형을 날짜로 바꾸는 코드"
train.columns = ["날짜","계절","공휴일 유무","평일","날씨","섭씨 온도","체감온도","습도","풍속","비등록 사용자의 대여 횟수","등록 사용자의 대여 횟수","총 대여 횟수"]
train["연도"] = train["날짜"].dt.year
train["월"] = train["날짜"].dt.month
train["일"] = train["날짜"].dt.day
train["시"] = train["날짜"].dt.hour
train["분"] = train["날짜"].dt.minute
train["초"] = train["날짜"].dt.second
train["요일"] = train["날짜"].dt.dayofweek

plt.style.use("ggplot") #"그래프의 스타일을 바꾸는 함수"
plt.rc("font",family = "NanumGothic")
sns.barplot(data = train,x = "연도",y = "총 대여 횟수")
#sns.barplot(data = train,x = "월",y = "총 대여 횟수") /1
#sns.barplot(data = train,x = "일",y = "총 대여 횟수") /2
#plt.ylim(150,250) /2
#sns.barplot(data = train,x = "시",y = "총 대여 횟수") /3
#sns.pointplot(data = train,x = "시",y = "총 대여 횟수") /4
#sns.pointplot(data = train,x = "시",y = "총 대여 횟수",hue = "계절") /5
#sns.pointplot(data = train,x = "시",y = "총 대여 횟수",hue = "날씨") /6
#sns.pointplot(data = train,x = "시",y = "총 대여 횟수",hue = "공휴일 유무") /7
#sns.pointplot(data = train,x = "시",y = "총 대여 횟수",hue = "평일") /8

plt.show()



