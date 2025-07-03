import csv
import matplotlib.pyplot as plt

f = open("accident.csv",encoding = "cp949")
data = csv.reader(f)

next(data)
#i,j = 0,0 //1
#days = [] //1
#days_sum = [0] * 7 //1
i = 0
road_type = []
number = []

for row in data :
    row[2:] = map(int,row[2:])
    #days_sum[i % 7] += row[2] //1
    if i % 7 == 5 :
        road_type.append(row[0])
        number.append(row[2])
    i += 1
    #if j < 7 : //1
        #days.append(row[1]) //1
        #j += 1 //1

plt.rc("font",family = "Malgun Gothic")
#plt.title("요일별 교통사고 발생 수") //1
#plt.bar(days,days_sum) //1
#plt.title("금요일 도로종류별 사고 건수") //2
#plt.bar(road_type,number) //2
#plt.xticks(rotation = 30) //2
plt.title("금요일 교통사고 건수 비율")
plt.pie(number,labels = road_type,autopct = "%.1f%%")

plt.show()

f.close()
