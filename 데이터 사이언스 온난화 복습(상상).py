import pandas as pd
'''
df = pd.read_csv("과일.csv",encoding = "euc-kr")
print(df["수량"].idxmax(),df["수량"].idxmin())
df.loc[df["수량"].idxmax()]

df = pd.read_csv("과일.csv",encoding = "euc-kr")
df.columns = ["name","amount","price","totle"]
df.columns
'''
import matplotlib.pyplot as plt

df = pd.read_csv("seoul.csv",encoding = "euc-kr")

df.columns = ["년월","평균기온","최저기온","최고기온"]

df2 = df[df["년월"].str.contains(" 1월")]
df3 = df[df["년월"].str.contains(" 8월")]

plt.rc("font",family = "Malgun Gothic")
plt.rcParams["axes.unicode_minus"] = False
df2.plot(x = "년월",y = "평균기온",color = "blue")
df3.plot(x = "년월",y = "평균기온",color = "red")
plt.show()
