#import matplotlib.pyplot as plt

#f = open("Alice.txt","r",encoding = "utf-8")
#book = f.read()
#print(book)
#words = input("검색하려고 하는 단어를 5개 입력해 주세요 : ")

#words = words.split()
#words = []

#words = input("검색하려고 하는 단어를 5개 입력해 주세요 :")
#words = words.split()
#cnt = []

#for word in words :
#    n = book.count(word)
#    cnt.append(n)

#for _ in range(5) :
#    words.append(input())

#for word in words :
#    n = book.count(word)
#    print("%s : %d개"%(word,n))

#f.close()

#plt.rc("font",family = "Malgun Gothic")
#plt.title("단어 개수")
#plt.plot(words,cnt)
#plt.xlabel("검색 단어")
#plt.ylabel("단어 개수")
#plt.bar(words,cnt)
#plt.show()

import matplotlib.pyplot as plt

f = open("practice.txt","r",encoding = "utf-8")
book = f.readlines()
duseh = ["2017","2018","2019","2020","2021","2022","2023","2024"]
avg = []

for i in book :
    avg.append(float(i))

f.close()

plt.rc("font",family = "Malgun Gothic")
plt.title("최형우 연도별 타율")
plt.xlabel("연도")
plt.ylabel("타율")
plt.plot(duseh,avg)
plt.show()
