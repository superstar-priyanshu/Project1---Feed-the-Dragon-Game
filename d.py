import pygame, random
pygame.init()
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 1000

#set fps
FPS = 60
clock = pygame.time.Clock()
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Dragon Game')

#game values
STARTING_PLAYER_LIVES = 1
PLAYER_VELOCITY = 15
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = .5
BUFFER_DISTANCE = 100
score = 0
player_lives = STARTING_PLAYER_LIVES
coin_velocity = COIN_STARTING_VELOCITY

# setting the fonts of the game
custom_font = pygame.font.Font("f1.ttf", 50)
title_text = custom_font.render('Feed the Dragon', True, (255,255,0), (0,0,0))
title_text_rect = title_text.get_rect()
title_text_rect.centerx = WINDOW_WIDTH//2
title_text_rect.y = 10
score_text = custom_font.render("Score: "+ str(score), True, (255,0,255), (0,0,0))
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10,10)
lives_text = custom_font.render("Lives: "+ str(player_lives), True, (255,0,255), (0,0,0))
lives_texts_rect = lives_text.get_rect()
lives_texts_rect.topright = (WINDOW_WIDTH - 10, 10)
game_over_text = custom_font.render("GAME OVER", True, (255,0,0), (0,0,0))
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
play_again_text = custom_font.render("Press any Key to PLAY again", True, (255,0,0), (0,0,0))
play_again_text_rect = play_again_text.get_rect()
play_again_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

#adding sound into the game
coin_sound = pygame.mixer.Sound('coin_sound.wav')
miss_sound = pygame.mixer.Sound('miss_sound.wav')
miss_sound.set_volume(0.1)
pygame.mixer.music.load('sound1.wav')
pygame.mixer.music.play(-1, 0.0)
dragon_left_image = pygame.image.load('dragon_right.png')
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.left = 32
dragon_left_rect.centery = WINDOW_HEIGHT//2
coin_image = pygame.image.load('coin.png')
coin_image_rect = coin_image.get_rect()
coin_image_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_image_rect.y = random.randint(64, WINDOW_HEIGHT-32)
running =True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_left_rect.top > 100:
        dragon_left_rect.y -= PLAYER_VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_left_rect.bottom < WINDOW_HEIGHT:
        dragon_left_rect.y += PLAYER_VELOCITY

    #moving the coin
    if coin_image_rect.x < 0:
        miss_sound.play()
        player_lives -= 1
        coin_image_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_image_rect.y = random.randint(64, WINDOW_HEIGHT-32)
    else:
        coin_image_rect.x -= coin_velocity

    #collision between dragon and coin
    if dragon_left_rect.colliderect(coin_image_rect):
        score += 1
        coin_sound.play()
        coin_velocity += COIN_ACCELERATION
        coin_image_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_image_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
    
    #game over
    if player_lives == 0:
        display.blit(game_over_text, game_over_text_rect)
        display.blit(play_again_text, play_again_text_rect)
        pygame.display.update()
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = STARTING_PLAYER_LIVES
                    dragon_left_rect.y =WINDOW_HEIGHT//2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1,0.0)
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    
    #updating the score and lives
    score_text = custom_font.render("Score: "+ str(score), True, (255,0,255), (0,0,0))
    lives_text = custom_font.render("Lives: "+ str(player_lives), True, (255,0,255), (0,0,0))
    display.fill((0,0,0))
    display.blit(dragon_left_image, dragon_left_rect)
    display.blit(coin_image, coin_image_rect)
    clock.tick(FPS)
    display.blit(title_text, title_text_rect)
    display.blit(score_text, score_text_rect)
    display.blit(lives_text, lives_texts_rect)
    pygame.draw.line(display, (255,255,255), (0,100), (WINDOW_WIDTH, 100), 2)
    pygame.display.update()

pygame.quit()