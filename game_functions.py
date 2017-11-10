#-*- encoding: utf-8 -*-
'''
Created on 2017年10月25日
用来储存程序运行函数
@author: 1
'''
import sys
import pygame
from pygame.tests.base_test import pygame_quit
from project import ship
from bullet import Bullet
from project import bullet
from alien import Alien
from lib2to3.fixer_util import Number
from optparse import check_builtin
from time import sleep
from _tkinter import create


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''相应按键'''
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key==pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False
        
    
def check_events(ai_settings,screen,ship,bullets):
    '''相应鼠标和按键事件'''
    for event in pygame.event.get():
        if event.type==pygame_quit():
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event, ship)
            

def update_screen(ai_settings,screen,ship,aliens,bullets):
    '''更新屏幕上的图像，并切换到屏幕'''
    #每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘制所有的子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()       
    aliens.draw(screen)
        #让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets):
    '''更新子弹的位置并删除已经消失的子弹'''
    #更新子弹的位置
    bullets.update()
        
    #删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)


def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
    #检查是否有子弹击中了外星人
    #如果是这样，就删除子弹和外星人
    collisions=pygame.sprite.groupcollide(bullets, aliens,True,True)
    if len(aliens)==0:
        #删除现有的子弹并且创建新的外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
            
def fire_bullet(ai_settings,screen,ship,bullets):
    #创建一颗子弹，并且加入编组bullets中
    new_bullet=Bullet(ai_settings,screen,ship)
    bullets.add(new_bullet)
    
def create_fleet(ai_settings,screen,ship,aliens):
    #创建外星人群
    #创建一个外星人，并计算一行可以容纳多少个外星人
    #外星人间距为外星人的宽度
    alien=Alien(ai_settings,screen)
    number_aliens_x=get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows=get_number_rows(ai_settings, ship.rect.height,alien.rect.height)
    
    #创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
    
def get_number_aliens_x(ai_settings,alien_width):
    '''计算每行容纳多少个外星人'''
    available_space_x=ai_settings.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))
    return number_aliens_x


def get_number_rows(ai_settings,ship_height,alien_height):
    '''计算屏幕可以容纳多少行外星人'''
    available_space_y=(ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    '''创建一个外星人并放在当前行'''
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)  

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    '''更新外星人群众所有外星人的位置'''
    '''检验是否有外星人到达边缘'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    
    #检验是否有飞船到达底端
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)
    
def check_fleet_edges(ai_settings,aliens):
    '''有外星人到达边缘时采取耳朵措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    '''将整个外星人向下移动，并改变他们的方向'''
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1


def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    '''响应被外星人撞到飞船'''
    if stats.ships_left>0:
        stats.ships_left-=1
    
        aliens.empty()
        bullets.empty()
    
    #创建一群外星人，并将飞船放到屏幕的中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.centre_ship()
    
    #暂停
        sleep(0.5)
    else:
        stats.game_active=False

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    '''检验是否有外星人到达了底端'''
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #像飞船被撞倒一样处理
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break
        

    
            
    







