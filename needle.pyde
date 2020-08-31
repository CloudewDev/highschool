from random import *

class Needle :
    
    def __init__ (self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        
    def display (self):
        stroke(0)
        rotate(radians(self.r))
        line(self.x, self.y, self.x, self.y-needleLength)
        circle(self.x, self.y, 3)
        
        
    def collideCheck(self):
        #circle(self.x + needleLength, self.y + needleLength, 3)
        global colneedle
        for i in range(0, 9):
            if abs((i*leak) - (self.y+(needleLength/2))) <= (leak/2)*sin(radians(abs(self.r))):
                colneedle += 1
    
    def howMuchPi(self):
        global piAssume, needleCnt, colneedle
        if colneedle == 0:
            piAssume = 0
        else:
            piAssume = (2*needleCnt)/colneedle
        
        
        


needleLength = 100
leak = 100
w= 1200
h = 800
f= 0
needleCnt = 0.00000000
needles = []
colneedle = 0.000000
piAssume = 0

def setup():
    global w, h, f, needleCnt
    PFont = f
    f = loadFont("NanumGothicExtraBold-40.vlw")
    size(w, h)
    textFont(f,20)
    needle = Needle(uniform(0, 1200), uniform(0, 800), uniform(-180, 180))
    needles.append(needle)
    needleCnt += 1
    
def draw():
    global needleCnt, colneedle
    background(230)
    fill(0)
    stroke(255)
    text("pi = %f" %piAssume, 30, 20)
    text("number of dropped needle : %d" % needleCnt,30, 60)
    text("needle met with line count : %d" % colneedle, 30, 100)
    
    for i in range(0, 9):
        stroke(0)
        line(0, i*leak, w, i*leak)

        
    if keyPressed == False:
        needle = Needle(uniform(0, 1200), uniform(0, 800), uniform(-180, 180))
        #print(needle.x, needle.y, needle.r)
        needles.append(needle)
        needleCnt += 1
        needle.collideCheck()
        needle.howMuchPi()
        
            
    for needle in needles:
        needle.display()
        
    
