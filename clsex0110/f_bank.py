def curExchange(mWorth):
#    mWorth = input('pls input the value and sign ($/¥)')
    if mWorth[-1] in ['$']:
        CNY=(eval(mWorth[0:-1]))*6.8833
        print('u could exchange ¥%.3f'%CNY)
    elif mWorth[-1] in ['¥']:
        USD=(eval(mWorth[0:-1]))*0.1452
        print('u could exchange $%.3f'%USD)
    else:
        print('input error')

    mWorth = input('pls input the value and sige($/¥)')
    curExchange(mWorth)
