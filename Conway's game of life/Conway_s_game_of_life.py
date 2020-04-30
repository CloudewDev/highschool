import pygame
import sys
import numpy as np
from pygame.locals import *
import random

BLACK = (0, 0, 0)
WHITE=(255, 255, 255)
width=800
height=800

class Cell (object):
    def __init__(self):
        self.color=BLACK
        self.xGridPos=[] #격자판 상의 위치. (1,1), (2,2) 이런식으로 저장됨
        self.yGridPos=[]
        self.gameBoard=np.zeros((40,40))
        self.nGameBoard=np.zeros((40,40))
        self.nearCell=0

    def saveFirstPositions (self, xGrid, yGrid): 
        self.gameBoard[[yGrid],[xGrid]]=1
        self.xGridPos.append(xGrid)
        self.yGridPos.append(yGrid)

    def draw(self, surface): 
        for p in range (0, len(self.xGridPos)):
            pygame.draw.rect(surface, self.color , pygame.Rect(self.xGridPos[p]*20, self.yGridPos[p]*20, 20, 20))

    def generate(self):
        self.nGameBoard=np.zeros((40,40))
        for screenY in range(0,40):
            for screenX in range(0,40):
                cell.nearCheck(screenY,screenX)
                #print("기준점 :", screenY, ",", screenX)
        self.gameBoard = self.nGameBoard
        cell.savePositions()

    def nearCheck(self, nearY, nearX):
        self.nearCell=0
        for checkY in range (nearY-1, nearY+2):
            for checkX in range(nearX-1, nearX+2):
                #print(checkX,",", checkY,"체크함")
                if checkX>-1 and checkX<40 and checkY>-1 and checkY<40 and self.gameBoard[[checkY],[checkX]] == 1:
                    if checkX==nearX and checkY==nearY:
                        self.nearCell = self.nearCell
                        #print("여긴 중앙칸임")
                        #print(self.nearCell)
                    else:
                        self.nearCell = self.nearCell+1
                        
        #print(nearX, ",", nearY, "의 nearCell은 ", self.nearCell)

        if self.gameBoard[[nearY],[nearX]] == 1: 
           if self.nearCell == 2 or self.nearCell == 3:
                self.nGameBoard[[nearY],[nearX]] = 1
                #print(nearX, ",",nearY,"세포 유지")
            
        elif self.nearCell == 3 and self.gameBoard[[nearY],[nearX]] == 0:
            self.nGameBoard[[nearY],[nearX]] = 1
            #print(nearX, ",",nearY,"세포 살아남")
            
        else:
            self.nGameBoard[[nearY],[nearX]] = 0
            #print(nearX, ",",nearY,"세포 죽음")
            
    def savePositions (self):
        self.xGridPos = []
        self.yGridPos = []
        for addY in range(0,40):
            for addX in range(0,40):
                if self.gameBoard[[addY],[addX]] == 1:
                    self.xGridPos.append(addX)
                    self.yGridPos.append(addY)

    def test (self): #말그대로 잘 작동하나 테스트하려고 만든 함수
        print(self.gameBoard)

def drawGrid (w, rows, surface): #격자판 그려주는 함수
    sizeBtwn = w // rows
    x=0
    y=0

    for l in range(rows):
        x=x+sizeBtwn
        y=y+sizeBtwn
        pygame.draw.line(surface, BLACK, (x,0),(x,w))
        pygame.draw.line(surface, BLACK, (0,y),(w,y))

pygame.init()
window = pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Life Game')
surface = pygame.Surface(window.get_size())
surface = surface.convert()
surface.fill(WHITE)
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 60)
window.blit(surface, (0, 0))
cell=Cell()
gameDone=False 
generate = False

print("r:재시작 f:게임시작 g:무작위 위치에 세포 60개 생성")
print("세포가 순식간에 사라지면 r을 한번 눌러주세요")

while gameDone == False:  #게임 루프
    for event in pygame.event.get(): 
        if event.type == QUIT:
            gameDone = True
        elif event.type == pygame.MOUSEBUTTONDOWN and generate == False: 
            if event.button == 1:
                xGridNum=(int(pygame.mouse.get_pos()[0])//20)
                yGridNum=(int(pygame.mouse.get_pos()[1])//20)
                cell.saveFirstPositions(xGridNum, yGridNum) 
                # print(cell.test())

        elif pygame.key.get_pressed()[pygame.K_f]:
            generate = True
            print("게임 시작")

        elif pygame.key.get_pressed()[pygame.K_g]:
            print("세포 60개 랜덤 생성")
            for repeat in range(0,61):
                 cell.saveFirstPositions(random.randrange(0,40), random.randrange(0,40))

        elif pygame.key.get_pressed()[pygame.K_r]:
            print("재시작")
            generate = False
            cell.__init__()
            

    surface.fill(WHITE) 
    drawGrid(800,40,surface)
    if generate == True:
        cell.generate()
    cell.draw(surface)
    window.blit(surface, (0,0)) 
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

    #어예ㅔ에ㅔ에에ㅔ에ㅔ에!!!!
    #ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
    #끝!