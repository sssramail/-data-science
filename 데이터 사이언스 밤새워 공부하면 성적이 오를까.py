import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sleeping_hours.csv",encoding = "euc-kr",header = [0,1],index_col = [0,1])
df = df.T
df = df.rename_axis(index = ["연도","수면시간"])
#print(df["학업성적"].loc["2018","상"]) 1
#print(df["학업성적"].iloc[6:12,:3]) 1

#for i in range(0,7,6) : 2 
#    print(df["학업성적"].iloc[i:i+6,:3]) 2

times = ["5시간 미만","5~6시간","6~7시간","7~8시간","8~9시간","9시간 이상"]

high_2019 = df["학업성적"].loc["2019","상"]
middle_2019 = df["학업성적"].loc["2019","중"]
low_2019 = df["학업성적"].loc["2019","하"]


plt.rc("font",family = "Malgun Gothic")
plt.title("2019년 학업 성적별 수면 시간")
plt.plot(times,high_2019,label = "상",color = "skyblue")
plt.plot(times,middle_2019,label = "중",color = "yellow")
plt.plot(times,low_2019,label = "하",color = "green")
plt.legend()
plt.show()


high_2018 = df["학업성적"].loc["2018","상"]
middle_2018 = df["학업성적"].loc["2018","중"]
low_2018 = df["학업성적"].loc["2018","하"]


plt.rc("font",family = "Malgun Gothic")
plt.title("2018년 학업 성적별 수면 시간")
plt.plot(times,high_2018,label = "상",color = "skyblue")
plt.plot(times,middle_2018,label = "중",color = "yellow")
plt.plot(times,low_2018,label = "하",color = "green")
plt.legend()
plt.show()

