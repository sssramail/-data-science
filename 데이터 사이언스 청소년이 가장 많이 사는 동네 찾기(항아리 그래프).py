import csv
import matplotlib.pyplot as plt

f = open("person.csv",encoding = "euc-kr")
data = csv.reader(f)
next(data)

men = []
women = []
area = input("동 단위로 검색 : ")

for row in data :
    row[1: ] = map(int,row[1: ])
    if area in row[0] :
        for i in range(3,64) :
            men.append(row[i]*-1)
            women.append(row[i+63])
        break

f.close()

plt.rc("font",family = "Malgun Gothic")
plt.rcParams["axes.unicode_minus"] = False
plt.title("%s 남녀 인구수"%area)
plt.barh(range(61),men, color = "green",label = "남자")
plt.barh(range(61),women,color = "orange",label = "여자")
plt.legend()
plt.show()
