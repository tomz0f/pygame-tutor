import pygame
pygame.init()

def display_score():
	current_time = pygame.time.get_ticks() - start_time
	current_time = int(current_time / 1000)
	
	score_surf = text_font.render(f"Score: {current_time}", False, (64,64,64))
	score_rect = score_surf.get_rect(center = (400,50))
	
	screen.blit(score_surf, score_rect)

	return current_time

resolution = (800,400)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Pixel Runner')
clock = pygame.time.Clock()
text_font = pygame.font.Font('font/Pixeltype.ttf', 45)
game_active = True
start_time = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(bottomright = (80, 300))
player_gravity = 0

#Intro Screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 175))

game_name = text_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 47))

game_message = text_font.render('Press space to run.', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 300))

def game_over():
	print('Game over!')
	score = 0

def exit_game():
	pygame.quit()
	exit()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit_game()
		if game_active:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
					player_gravity = -20

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
					player_gravity = -20
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				snail_rect.left = 800
				start_time = pygame.time.get_ticks()
	if game_active:
		screen.blit(sky_surface, (0,0))
		screen.blit(ground_surface, (0,300))

		score = display_score()
		
		#Snail (Enemy Entity)
		snail_rect.x -= 4
		if snail_rect.right <= 0: snail_rect.left = 800
		
		screen.blit(snail_surface, snail_rect)
		
		#Player
		player_gravity += 1
		player_rect.y += player_gravity 

		if player_rect.bottom >= 300: player_rect.bottom = 300
		
		screen.blit(player_surf, player_rect)

		if player_rect.colliderect(snail_rect):
			game_active = False
	else:
		screen.fill((94,129,162))
		screen.blit(player_stand, player_stand_rect)
		
		score_message = text_font.render(f'Your score: {score}', False, (111,196,169))
		score_message_rect = score_message.get_rect(center = (400, 350))

		screen.blit(score_message, score_message_rect)
		screen.blit(game_name, game_name_rect)
		screen.blit(game_message, game_message_rect)

	pygame.display.update()
	clock.tick(60)