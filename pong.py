



#Initialise window
import pygame,os
pygame.init()
WIDTH,HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong")



#Constants for the game. 
WHITE=(255,255,255)
BLACK=(0,0,0)
VELOCITY = 10
FRAMERATE= 30
PADDLE_WIDTH,PADDLE_HEIGHT=15,80
BALL_RADIUS = 10
GAMEFONT = pygame.font.SysFont("Dhurjati Regular", 40)



def draw_objects(LeftPlayer,RightPlayer,Border,leftScore,rightScore,ball): # handles drawing of objects
	#draw the background
	WIN.fill(BLACK) 
	
	#draw the players
	pygame.draw.rect(WIN,WHITE,LeftPlayer)
	pygame.draw.rect(WIN,WHITE,RightPlayer)
	
	#draw the border
	pygame.draw.rect(WIN,WHITE,Border)
	
	#draw the ball
	pygame.draw.rect(WIN,WHITE,ball)
	
	#score labels
	leftScoreLabel = GAMEFONT.render(str(leftScore), True, WHITE)
	rightScoreLabel = GAMEFONT.render(str(rightScore), True, WHITE)
	
	#display score labels
	WIN.blit(leftScoreLabel,(338,10))
	WIN.blit(rightScoreLabel,(563,10))
	
	#update the display
	pygame.display.update()
	
def ball_trajectory():
	print()

def ball_shoot():
	print()
	
def win_state(): #win state, detects if ball has hit any of the horizontal borders5
	print()
	#tbd
	
def collision_check(leftPlayer,rightPlayer,ball):
	angle,velocity = 0,0
	return angle,velocity
	
def move_up(player):
	if player.y - VELOCITY > 0:
		player.y-=VELOCITY
	
def move_down(player):
	if player.y + VELOCITY < (HEIGHT-PADDLE_HEIGHT):
		player.y+=VELOCITY
	
def movement(keysPressed,move,player):
	for movement in move:
		if keysPressed[movement]:
			move[movement](player)
	
	
	
def game_loop(): #main game loop
	
	#define each player object
	LeftPlayer = pygame.Rect(100,170,PADDLE_WIDTH,PADDLE_HEIGHT)
	RightPlayer = pygame.Rect(730,170,PADDLE_WIDTH,PADDLE_HEIGHT)
	leftScore, rightScore = 0,0
	Border = pygame.Rect(WIDTH/2 - 5, 0, 2, HEIGHT)
	ball = pygame.Rect(WIDTH/2 - 0.5*(BALL_RADIUS), HEIGHT/2, BALL_RADIUS, BALL_RADIUS)
	
	LEFT_MOVEMENT = {
		pygame.K_w : move_up,
		pygame.K_s : move_down}
	
	RIGHT_MOVEMENT = {
		pygame.K_UP : move_up,
		pygame.K_DOWN : move_down}
	
	runGame = True
	clock = pygame.time.Clock()
	
	#main game loop
	while runGame:
		
		#game clock, handles how often each frame occurs
		clock.tick(FRAMERATE)
		
		#if the game is quit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				runGame = False
		

		keysPressed = pygame.key.get_pressed()
		movement(keysPressed,LEFT_MOVEMENT,LeftPlayer)
		movement(keysPressed, RIGHT_MOVEMENT, RightPlayer)
		draw_objects(LeftPlayer,RightPlayer,Border,leftScore,rightScore,ball)



game_loop()
	
	
