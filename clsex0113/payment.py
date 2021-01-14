base=2000
sell=input('pls input  the sale val: ')
sell=eval(sell)
if sell <=3000:
    rate=0.0
elif sell > 3000 and sell <= 7000:
    rate=0.1
elif sell > 7000 and sell <= 10000:
    rate=0.15
elif sell > 10000 :
    rate=0.2

payment=(base+sell)*(1+rate)
print(payment)
