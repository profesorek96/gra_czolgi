import pgzrun

class Czolg:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.body=Actor("tankbody",(self.x,self.y))
        self.track=Actor("tanktrack",(self.x,self.y+50))
        self.turret=Actor("tankturret",(self.x+15,self.y-20),anchor=("left","bottom"))
    def draw(self):
        self.turret.draw()
        self.track.draw()
        self.body.draw()
    def prawo(self):
        self.body.x+=2
        self.track.x+=2
        self.turret.x+=2

    def lewo(self):
        self.body.x -= 2
        self.track.x -= 2
        self.turret.x -= 2
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

pgzrun.go()

