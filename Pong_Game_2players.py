import pygame, sys, random
from pygame import mixer
import time

def ball_animation():
    global ball_speed_x, ball_speed_y, opponent_score, player_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

#If ball hits the top or bottom then it will reflect back
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        #If it hits left side the score will go up 1 and sound affect will play
        player_score += 1
        score_time = pygame.time.get_ticks()
        pygame.mixer.music.load('goalsound.wav')
        pygame.mixer.music.play(1)
    
    if ball.right >= screen_width:
        #If it hits right side the score will go up 1 and sound affect will play
        opponent_score += 1
        score_time = pygame.time.get_ticks()
        pygame.mixer.music.load('goalsound.wav')
        pygame.mixer.music.play(1)

    if ball.colliderect(player) or ball.colliderect(opponent): 
        #If ball hits the paddle the ball will go to the opposite direction and sound will play
        ball_speed_x *= -1
        pygame.mixer.music.load('ballhit.wav')
        pygame.mixer.music.play(1)

def player_animation():
    #This will restrict the paddle from leaving the screen
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >=screen_height:
        player.bottom = screen_height

def opponent_ai():
    #This will restrict the paddle from leaving the screen
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >=screen_height:
        opponent.bottom = screen_height
    

def ball_restart():
    global opponent_score, player_score, ball_speed_y, ball_speed_x, score_time
    
#If the oppenent or the player scores 5, the game will reset back to zero
    if opponent_score >= 5:
        opponent_score = -1
        player_score = 0
   
    elif player_score >= 5:
        opponent_score = 0
        player_score = -1

#IF its under 5 the ball will return back to the middle after a goal and will be randomly launched in a direction (possible 4 different directions)
    elif player_score or opponent_score <= 4:

        current_time = pygame.time.get_ticks()
        ball.center = (screen_width/2, screen_height/2)

        if current_time - score_time < 2100:
            ball_speed_x, ball_speed_y = 0,0
        else:
            ball_speed_x = 8 * random.choice((1,-1))
            ball_speed_y = 8 * random.choice((1,-1))
            score_time = None

    
  
        
#Genral setup
pygame.init()
clock = pygame.time.Clock()

#Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")


#Game rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,100)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 100)

#Colours
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

#The speeds of the players
ball_speed_x = 8 * random.choice((1,-1))
ball_speed_y = 8 * random.choice((1,-1))
player_speed = 0
opponent_speed = 0


#Text variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)


#Score timer
score_time = True

while True:
    #Handling inpit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            #Game controls for player - IF down is pressed will go down at a speed of 6, IF up is pressed it will go up at a speed of 6
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed +=6
            if event.key == pygame.K_UP:
                player_speed -=6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -=6
            if event.key == pygame.K_UP:
                player_speed +=6

 #Game controls for oppenent - IF s is pressed will go down at a speed of 6, IF w is pressed it will go up at a speed of 6
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                opponent_speed +=6
            if event.key == pygame.K_w:
                opponent_speed -=6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                opponent_speed -=6
            if event.key == pygame.K_w:
                opponent_speed +=6

#game logic
    ball_animation()
    player_animation()
    opponent_ai()

    

 

    


    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))

    if score_time:
        ball_restart()


        

#THis diplays the player an oppenet scores and will automatically update once scored
    pygame.init()
    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (660,470))

    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (600,470))

    #Updating the window
    pygame.display.flip()
    clock.tick(60)





