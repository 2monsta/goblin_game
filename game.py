#include pygame
	#include pygame which we got from pip
import pygame
#init pygame
# inorder to use pygame, we have to run the init method
pygame.init();

#create a screen with a particular size, the screen size MUST be a TUPLE
screen_size = (512, 480);
#actually tell pygame to set the screen up and store it
pygame_screen = pygame.display.set_mode(screen_size);
#set a pointless caption
pygame.display.set_caption("Goblin Chase");
#set up a var with our
background_image = pygame.image.load("./images/background.png"); #can use a different image just got to know the size
hero_image = pygame.image.load("./images/hero.png"); #can use a different image just got to know the size

#set up the hero location
hero = {
	"x":100,
	"y":100,
	"speed": 10
}
keys = {
	"up":273,
	"down": 274,
	"right": 275,
	"left": 276
}

keys_down ={
	"up": False,
	"down": False,
	"left": False,
	"right": False,
}

# game loop (while)
# create a boolean wheater a game should be going or not
game_on = True;
while(game_on):
	# we are inside the main game loop
	# it will keep running as long as our boolean is true;
	#a quit event(python needs an escape);
	# pygame comes with an even loop! sort of like JS
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			# the user clicked the red x in the top left 
			game_on = False;
		elif (event.type == pygame.KEYDOWN):
			print("user pressed a key");
			if event.key == keys["up"]:
				#hero["y"] -= hero["speed"];
				keys_down["up"] = True;
			elif(event.key == keys["down"]):
				#hero["y"] += hero["speed"];
				keys_down["down"] = True;
			elif(event.key == keys["right"]):
				#hero["x"] += hero["speed"];
				keys_down["right"] = True;
			elif(event.key == keys["left"]):
				#hero["x"] -= hero["speed"];
				keys_down["left"] = True;

	if(keys_down["up"]):
		hero["y"] -= hero["speed"];
	elif(keys_down["down"]):
		hero["y"] += hero["speed"];
	if(keys_down["left"]):
		hero["x"] -= hero["speed"];
	elif(keys_down["right"]):
		hero["x"] += hero["speed"];
	# #actually render something
	# blit takes two argument, block level image transfer
	# 1) what do you want to draw
	# 2) where do oyu want to draw it
	pygame_screen.blit(background_image, [0,0]);
	pygame_screen.blit(hero_image, [hero["x"],hero["y"]]);
#fill in the screen with a color (or image);
# repeat 6 over and over and over....
	pygame.display.flip(); #flip to start over the while loop


