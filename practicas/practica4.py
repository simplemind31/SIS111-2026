primes=[]
criba=[False]*20001
for i in range(2,20000):
    if(not criba[i]):
        primes.append(i)
    for j in primes:
        if(i*j>20000):
            break
        criba[i*j]=True
        if(i%j==0):
            break
t=0
#2, 7, 5, 11, 3
while(t<1 or t>1000):
    t=int(input())
for case in range(t):
    n=0
    while(n<1 or n>2000):
        n=int(input())
    n-=1
    co=n//5
    re=n%5
    if(re==0 or re==2):
        print(primes[co*5+re])
    elif(re==1):
        print(primes[co*5+3])
    elif(re==3):
        print(primes[co*5+4])
    else:
        print(primes[co*5+1])
    