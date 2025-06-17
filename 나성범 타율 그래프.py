import matplotlib.pyplot as plt

f = open("sss.txt","r",encoding = "utf-8")
book = f.readlines()
duseh = ["2022","2023","2024"]
avg = []

for i in book :
    avg.append(float(i))

f.close()

plt.rc("font",family = "Malgun Gothic")
plt.title("나성범 연도별 타율")
plt.xlabel("연도")
plt.ylabel("타율")
plt.plot(duseh,avg)
plt.show()

