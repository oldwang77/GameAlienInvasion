#-*- encoding: utf-8 -*-
'''
Created on 2017年10月24日
我们先做程序的主页面
@author: 1
'''
import sys
import pygame
from pygame.tests.base_test import pygame_quit
from settings import Settings
from ship import Ship
import game_functions as gf
from email._header_value_parser import Group
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats


def run_game():
    #初始化游戏并创建一个对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    #创建一个用于储存游戏统计信息的实例
    stats=GameStats(ai_settings)
    
    #创建一个用于存储子弹的编组,一艘飞船，一个外星人编组
    ship=Ship(ai_settings,screen)    
    bullets=Group()
    aliens=Group()
    
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #创建一个外星人
    alien=Alien(ai_settings,screen)
    
    while True:
        #监听键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)       
                 
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
        
