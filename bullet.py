#-*- encoding: utf-8 -*-
'''
Created on 2017年10月25日

@author: 1
'''
import pygame
from pygame.sprite import Sprite
from project import ship

class Bullet(Sprite):
    '''对一个飞船发射的子弹进行管理的类'''
    
    def __init__(self,ai_settings,screen,ship):
        '''在飞船的位置创建一个子弹对象'''
        '''通过使用精灵，可以将游戏中的元素编组，进而同时操作所有的元素'''
        #继承Sprite
        super().__init__()
        self.screen=screen
        
        #在(0,0)处创建一个表示子弹的矩形，再设计正确的位置
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        
        #存储用小数表示子弹的位置
        self.y=float(self.rect.y)
        
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
        
    def update(self):
        '''向上移动子弹'''
        #更新表示子弹位置的小数值
        self.y-=self.speed_factor
        #更新表示子弹的rect位置
        self.rect.y=self.y
        
    def draw_bullet(self):
        '''绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)
         