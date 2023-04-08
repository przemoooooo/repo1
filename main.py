import pygame
from sys import exit

def display_score():
    current_time = round((pygame.time.get_ticks() - start_time)/1000)
    score_surface = test_font.render(f'{current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    screen.blit(score_surface, score_rect)
    return current_time

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Wiedźmin 4')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (800,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,200))
player_gravity = 0
#intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))
title_surface = test_font.render('Wiedzmin 4',False, (64,64,64))
title_rect = title_surface.get_rect(center = (400,50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect = snail_surface.get_rect(bottomleft=(800, 300))
                player_rect = player_surface.get_rect(midbottom=(80, 200))
                start_time = pygame.time.get_ticks()

    if game_active:


        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        pygame.draw.line(screen, 'Pink', (0,0), pygame.mouse.get_pos(),10)
        display_score()
        snail_rect.left-=5
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surface,snail_rect)
        #player
        if player_rect.bottom < 300 or player_gravity < 0:
            player_gravity += 1
            player_rect.bottom += player_gravity
        if player_rect.bottom > 300:
            player_rect.bottom = 300
            player_gravity = 0
        screen.blit(player_surface,player_rect)
        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False
            score = display_score()
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        screen.blit(title_surface,title_rect)
        instruction_surface = test_font.render(f'previous score: {score}    press space to begin', False, (64, 64, 64))
        instruction_rect = instruction_surface.get_rect(center=(400, 350))
        screen.blit(instruction_surface,instruction_rect)



    pygame.display.update()
    clock.tick(60)