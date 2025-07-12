import pygame
from pygame.locals import *
import random
import numpy

BLACK = (0, 0, 0)
WHITE=(255, 255, 255)
ORANGE = (255, 125, 37)
width=800
height=800
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)
count = 1

class Ant (object):
    def __init__ (self):
        self.position = [width/2, height/2]
        self.direction = random.choice([up, right, left, down])
        self.ground = numpy.zeros((80, 80))

    def antDraw (self):
        pygame.draw.rect(surface, ORANGE , pygame.Rect(self.position[0], self.position[1], 10, 10))

    def groundDraw (self):
        for a in range(0,80):
            for b in range(0, 80):
                if self.ground[[a],[b]] == 1:
                    pygame.draw.rect(surface, BLACK , pygame.Rect(b*10, a*10, 10, 10))
        
    def move (self): # 칸 간격 10
        ant.turn()
        x, y = self.direction
        self.position[0] = self.position[0] + 10*x
        self.position[1] = self.position[1] + 10*y

    def floorCheck(self): # 1이 검정 0이 하양, 검정 위면 우회전 하양 위면 좌회전, 검정이면 True 아님 False
        xPos = int(self.position[0])//10
        yPos = int(self.position[1])//10

        if self.ground[[yPos],[xPos]] == 1:
            self.ground[[yPos],[xPos]] = 0
            return True

        else :
            self.ground[[yPos],[xPos]] = 1
            return False

    def turn (self):
        check = ant.floorCheck()

        if check == True: # 바닥이 검은색일때 우회전
            if self.direction == up:
                self.direction = right
            elif self.direction == right:
                self.direction = down
            elif self.direction == down:
                self.direction = left
            elif self.direction == left:
                self.direction = up

        else: # 바닥이 흰색일때 좌회전
            if self.direction == up:
                self.direction = left
            elif self.direction == left:
                self.direction = down
            elif self.direction == down:
                self.direction = right
            elif self.direction == right:
                self.direction = up

def drawGrid (w, rows, surface): #격자판 그려주는 함수
    sizeBtwn = w // rows
    x=0
    y=0

    for l in range(rows):
        x=x+sizeBtwn
        y=y+sizeBtwn
        pygame.draw.line(surface, (200, 200, 200), (x,0),(x,w))
        pygame.draw.line(surface,(200, 200, 200), (0,y),(w,y))

pygame.init()
window = pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Ant')
surface = pygame.Surface(window.get_size())
surface = surface.convert()
surface.fill(WHITE)
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 60)
window.blit(surface, (0, 0))
font = pygame.font.Font(None, 30)
text = font.render(str(count), 1, BLACK)
gameDone = False
generate = False

ant = Ant()

while gameDone == False:  #게임 루프
    for event in pygame.event.get(): 
        if event.type == QUIT:
            gameDone = True

        elif pygame.key.get_pressed()[pygame.K_f]:
            generate = True
            print("게임 시작")

        elif pygame.key.get_pressed()[pygame.K_r]:
            print("재시작")
            generate = False
            ant.__init__()
            


    surface.fill(WHITE) 
    drawGrid(800, 80, surface)
    if generate == True:
        ant.antDraw()
        ant.groundDraw()
        ant.move()
        count = count+1
        print(count)
    window.blit(text, (50, 50))
    window.blit(surface, (0,0)) 
    pygame.display.flip()
    pygame.display.update()
    clock.tick(1000)




    #끝!!!!!!!!!!!!!!!!!!! :)