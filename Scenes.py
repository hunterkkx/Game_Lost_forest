from random import randint
from sys import *
import sys
sys.path.insert(0,'/mystuff/LOSTFOREST')
from Battle_system import *

class Scene(object):

	def __init__(self):
	
		Scene.collection = []
		
	def enter(self):
		print "nothing happens here"
		exit(1)

class Engine(object):
	
	def __init__ (self,scene_map):
		
		self.scene_map = scene_map
	#self = Map('start') 
	def play(self):
		
		current_scene = self.scene_map.opening_scene()
	
		while True:
			print "\n--------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
class Start(Scene):

	def enter(self):
		print"you waked up in a mystery  forest, a forest full of fog and strange sounds come from all direction, there are beast howling,"
		print "ghost whispering, and insects chirping, what a forest!"
		print "And Then a voice in you mind raised up:\'Oh,boy! You must be wonderring where you are now!\'"
		print "\'Yes, who are you and why i am here?\' said you."
		print "\"You are in the Lost forest which is a dangerious place for those who has lost the hearts!\" said the voice."
		print "\"How could i leave this dangerious place?\""
		print """
			\"You have to defeat the Dark wizard in the center of this forest, but the Dark wizard is too powerful to defeat.
			The only way you could defeat it is to gether all you lost hearts and find the mystery cave where are the sword of truth and shield of truth, 
			when you gether all these items , then you can challenge the dark wizard if your will is strong enough.\"
			\"Are you willing to take the challenge or waiting here to be ate by the beasts?\"
		"""
		action = raw_input("> ")
	
		if action == "yes":
			print "\"You are such a brave young man\" said the voice"
			return 'mystery_cave'
		else:
			print "\"You answer is not gonna save you from this dilemma\" said the voice"
			return 'death' 
	
class Death(Scene):
	
	quips = [
		"Too bad ,boy! it seems you are not prepared well for the challenge!You might want to challenge it again?",
		"Is that the dark wizard too strong or just because you are a coward?Do it again, Coward!",
		"Oh,my hero!You must train yourself better and harder, otherwise you are just another ordinary person,if you are done your train, come to me and try it again.",
		"Death is just a process of every life, time after time you will know it,shall we start again?"]
	
	def enter(self):
		print "again?"
		
		print Death.quips[randint(0, len(self.quips)-1)]

		action = raw_input("Yes/No:")
		if action == "yes":
			return 'revive'
		else:
			print "No a good story to have fun?tell me what you think by sending emails to :573757590@qq.com."
			print "Game over!"
			exit(0)
			
class Revive(Scene):

	def enter(self):
		print "\"you are kind of trying hard, so i will use my magic to let you survive from death.\""
		print "you will to be revived by some kind of magic power"
		return 'start'

class East_forest(Scene):
	def enter(self):
		self.collection.append("heart_of_integrity")
		#print """
			#\"This place used to be the dreamland for the brave fighters, 
			#but things have changed since it comed,a dragon with red scale and giant wings,
			#firing with its dragonbreath, now this place has been a totally miserable hell of fire, 
			#all the fighters here either died or now a timid coward who can not fight anymore!
			#There is a legend saying that the one who kills the dragon of timid could gains his heart - 
			#the heart of brave, but no one has ever proved that.\"
			#\n you walk along a rock pavement where everything was burning and suddenly,
			#a dragon is flying in the sky, and found you on the road, and diving to you.
			#"""
		#print "you need to decide what to do now,run or fight?"
		#action = raw_input("> ")
		
		#if action == "run":
			#print "the dragon is so fast and it reachs you within a few seconds and you were burn by the dragonbreath"
			#return 'death'
		#elif action == "fight":
			#print "You are so brave, no one has ever dared to challenge it since 20 year ago,now i hope you could defeat it and release the residents"
			#return 'dragon_battle'
		#else :
			#print "The dragon fund you, and too bad it is too hungry, and then it catches you and tear your apart and ate you"
			#return 'death'
		return 'central_forest'
class West_forest(Scene):
	
	def enter(self):
		print """
			\"In the west of the forest was the homeland some great honest and hard working dwarf.But since the dragons coming,
			there homeland was nolong exist, the dragon of improbity destroyed the homes and farmlands and nowadays, 
			you can hardly see any of them.We have heard that some of the remains were hiden underground, who knows... \"
			you walk into  the forest and fund the dragon, it is sleeping,
			there are tons of golds around its body, 
			you could take some gold coins back while it is sleep.
			how many coins do you want to take.
			"""
		Numb = input("> ")
		if Numb <= 50:
			print "You are not greedy,i shall let you go and get what you want"
			print "\'I need the heart of brave, can you give it to me?\' said you"
			print "the dragon take out the heart of the brave and gave it to you and fly away!"
			if 'heart_of_brave' in self.collection:
				return 'central_forest'
			else:
				self.collection.append("heart_of_brave")
				return 'central_forest'
		elif Numb > 50:
			print "\'You greedy little man, how dare you steal my gold\'.the dragon is angry and fired on you"
			return 'death'
			
		else:
			print "It seems you are wondering too much and the dragon is not so patient so you are doom, the dragon tear you apart."
			return 'death'
			
class South_forest(Scene):

	def enter(self):
		print """
		the south forest was the residence of elven,once upon a time , 
		the elfs  enjoys their imortal life there and leave peacefully with other creatures.
		Things all changed since the dragons coming.Peace no long exist anymore,
		the elfs either being killed or moved far away from their homeland and never come back again.
		You followed the old path which were built by the elfs into the south forest ,
		there is a wide lake, a dragon is floating on the water near by the shore of the lake,
		this dragon wants you to help him solve a puzzle, other wise him will ate you
		"""
		print "Here is the puzzle:"
		print "\n"
		print "which month has 28 days?"
		
		Answer = raw_input("answer:")
		
		if Answer =="february":
			print "You are not wise enough to get the heart_of_wisedom, thus go to hell!!"
			return 'death'
		elif Answer == "every month":
			print "You got a wise mind, so i shall reward you the heart_of_wisedom"
			if 'heart_of_wisedom' in self.collection:
				return 'central_forest'
			else:
				self.collection.append("heart_of_wisedom")
				return 'central_forest'
		else:
			print "Wrong answer , sorry! You are just a fool and a fool is no good for the world,may be you could be serve as my meal."
			return 'death'
			
class North_forest(Scene):
	def enter(self):
		print """
		the north forest is an icy plateau, there are not too much creatures live here, 
		A dragon hides in the snow, it is hardly to find it if you do not pay attention.
		It has killed innocent passager who were trying to get through the plateau.
		you have to go through the plateau and the dragon is there waiting for you, 
		you have to play a game with the dragon, otherwise he will eat you:
		the game is named snowball rolling, each of you will roll a snowball from the plateau,
		the one who rolls the farthest wins.
		"""
		
		Your_snowball_rolling = randint(1, 800)
		Dragon_snowball_rolling = randint(1,500)
		
		action = raw_input("yes/no:")
		if action == "yes":
			print "You accept the game request and start the snowball rolling game with the dragon"
			print "your score:%s meter " %Your_snowball_rolling
			print "Dragon score:%s meter " %Dragon_snowball_rolling
			if Your_snowball_rolling >= Dragon_snowball_rolling:
				print "You win, you can go through the plateau and i will reward you the heart_of_Love "
				if 'heart_of_Love' in self.collection:
					return 'central_forest'
				else:
					self.collection.append("heart_of_Love")
					return 'central_forest'
			
			else:
				print "You are such a loser, do not even know how to roll a snowball? You smell so taste."
				return 'death'
		else:
			print "your are such a coward, do not even dare to roll a snowball, you must has no ball, dont you?"
			return 'death'
			
class Dark_wizard_room(Scene):

	def enter(self):
		print "Now you have been transtered to a dark room "
		print "where there is a gleam candle in the house and a shadow is in the room, it is the dark wizard with his magic stick in her hand."
		print "\'Oh!Little boy, it seems you have get through all the troubles to come to my place, but now this is the end of it\'said the wizard"
		return 'wizard_battle'
		
	
		
class Mystery_cave(Scene):
	
	def enter(self):
		print """
		after you  take the challege , you fallowed the path that directed by voice in your head and after 2 days, 
		you saw a mystery cave, there is a shinning light in the cave,you were so curious about it and then decide to 
		take a look.After going to the cave, you fund there are some old fashioned box , and there is some gleam shining from the box.
		You opened the box and find a rusty sword and sheild.
		\'these are the sword and sheild left from some ancient hero, they were named sword of truth and sheild of truth,
		it will reveal its true power once they find there true master\' some ancient voice whispered in the air.
		you took up the sword and sheild, somehow , they were trebling, and becoming more and more shining,it seems you were the right person for them.
		"""
		if "sword_of_truth" in self.collection:
			return 'central_forest'
		elif "sheild_of_truth" in self.collection:
			return 'central_forest'
		else:
			self.collection.append("sword_of_truth")
			self.collection.append("sheild_of_truth")
			return 'central_forest'
	
class Central_forest(Scene):
	def enter(self):
		print "you have been transfered to the central of the forest"
		print self.collection
		if set(self.collection) == set(['sword_of_truth','sheild_of_truth','heart_of_brave','heart_of_wisedom','heart_of_integrity','heart_of_Love']):
			return 'dark_wizard_room'
		else:
			print "You are not prepared well, try to find the items that could help you defeat your enamey"
			print "The are four path which leads to the east,south, west and north of the forest, which would like to take?"
		
			direction = raw_input("> ")
				
			if direction == "south":
				return 'south_of_forest'
			elif direction == "north":
				return 'north_of_forest'
			elif direction == "east":
				return 'east_of_forest'
			elif direction == "west":
				return 'west_of_forest'
			else:
				print "you can't distinguish the directions?It seems you are not gonna survive in this forest.You were lost in the forest and ate by whatever moster?"
				return 'death'
				
class Dragon_battle(Scene):
	def enter(self):
		print "The dragon is going so mad at you , and it rushes to you"
	
		dragon_battle = Battle_system(your_blood = 500, dragon_blood = 1000, your_sword_damage = randint(100, 200), dragon_damage = randint(50, 200), your_sheild_defense = 80)

		dragon_battle.fight()
		
		if your_blood <= 0:
			print "your were killed by the dragon"
			return 'death'
		else:
			print "After several round of fighting, you have defeat the draong and get the heart_of_integrity"
			if 'heart_of_integrity' in self.collection:
				return 'central_forest'
			else:
				self.collection.append("heart_of_integrity")
				return 'central_forest'
			
class Wizard_battle(Scene):
	
	def enter(self):
		wizard_battle = Battle_system(self, your_blood = 1000, wizard_blood = 2000,wizard_damage = randint(50, 200), your_sword_damage = randint(100, 200), your_sheild_defense = 80)
		wizard_battle.fight()

		if your_blood <= 0:
			print "you were killed by the wizard"
			return 'death'
		else:
			print "You have defeated the evil wizard and save the whole world!"
			print "the dragons and evil creatures are leaving, and residents of the forest are coming back."
			print "Thanks for your effort , my hero!"
			print "The Lost forest once again shining by the sunshine "
			print "The end!"
			exit(0)
class Map(object):
	scenes = {
			'start': Start(), 'death': Death(),
			'east_of_forest': East_forest(), 'west_of_forest': West_forest(),
			'north_of_forest': North_forest(), 'south_of_forest': South_forest(),
			'revive': Revive(),  'dragon_battle':Dragon_battle(),
			'wizard_battle': Wizard_battle(), 'dark_wizard_room': Dark_wizard_room(),
			'central_forest': Central_forest(), 'mystery_cave': Mystery_cave(),'revive':Revive()
	}
	
	def __init__ (self, start_scene):
	
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
	
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
	
		return self.next_scene(self.start_scene)

a_map = Map('start')
a_game = Engine(a_map)
a_game.play()
	
	

