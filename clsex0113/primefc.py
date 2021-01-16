def prime(n):
  for i in range(2,n):
      if n % i ==0:
          return
  print(n)

def main():
    for i in range(1,100+1):
        prime(i)

main()
