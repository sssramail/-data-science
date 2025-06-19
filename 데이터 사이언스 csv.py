import csv
import matplotlib.pyplot as plt

f = open("sns_use.csv",encoding = "euc-kr")
data = csv.reader(f)

next(data)
next(data)

year = [2016,2017,2018]
facebook = []
kakao = []
insta = []

for row in data :
    facebook.append(float(row[2]))
    kakao.append(float(row[3]))
    insta.append(float(row[4]))

#print(facebook)  /2

#next(data)  /1
#header = next(data)  /1
#print(header)  /1

#for row in data : /1
#    print(row)  /1

f.close()

plt.title("SNS Occupancy ratio")
plt.plot(year,facebook,label = "facebook",color = "blue")
plt.plot(year,kakao,label = "kakao",color = "brown")
plt.plot(year,insta,label = "insta",color = "pink")
plt.legend()
plt.show()
