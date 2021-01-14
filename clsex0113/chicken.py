#百钱百鸡
max1=100.0/5.0
max2=100.0/3.0
max3=100.0/1.0
money=100.0
chick=100.0
# i for m-chick j for fema-chick k for child-chick
for i in range(1,int(max1)+1):
    for j in range(1,int(max2)+1):
        for k in range(3,int(max3)+1,3):
            temp1=i+j+k
            temp2=i*5+j*3+k/3
            if temp1==100 and temp2==100:
                print('the best solution is m-chick:%d fe-chick:%d child-chicken:%d '%(i,j,k))
