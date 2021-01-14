for i in range(1,10):
    print('    %d'%i,end='')
print()
print(20*'-')

for i in range(1,10) :
    print('%d'%i,end='')
    for j in range(1,i+1) :
        temp=i*j
        print('   %d'%temp,end='')
    print()
