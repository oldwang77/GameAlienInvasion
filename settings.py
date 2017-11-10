#-*- encoding: utf-8 -*-
'''
Created on 2017年10月25日

@author: 1
'''
class Settings():
    '存储外星人入侵的所有的类'
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        
        #飞船的位置,每次移动1.5个像素
        self.ship_speed_factor=1.5
        
        #飞船数目设置
        self.ship_limit=3
        
        #控制外星人的运动
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        #fleet_direction表示1表示向右移动，为-1表示向左移
        self.fleet_direction=1
        
        #子弹的设置
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=5
        self.bullet_color=60,60,60