#include pygame
	#include pygame which we got from pip
import pygame;
import random;

# from the math module(build into python) get the fabs object
from math import fabs;
#init pygame
# inorder to use pygame, we have to run the init method
pygame.init();

#create a screen with a particular size, the screen size MUST be a TUPLE
screen_size = (512, 480);

#generating random locations after goblin has collide with hero
randGobX = random.randint(0,100);
randGobY = random.randint(0,100);
#actually tell pygame to set the screen up and store it
pygame_screen = pygame.display.set_mode(screen_size);
#set a pointless caption
pygame.display.set_caption("Goblin Chase");
#set up a var with our
background_image = pygame.image.load("./images/background.png"); #can use a different image just got to know the size
hero_image = pygame.image.load("./images/hero.png"); #can use a different image just got to know the size
goblin_image = pygame.image.load("./images/goblin.png");
#set up the hero location
hero = {
	"x":100,
	"y":100,
	"speed": 10,
	"wins": 0
}
goblin = {
	"x": 50,
	"y": 50,
	"speed": 15
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
		elif(event.type == pygame.KEYUP):
			#user let go of a key, see if its the one that matters
			if(event.key == keys["up"]):
				# user let go of the up key, flip the switch
				keys_down["up"] = False;
			elif(event.key == keys["down"]):
				keys_down["down"] = False;
			elif(event.key == keys["right"]):
				keys_down["right"] = False;
			elif(event.key == keys["left"]):
				keys_down["left"] = False;

	if(keys_down["up"]):
		hero["y"] -= hero["speed"];
	elif(keys_down["down"]):
		hero["y"] += hero["speed"];
	if(keys_down["left"]):
		hero["x"] -= hero["speed"];
	elif(keys_down["right"]):
		hero["x"] += hero["speed"];

	#Collision detection
	distance_between = fabs(hero["x"] - goblin["x"]) + fabs(hero["y"] - goblin["y"]);
	if (distance_between) < 32:
		#the hero and goblin are touching
		print "collision";
		hero["wins"] += 1;
		print("You Win the Game");
		break;
	else:
		print("not touching");
	# #actually render something
	# blit takes two argument, block level image transfer
	# 1) what do you want to draw
	# 2) where do oyu want to draw it
	pygame_screen.blit(background_image, [0,0]);
		#set a font so we can write the screen
	font = pygame.font.Font(None, 25);
	wins_text = font.render("wins: %d" %(hero["wins"]), True, (0,0,0));
	pygame_screen.blit(wins_text, [40, 40]);

	pygame_screen.blit(hero_image, [hero["x"],hero["y"]]);
	pygame_screen.blit(goblin_image, [goblin["x"], goblin["y"]]);
#fill in the screen with a color (or image);
# repeat 6 over and over and over....
	pygame.display.flip(); #flip to start over the while loop


