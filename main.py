import pgzrun
import math
class Pocisk:
    def __init__(self,x,y,kat):
        self.x=x
        self.y=y
        self.kat=kat
        self.pocisk=Actor("bullet",(self.x,self.y))
        self.pocisk.angle=kat
    def draw(self):
        self.pocisk.draw()
    def update(self):
        self.pocisk.x+=4
        self.pocisk.y-=math.tan(math.radians(self.kat))*4

class Wyrzutnia:
    def __init__(self):
        self.pociski=[]
        self.blokada_strzalu=False
    def zwolnienie_blokady(self):
        self.blokada_strzalu=False
    def wystrzel(self,kat,x,y):
        if(self.blokada_strzalu==False):
            self.pociski.append(Pocisk(x,y,kat))
            self.blokada_strzalu=True
            clock.schedule_unique(self.zwolnienie_blokady,1.0)
    def draw(self):
        for i in self.pociski:
            i.draw()
    def update(self):
        tmp=[]
        for i in self.pociski:
            if i.x<800 and i.y>0:
                tmp.append(i)
        self.pociski=tmp
        for i in self.pociski:
            i.update()




class Czolg:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.body=Actor("tankbody",(self.x,self.y))
        self.track=Actor("tanktrack",(self.x,self.y+50))
        self.turret=Actor("tankturret",(self.x+15,self.y-20),anchor=("left","bottom"))
        self.wyrzutnia=Wyrzutnia()
    def draw(self):
        self.turret.draw()
        self.track.draw()
        self.body.draw()
        self.wyrzutnia.draw()
    def prawo(self):
        self.body.x+=2
        self.track.x+=2
        self.turret.x+=2
        self.wyrzutnia.x+=2

    def lewo(self):
        self.body.x -= 2
        self.track.x -= 2
        self.turret.x -= 2
        self.wyrzutnia.x-=2
    def turretup(self):
        if self.turret.angle>=0 and self.turret.angle<=80:
            self.turret.angle+=2
        if self.turret.angle>80:
            self.turret.angle=80
    def turretdown(self):
        if self.turret.angle>=0 and self.turret.angle<=80:
            self.turret.angle-=2
        if self.turret.angle<0:
            self.turret.angle=0
    def wystrzel(self):
        self.wyrzutnia.wystrzel(self.turret.angle,self.turret.x,self.turret.y)
    def update(self):
        self.wyrzutnia.update()
czolg=Czolg(200,456)

def draw():
    screen.clear()
    screen.fill("#66e6ff")
    for i in range(13):
        screen.blit("grass",(i*64,536))
    czolg.draw()


def update():
    if keyboard.RIGHT:
        czolg.prawo()
    if keyboard.LEFT:
        czolg.lewo()
    if keyboard.UP:
        czolg.turretup()
    if keyboard.DOWN:
        czolg.turretdown()
    if keyboard.SPACE:
        czolg.wystrzel()
    czolg.update()

pgzrun.go()

