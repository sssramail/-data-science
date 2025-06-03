#a = "Carpe Diem!"
#print(a[6:11])

#a = "Carpe Diem!"
#print(a[6:])

#a = [10,20,30,40,50]
#print(a[0])
#b = [10,20,[30,40],50]
#print(b[2])
#print(b[2][0])
#print(b[2][1])

#a = [10,20,30,40,50]
#print(a[1:4])

#a = [1,2,'a','b',3,4,'c']
#print(a[5])
#print(a[0:2])
#print(a[4:-1])
#print(a[0]+a[1])
#print(a[2]+a[3]+a[6])

#a = [10,20,30,40,50]
#a[0] = 'a'
#print(a)
#a[1:3] = 'b'
#print(a)

#a = [1,5,3,10]
#a.append(20)
#print(a)
#a.sort()
#print(a)
#a = ['b','a','n','a','n','a']
#a.reverse()
#print(a)
#a.remove('a')
#print(a)
#p = a.pop()
#print(p,a)
#n = a.count('n')
#print(n)

#a = {'a' : 1,'b' : 2,'c' : 3,'d' : 4}
#print(a.keys())
#print(a.values())
#print(a.items())
#print(a)

#a = set([1,2,3])
#a.add(4)
#print(a)
#a.update('abc')
#print(a)
#a.remove('c')
#print(a)

#a = set('abc')
#a.update('abcde')
#print(a)

#score = 80
#if score >= 60 and score <= 100 :
#    print("Pass")
#else :
#    print("Fail")

#a = 1 in [1,2,3]
#print(a)

#a = 1 not in [1,2,3]
#print(a)

#case = ['Homwork','Eating','Sleeping']

#if 'Homwork' in case :
#    print("I have to do Honwork.")
#else :
#    print("It's break time.")

def two_times():
    for i in range(1,10) :
        print("2 * %d = %d\n"%(i,2 * i) , end = ' ')
two_times()
