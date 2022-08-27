from datetime import datetime
import turtle as t
from time import sleep

def marcas(t, posx, posy, raio):
    t.pu()
    t.goto(posx, posy)
    for i in range(60):
        if i % 5==0:
            d=0.2
            w=3
        else:
            d=0.1
            w=2
        t.fd(raio*(1-d))
        t.pd()
        t.width(w)
        t.fd(raio*d)
        t.pu()
        t.bk(raio)
        t.rt(6)

def ponteiro(t,posx,posy, raio, ang, width, color):
    t.pu()
    t.goto(posx,posy)
    t.color(color)
    t.width(width)
    t.seth(90-ang)
    t.pd()
    t.fd(raio)

t.tracer(0)

x=0
y=0
r=300

while True:
    now=datetime.now()
    s_ang=now.second*6+now.microsecond/1000000*6
    m_ang=now.minute*6+now.second*0.1
    h_ang=now.hour*30+now.minute*0.5
    t.reset()
    #fundo
    marcas(t,x,y,r)
    #segundos
    ponteiro(t,x,y,r,s_ang,2,'red')
    ponteiro(t,x,y,r,m_ang,10,'black')
    ponteiro(t,x,y,r*0.7,h_ang,10,'black')
    t.update()
    sleep(1/30)