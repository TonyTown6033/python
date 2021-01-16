from turtle import *
from datetime import *
def skip(step):
    penup()
    forward(step)
    pendown()

def setup_clock(radius):
    reset()
    pensize(7)
    for i in range(60):
        skip(radius)
        if i%5==0:
            forward(20)
            skip(-radius-20)
        else:
            dot(5)
            skip(-radius)
        right(6)
def make_hand(name,length):
    reset()
    skip(-0.1*length)
    begin_poly()
    forward(1.1*length)
    end_poly()
    handForm=get_poly()
    register_shape(name,handForm)

def init():
    global secHand,minHand,hurHand,printer
    mode("logo")
    secHand=Turtle()
    make_hand("secHand",130)
    secHand.shape("secHand")
    minHand=Turtle()
    make_hand("minHand",125)
    minHand.shape("minHand")
    hurHand=Turtle()
    make_hand("hurHand",90)
    hurHand.shape("hurHand")
    for hand in secHand,minHand,hurHand:
        hand.shapesize(1,1,3)
        hand.speed(0)
    printer = Turtle()
    printer.hideturtle()
    printer.penup()

def week(t):
    week = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
    return week[t.weekday()]

def day(t):
    return "%s %d %d" %(t.year,t.month,t.day)

def tick():
    t=datetime.today()
    second= t.second+t.microsecond*0.000001
    minute= t.minute+t.second/60.0
    hour= t.hour+t.minute/60.0

    secHand.setheading(second*6)
    minHand.setheading(minute*6)
    hurHand.setheading(hour*30)

    tracer(False)
    printer.fd(70)

    printer.write(week(t),align="center",font=("Courier",14,'bold'))
    printer.back(130)
    printer.write(day(t),align='center',font=("Courier",14,"bold"))
    printer.home()
    tracer(True)
    ontimer(tick,100)

def main():
    tracer(False)
    init()
    setup_clock(200)
    tracer(True)
    tick()
    done()

main()
