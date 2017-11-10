#-*- encoding: utf-8 -*-
'''
Created on 2017年10月28日
我们需要确定外星人和飞船碰撞的时候我们需要做些什么，我们通过跟踪游戏的统计信息来记录飞船被撞了多少次
@author: 1
'''
class GameStats():
    '''跟踪游戏的统计信息'''
    
    def __init__(self,ai_settings):
        '''初始化游戏信息'''
        self.ai_settings=ai_settings
        self.reset_stats()
        
        #游戏刚启动的时候处于活动状态
        self.game_active=True
    
    def reset_stats(self):
        '''初始化游戏运行中可能变化的信息'''
        self.ships_left=self.ai_settings.ship_limit
        