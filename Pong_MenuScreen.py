import pygame, sys
from button import Button
#import Pong_Game_2players, Pong_game_1player

pygame.init()

pygame.mixer.music.load('Halo3.mp3')
pygame.mixer.music.play(-1)

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    pygame.init()
    return pygame.font.Font("font.ttf", size)

def oneplayer():
    #IF one player is clicked will open one player
    import Pong_game_1player
    Pong_game_1player()

def twoplayers():
    #IF two players is clickef will open two players
    import Pong_Game_2players
    Pong_Game_2players()
    





while True:
    SCREEN.blit(BG, (0, 0))

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT = get_font(100).render("PONG", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))


#Single pplayer options - Opens the png, postions the rectangle image, and then inserts text and colour
    PLAYER1_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 250), 
                        text_input="1 PLAYER", font=get_font(65), base_color="#d7fcd4", hovering_color="White")

#Double player options
    PLAYER2_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 400), 
                        text_input="2 PLAYERS", font=get_font(65), base_color="#d7fcd4", hovering_color="White")

#QUIT
    QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550), 
                        text_input="QUIT", font=get_font(65), base_color="#d7fcd4", hovering_color="White")

    SCREEN.blit(MENU_TEXT, MENU_RECT)

#CHanges colour when hovered
    for button in [PLAYER1_BUTTON, PLAYER2_BUTTON, QUIT_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(SCREEN)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #IF pressed this variable will launch
            if PLAYER1_BUTTON.checkForInput(MENU_MOUSE_POS):
                oneplayer()
            #IF pressed this variable will launch
            if PLAYER2_BUTTON.checkForInput(MENU_MOUSE_POS):
                twoplayers()
                    
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                pygame.quit()
                sys.exit()

        pygame.display.update()

