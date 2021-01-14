import random
player1=0
player2=0
rates1=0
rates2=0
count=0
while True:

    if count==50:
        break
    rates1=0
    rates2=0
    for i in range(1,6):
        rates1=rates1+random.randint(1,6)
        rates2=rates2+random.randint(1,6)

    if rates1 > rates2:
        player1=player1+1
    elif rates1 < rates2:
        player2=player2+1
    count=count+1
if player1 > player2:
    print('player1 is winner')
elif player1 < player2:
    print('player2 is winner')
else:
    print('peace end')
