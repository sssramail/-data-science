import pandas as pd

df = pd.read_html("https://ko.wikipedia.org/wiki/%EA%B8%B0%EB%8C%80%EC%88%98%EB%AA%85%EC%88%9C_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D")[1]
#print(df.index)
#RangeIndex(start=0, stop=201, step=1)
#print(df.columns)
#Index(['순위', '국가/영토', '전체', '남성', '여성'], dtype='object')
#print(df.sort_values(by = "남성",ascending = False).head(5)) 
#print(df.sort_values(by = "여성",ascending = False).head(5)) 
#print(df.sort_values(by = "전체",ascending = False).head(5)) 

df_m_avg = df["남성"].mean() #평균 구하는 함수 mean()
df_w_avg = df["여성"].mean()

#평균값 출력
print("Men : %.2f" %df_m_avg)
print("Women : %.2f" %df_w_avg)

#평균값의 차 구하기
difference = abs(df_m_avg - df_w_avg)

#평균수명이 더 긴 성별을 판단하기
if df_m_avg > df_w_avg :
    gender1,gender2 = "men","women"
else :
    gender1,gender2 = "women","men"

#결과 출력하기
print("On average, %s live %.2f years longer than %s." %(gender1,difference,gender2))
