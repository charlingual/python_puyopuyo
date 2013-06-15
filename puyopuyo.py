# coding: utf-8
import pygame
from pygame.locals import *
import random
import sys

RED, BLUE, GREEN, YELLOW = 0, 1, 2, 3
SCR_RECT = Rect(0, 0, 400, 500) #スクリーンのサイズ
CS = 50 #1マスあたりのサイズ
max_rensa = 0 #最大連鎖数
rensa = 0 #現在の連鎖数




class Field:
    sum_puyo = 0 #ぷよの繋がってる数、4超えてたら消える
    puyo_point = [] #ぷよの座標入れる、sum_puyoが4超えてたらこの座標を消す
    def __init__(self):
        self.field = [[] for x in range(6)]

    def same_color(self, column, line):
        sum_puyo++
        puyo_point.append([column, line])
        if line > 0:
            if self.field[column][line-1] == self.field[column][line]:
                same_color(self, column, line-1)
        if line < 
        if column > 0:
            if self.field[column-1][line] == self.field[column][line]:
                same_color(self, column-1, line)
        if column < 5:
            if self.field[column+1][line] == self.field[column][line]:
                same_color(self, column+1, line)
                
                

    def judge(self, column, line):

                judge
                
        


    def gameover(self):
        if len(self.field[2]) >= 10:
            return True
        else:
            return False

    
    def vanish(self, column, line1, line2):
        self.field[column][line1:line2+1] = []
        

    def add(self, column, *puyo):
        for n in puyo:
            self.field[column].append(n)


    


class Puyo:
    def __init__(self, color):
        self.color = color

        
if __name__ == '__main__':
    myfield = Field()
    myfield.add(2, 1,2,3,4,5,6,7,8,9)
    print myfield.field
    if myfield.gameover() == True:
        print "gameover!!!!!!"

    myfield.vanish(2, 3, 5)
    myfield.add(2,1)
    print myfield.field
    if myfield.gameover() == True:
        print "gameover!!!!!!"
#    myfield.vanish(0, 5, 9)
#    print myfield.field
