#include pygame
	#include pygame which we got from pip
import pygame;
import random;
import time;

# from the math module(build into python) get the fabs object
from math import fabs, hypot;
#init pygame
# inorder to use pygame, we have to run the init method
pygame.init();
screenX = 512;
screenY = 480;
#create a screen with a particular size, the screen size MUST be a TUPLE
screen_size = (screenX, screenY);


#actually tell pygame to set the screen up and store it
pygame_screen = pygame.display.set_mode(screen_size);
#set a pointless caption
pygame.display.set_caption("Goblin Chase");


#can use a different image just got to know the size
background_image = pygame.image.load("./images/background.png");
 #can use a different image just got to know the size
hero_image = pygame.image.load("./images/hero.png");
goblin_image = pygame.image.load("./images/goblin.png");
power_up_image = pygame.image.load("./images/asuna.jpg");

#set up the hero location
hero = {
	"x":100,
	"y":100,
	"speed": 10,
	"wins": 0,
	"health": 3
}
goblin = {
	"x": screenX / 2,
	"y": screenY / 2,
	"speed": 3,
	"health": 3,
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
monster = {
	"x": random.randint(70, 450),
	"y": random.randint(70, 400),
	"speed": 20
}


# def top_right():
# 	goblin["x"] +=1;
# 	goblin["y"] +=1;
# def top_left():
# 	goblin["x"] -=1;
# 	goblin["y"] +=1;
# def bottom_right():
# 	goblin["x"] +=1;
# 	goblin["y"] -=1;
# def bottom_left():
# 	goblin["x"] -=1;
# 	goblin["y"] -=1;
#=============Keep Hero on Screen =====
def keep_hero():
	if(hero["x"] <= 0):
		hero["x"] = 0;
	elif(hero["x"]> 480):
		hero["x"] = 480
	if(hero["y"] < 0):
		hero["y"] = 0;
	elif(hero["y"] > 450):
		hero["y"] = 450;

#===================Goblin Moving========
# def goblin_moving():
# 	if(hero["x"] > screenX /2 and hero["y"] > screenY /2):
# 		top_right();
# 	elif(hero["x"] < screenX /2 and hero["y"] > screenY /2):
# 		top_left();
# 	elif(hero["x"] > screenX /2 and hero["y"] < screenY /2):
# 		bottom_right();
# 	elif(hero["x"] < screenX /2 and hero["y"] < screenY /2):
# 		bottom_left();


# game loop (while)
# create a boolean wheater a game should be going or not
game_on = True;
#added key flip switch

monster_power_up = True;
monster_returns_to_map = True;
hero_max_health = True;

while(game_on):

#===================Goblin Moving========
	#WORKING ON MOVE SPEED OF GOBLIN
	#at the start, we want goblin to move randomly towards the hero
	# goblin_moving();
	
	

#=============Keep Hero on Screen =====
	keep_hero();
#=============EVENT HANDLE=============
		
	# we are inside the main game loop
	# it will keep running as long as our boolean is true;
	#a quit event(python needs an escape);
	# pygame comes with an even loop! sort of like JS
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			# the user clicked the red x in the top left 
			game_on = False;
		elif (event.type == pygame.KEYDOWN):
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
	#distance between hero and monster
	distance_betweenHM = fabs(hero["x"] - monster["x"]) + fabs(hero["y"] - monster["y"]);
	# ==================================================================
	#keep goblin move towards to hero
	dx = goblin["x"] - hero["x"];
	dy = goblin["y"] - hero["y"];
	dist = hypot(dx, dy);

	dx = dx/dist;
	dy = dy/dist;
	goblin["x"] -= dx * goblin["speed"];
	goblin["y"] -= dy * goblin["speed"];
	# =============================================================================
	if (distance_between < 32):
		goblin["x"] = 200;
		goblin["y"] = 200;
		goblin["speed"] += 1;
		#the hero and goblin are touching		
		hero["health"] -=1;
		hero["speed"] -=5;
		if(hero["health"]<= 0):
			hero["health"] = 0;
		if(hero["speed"] <= 0):
			hero["speed"] = 10;

	# #actually render something
	# blit takes two argument, block level image transfer
	# 1) what do you want to draw
	# 2) where do oyu want to draw it
	pygame_screen.blit(background_image, [0,0]);
		#set a font so we can write the screen
	font = pygame.font.Font(None, 25);
	wins_text = font.render("wins: %d" %(hero["wins"]), True, (0,0,0));
	pygame_screen.blit(wins_text, [40, 40]);

	hero_health = font.render("health %d" %(hero["health"]), True, (0, 0, 0) )
	pygame_screen.blit(hero_health, [400, 40]);

	pygame_screen.blit(hero_image, [hero["x"],hero["y"]]);
	pygame_screen.blit(goblin_image, [goblin["x"], goblin["y"]]);

#========================Monster As power UP=============
	#Monster now respond after collision, can change to power up later.
	if(monster_power_up == True):
		pygame_screen.blit(power_up_image, [monster["x"], monster["y"]]);
		if(distance_betweenHM<32):
			pygame_screen.blit(power_up_image, [-10, -10]);
			hero["speed"] += 5;
			goblin["speed"] -=1;
			monster_power_up = False;
			monster_returns_to_map = False;
			if(hero["speed"] == 25):
				hero["speed"] = 25;
			if(hero_max_health == True):
				hero["health"] += 1;
			if(hero["health"] >=3):
				hero["health"] =3;
				pygame_screen.blit(power_up_image, [-10, -10]);
	if(monster_returns_to_map == False):
		monster["x"] = random.randint(70, 450);
		monster["y"] = random.randint(70, 400);
		pygame_screen.blit(power_up_image, [monster["x"], monster["y"]]);
		monster_returns_to_map = True;
		monster_power_up = True;


#fill in the screen with a color (or image);
# repeat 6 over and over and over....
	pygame.display.flip(); #flip to start over the while loop


