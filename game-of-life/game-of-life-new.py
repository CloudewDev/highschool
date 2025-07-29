import pygame
from pygame.locals import *
import sys
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

class CellManager():
    def __init__(self):
        self.pos2cell = dict()

    def AddCell(self, input_pos:tuple):
        self.pos2cell[input_pos] = 0
    
    def UpdateCells(self, gamesize):
        temp_list_for_original_delete = list()
        temp_dict = dict()

        for pos, cell in self.pos2cell.items():
            for i in range(-1, 2):
                for j in range(-1, 2):
                    cur_pos = (pos[0] + i, pos[1] + j)
                    if (i != 0 or j != 0) and (cur_pos[0] >= 0 and cur_pos[0] < gamesize[0] and cur_pos[1] >= 0 and cur_pos[1] < gamesize[1]):
                        if cur_pos in self.pos2cell:
                            self.pos2cell[cur_pos] += 1
                        if cur_pos in temp_dict:
                            temp_dict[cur_pos] += 1
                        else:
                            temp_dict[cur_pos] = 1
    
        for key, cnt in self.pos2cell.items():
            if cnt != 2 and cnt != 3:
                temp_list_for_original_delete.append(key)
            self.pos2cell[key] = 0
        
        for key in temp_list_for_original_delete:
            del self.pos2cell[key]
                
        for key, cnt in temp_dict.items():
            if cnt == 3:
                self.pos2cell[key] = 0
    
    def GenerateRandom(self, times, gamesize):
        for i in range(times):
            self.AddCell((random.randrange(0, gamesize[0]), random.randrange(0, gamesize[1])))

class ScreenManager():
    def __init__(self, input_cell_manager, input_surface, input_game_size, input_rect_size):
        self.color=BLACK
        self.cell_manager = input_cell_manager
        self.surface = input_surface
        self.game_size = input_game_size
        self.rect_size = input_rect_size

    def DrawBoard(self): 
        for pos in self.cell_manager.pos2cell.keys():
            pygame.draw.rect(self.surface, self.color , pygame.Rect(pos[0]*rect_size, pos[1]*rect_size, rect_size, rect_size))

    def SetByHand(self, input_pos):
        pygame.draw.rect(self.surface, self.color , pygame.Rect(input_pos[0]*rect_size, input_pos[1]*rect_size, rect_size, rect_size))
        cell_manager.AddCell(input_pos)
    
    def DrawGrid (self, rect_size):
        x=0
        y=0

        for i in range(game_size[0]):
            x = x + rect_size
            pygame.draw.line(self.surface, GRAY, (x, 0),(x, self.game_size[1] * rect_size))
        for j in range(game_size[1]):
            y = y + rect_size
            pygame.draw.line(self.surface, GRAY, (0, y),(self.game_size[0] * rect_size, y))


game_size = [360, 180]
rect_size = 5

pygame.init()
window = pygame.display.set_mode((game_size[0] * rect_size, game_size[1] * rect_size),0,32)
pygame.display.set_caption('Life Game')
surface = pygame.Surface(window.get_size())
surface = surface.convert()
surface.fill(WHITE)
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 60)
window.blit(surface, (0, 0))

cell_manager=CellManager()
screen_manager = ScreenManager(cell_manager, surface, game_size, rect_size)

gameDone=False 
generate = False

print("r:재시작 f:게임시작 g:무작위 위치에 세포 60개 생성")
print("세포가 순식간에 사라지면 r을 한번 눌러주세요")


gen_cnt = 0
while gameDone == False:  #게임 루프
    for event in pygame.event.get(): 
        if event.type == QUIT:
            gameDone = True
        elif event.type == pygame.MOUSEBUTTONDOWN and generate == False: 
            if event.button == 1:
                x=(int(pygame.mouse.get_pos()[0])//rect_size)
                y=(int(pygame.mouse.get_pos()[1])//rect_size)
                screen_manager.SetByHand((x, y))

        elif pygame.key.get_pressed()[pygame.K_f]:
            generate = True
            print("게임 시작")

        elif pygame.key.get_pressed()[pygame.K_g]:
            print("세포 랜덤 생성")
            cell_manager.GenerateRandom(200, game_size)

        elif pygame.key.get_pressed()[pygame.K_r]:
            print("재시작")
            generate = False
            cell_manager.__init__()
            gen_cnt = 0
            

    surface.fill(WHITE) 
    screen_manager.DrawGrid(rect_size)
    if generate == True:
        cell_manager.UpdateCells(game_size)
        print("현재", gen_cnt, "세대")
        gen_cnt+=1
    screen_manager.DrawBoard()
    window.blit(surface, (0,0)) 
    pygame.display.flip()
    pygame.display.update()
    clock.tick(30)