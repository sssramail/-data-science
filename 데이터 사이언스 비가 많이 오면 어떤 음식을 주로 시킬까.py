import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc("font",family = "Malgun Gothic",size = 25)

call_df = pd.read_csv("Calldata_2008.csv",encoding = "utf-8",parse_dates = ["일자(YYYYMMDD)"])
rain_df = pd.read_csv("Raindata_2008.csv",encoding = "cp949",parse_dates = ["일시"])

call_df.columns = ["일자","연령","성별","발신지1","발신지2","대분류","중분류","통화비율"]
rain_df.columns = ["지점번호","지점명","일자","강수량","1시간최대강수량","1시간최대강수량시각"]
#print(call_df)
#print(rain_df)

#조건을 만족하는 데이터 추출
is_ture = (call_df["발신지1"] == "서울") & (call_df["대분류"] == "음식점")
call_df = call_df[is_ture]
#print(call_df)

#필요없는 부분 드랍 함수로 삭제
call_df = call_df.drop(columns = ["연령","성별","발신지1","발신지2","통화비율","대분류"])
print(call_df)

rain_df = rain_df.drop(columns = ["지점번호","지점명","1시간최대강수량","1시간최대강수량시각",])
#print(rain_df)

#널문자 지우기
rain_df["강수량"] = rain_df["강수량"].fillna(0)
#print(rain_df)

#강수량 데이터와 콜 데이터 합치기
tot_df = pd.merge(call_df,rain_df,on = "일자")
#print(tot_df)

#강수량이 0인 날짜를 표로 나타내기
no_rain = tot_df[tot_df["강수량"] == 0]
no_rain = pd.DataFrame(no_rain["중분류"].value_counts())
#print(no_rain)

#강수량이 40이상인 날짜를 표로 나타내기
yes_rain = tot_df[tot_df["강수량"] >= 40]
yes_rain = pd.DataFrame(yes_rain["중분류"].value_counts())
#print(yes_rain)

#그래프 그리기

figure, (ax1,ax2) = plt.subplots(ncols = 2)

#그래프 세트 만들기
figure.set_size_inches(40,15)

#no_rain.columns = ["중분류"]

color1 = ["royalblue","crimson","orange","forestgreen","chocolate","tomato"]

color2 = ["royalblue","orange","crimson","forestgreen","tomato","chocolate"]



#plt.rcParams["figure.figsize"] = (20,15)
#no_rain.plot.pie(y = "중분류",autopct = "%.2f",colors = color)

no_rain.plot.pie(autopct = "%.2f",subplots = True,ax = ax1,colors = color1)
yes_rain.plot.pie(autopct = "%.2f",subplots = True,ax = ax2,colors = color2)

ax1.set(title = "비 안 오는 날")
ax2.set(title = "비 많이 오는 날")

plt.show()
