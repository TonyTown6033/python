def move(a,b):
    print("%s ==> %s" %(a,b))
def hanoi(a,b,c,n):
    if n==1:
        move(a,c)
    else :
        hanoi(a,c,b,n-1)
        move(a,c)
        hanoi(b,a,c,n-1)
def main():
    n=input("pls input the disks of hanoi : ")
    n=eval(n)
    a="A"
    b="B"
    c="C"
    hanoi(a,b,c,n)

main()
