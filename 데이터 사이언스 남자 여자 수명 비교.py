import pandas as pd

df = pd.read_html("https://ko.wikipedia.org/wiki/%EA%B8%B0%EB%8C%80%EC%88%98%EB%AA%85%EC%88%9C_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D")[1]

df_m_avg = df["남성"].mean() 
df_w_avg = df["여성"].mean()

print("Men : %.2f" %df_m_avg)
print("Women : %.2f" %df_w_avg)

difference = abs(df_m_avg - df_w_avg)

if df_m_avg > df_w_avg :
    gender1,gender2 = "men","women"
else :
    gender1,gender2 = "women","men"

print("On average, %s live %.2f years longer than %s." %(gender1,difference,gender2))




