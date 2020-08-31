#damn i cant write korean 
import random
import math
import operator



class Person ():
    def __init__(self, x, y, dx, dy, id, maskFrequency=int(0), disFrequency=int(0)):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.stat = 0
        self.id = id
        self.maskWear = 1
        self.maskFrequency = maskFrequency
        self.disFrequency = disFrequency
        self.score = 0
        
    def generator(self):
        
        for a in range(0, len(people)):
            if self != people[a]:
                person = people[a]
            
                d = sqrt((self.x - person.x)**2 + (self.y - person.y)**2)
            
                if d < 80:
                    while d<80:
                        self.x = random.randrange(0, w-70)
                        self.y = random.randrange(0, h-70)
                        d = sqrt((self.x - person.x)**2 + (self.y - person.y)**2)
            else:
                pass
        
    def display (self):
        if self.stat == 1 :
            fill(255, 40, 40)
        else :
            fill(6, 215, 28)
        noStroke()
        ellipseMode(CENTER)
        ellipse(self.x, self.y, 40, 40)
        
        stroke(0)
        noFill()
        ellipse(self.x, self.y, 60, 60)
        
        if self.maskWear == 1:
            fill(200)
            rectMode(CENTER)
            noStroke()
            rect(self.x , self.y+10 , 40, 20)
        
        
        fill(0)
        textSize(12)
        textAlign(CENTER)
        text(self.id, self.x, self.y)
        
        
        if self.x < 0 or self.x > w:
            self.dx = self.dx * -1
            
        if self.y < 0 or self.y > h:
            self.dy = self.dy * -1
        
        self.x = self.x+self.dx
        self.y = self.y+self.dy
    
    def collidecheck(self):
        for a in range(self.id+1, len(people)):
            person = people[a]
            
            d = sqrt((self.x - person.x)**2 + (self.y - person.y)**2)
            
            if d < 20 and random.random() < infectP:
                #print("distance is under 30")
                #print(self.id, self.stat)
                #print(person.id, person.stat)
                
                if self.stat == 0 and person.stat == 1 :
                    if self.maskWear == 0 and person.maskWear == 0:
                        self.stat = 1
                    elif self.maskWear == 1 and person.maskWear == 0 and random.random() < 0.15:
                        self.stat = 1
                    #print("infection occured")
                
                elif self.stat == 1 and person.stat == 0:
                    if self.maskWear == 0 and person.maskWear == 0:
                        person.stat = 1
                    elif self.maskWear == 0 and person.maskWear == 1 and random.random() < 0.15:
                        person.stat = 1
                    #print("infection occured")
    '''  
    def socialDistance(self):
        for a in range(self.id+1, len(people)):
            person = people[a]
            
            d = sqrt((self.x - person.x)**2 + (self.y - person.y)**2) 
            
            if d < 70:
                x_delta = math.fabs(self.x-person.x)
                y_delta = math.fabs(self.y-person.y)
                
                angle1 = math.atan2(x_delta, -(y_delta))
                angle2 = math.atan2(-(x_delta), y_delta)
                
                
                v1 = 1
                v2 = 1
                
                v0 = sqrt(self.dx**2 + self.dy**2)
                
                print(v1)
                print(v2)
                
                interAngle1 = math.asin((self.dx*sin(angle1) - self.dy*cos(angle1))/(v0+v1))
                interAngle2 = math.asin((self.dx*sin(angle2) - self.dy*cos(angle2))/(v0+v2))
                
                
                if (cos(angle1) * self.dx + sin(angle1) * self.dy) /(v1 * v0) > (cos(angle2) * self.dx + sin(angle2) * self.dy) / (v2 * v0):
                    self.dx = self.dx * cos(interAngle1) - self.dy * sin(interAngle1)
                    self.dy = self.dx * sin(interAngle1) + self.dy * cos(interAngle1)
                    
                else : 
                    self.dx = self.dx * cos(interAngle2) - self.dy * sin(interAngle2)
                    self.dy = self.dx * sin(interAngle2) + self.dy * cos(interAngle2)
                    
            if d < 70 :
                
                x_delta = math.fabs(person.x-self.x)
                y_delta = math.fabs(person.y-self.y)
                
                angle1 = math.atan2(x_delta, -(y_delta))
                angle2 = math.atan2(-(x_delta), y_delta)
                
                v1 = 1
                v2 = 1
                
                v0 = sqrt(person.dx**2 + person.dy**2)
                
                interAngle1 = math.asin((person.dx*sin(angle1) - person.dy*cos(angle1))/(v0+v1))
                interAngle2 = math.asin((person.dx*sin(angle2) - person.dy*cos(angle2))/(v0+v2))
                
                if (cos(angle1) * person.dx + sin(angle1) * person.dy) /(v1 * v0) > (cos(angle2) * person.dx + sin(angle2) * person.dy) / (v2 * v0):
                    person.dx = person.dx * cos(interAngle1) - person.dy * sin(interAngle1)
                    person.dy = person.dx * sin(interAngle1) + person.dy * cos(interAngle1)
                    
                else : 
                    person.dx = person.dx * cos(interAngle2) - person.dy * sin(interAngle2)
                    person.dy = person.dx * sin(interAngle2) + person.dy * cos(interAngle2)
            
        '''
        
        
    def socialDistance(self):
        for a in range(self.id+1, len(people)):
            person = people[a]
            
            d = sqrt((self.x - person.x)**2 + (self.y - person.y)**2) 
            
            if d < 65 and d > 63 and random.random() < self.disFrequency:
                if random.random() > 0.5:
                    self.dx = self.dx * -1
                else:
                    self.dy = self.dy * -1
                
            if d < 65 and d > 63 and random.random() < person.disFrequency :
                if random.random() > 0.5:
                    person.dx = person.dx * -1
                else:
                    person.dy = person.dy * -1 
                
    def isMaskWearing(self):
        
        if random.random() < self.maskFrequency:
            self.maskWear = 1
        else : 
            self.maskWear = 0
            
    def scoreCheck(self) :
        if self.stat == 0:
            self.score = self.score+1
        
        
    def geneManager(self) :
        n_infected = 0
        for person in people :
            if person.stat == 1:
                n_infected = n_infected + 1
        if n_infected == len(people)-1:
            person.childMaker()
            
               
    def childMaker(self):
        sorted_people = sorted(people, key=operator.attrgetter('score'), reverse = True)
        random.shuffle(people)
        shuffled_people = people
        
        global bestMaskFreq, bestDisFreq
        bestMaskFreq = sorted_people[0].maskFrequency
        bestDisFreq = sorted_people[0].disFrequency
        
        del people[0:]
        for i in range(0, n_people):
            person = Person(random.randrange(0, w), random.randrange(0, h), random.uniform(-3, 3), random.uniform(-3, 3), i, random.random(), random.random())
            people.append(person)
        people.append(Person(random.randrange(0, w), random.randrange(0, h), random.uniform(-3, 3), random.uniform(-3, 3), n_people))
        people[n_people].stat = 1
        
        a = 0
        b = 7
        
        for j in range(0, 6):
            
            for i in range(a, b):
            
                if random.random() < 0.5:
                    people[i].maskFrequency = sorted_people[j].maskFrequency
                
                else:
                    people[i].maskFrequency = shuffled_people[j].maskFrequency
                
                
                if random.random() < 0.5:
                    people[i].disFrequency = sorted_people[j].disFrequency
                
                else:
                    people[i].disFrequency = shuffled_people[j].disFrequency
                
            a = a+7
            b = b+7
        global generation
        generation = generation + 1
            

            
           

w=1500
h=800
infectP = 0.8
generation = 1

people=[]
n_people = 50
bestMaskFreq = 0
bestDisFreq = 0

f= 0



def setup():
    global w, h, f
    size(w, h)
    frameRate(300)
    PFont = f
    f = loadFont("NanumGothicExtraBold-40.vlw")
    textFont(f,20)
    for i in range(0, n_people):
        person = Person(random.randrange(0, w), random.randrange(0, h), random.uniform(-3, 3), random.uniform(-3, 3), i, random.random(),random.random())
        people.append(person)
    people.append(Person(random.randrange(0, w), random.randrange(0, h), random.uniform(-3, 3), random.uniform(-3, 3), n_people))
    people[n_people].stat = 1

    
    for person in people:
        person.generator()
    
def draw():
    background(100)
    fill(0)
    for person in people:
        person.display()
        person.socialDistance()
        person.collidecheck()
        person.isMaskWearing()
        person.scoreCheck()
    person.geneManager()
    
    textSize(30)
    textAlign(LEFT)
    text("generation = %d" %generation, 50, 50)
    text("person that had best score in last generation's mask frequency = %f" % bestMaskFreq, 50, 95)
    text("person that had best score in last generation's distance freequency = %f" % bestDisFreq, 50, 140)
