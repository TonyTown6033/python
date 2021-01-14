for i in range(100,1000):
    t1=int(i/100)
    t2=int((i-t1*100)/10)
    t3=int(i-t1*100-t2*10)
    #print(i,t1,t2,t3)
    if t1**3+t2**3+t3**3==i:
        print(i)
