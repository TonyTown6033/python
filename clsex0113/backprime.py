
for i in range(2,1000+1):
    flag=True
    for j in range(2,i):
        if i%j==0:
            flag=False
            continue
    if flag:
        h=i/100
        h=int(h)
        t=i%100
        t=t%10

        if h==t:
            print(i)
