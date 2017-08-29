from random import randint
from sys import exit

class Scene(object):
	collection = []
	def enter(self):
		print "nothing happens here"

class start(Scene):
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
	action == raw_input("> ")
	
	if action == "yes":
		print "\"You are such a brave young man\" said the voice"
		return mystery_cave
		
	else:
		print "\"You answer is not gonna save you from this dilemma\" said the voice"
		return death 

class Death(Scene):
	print "again?"
	quips = [
		"Too bad ,boy! it seems you are not prepared well for the challenge!You might want to challenge it again?",
		"Is that the dark wizard too strong or just because you are a coward?Do it again, Coward!",
		"Oh,my hero!You must train yourself better and harder, otherwise you are just another ordinary person,if you are done your train, come to my and try it again.",
		"Death is just a process of every life, time after time you will know it,shall we start again?"]
	
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1]
		exit(0)

class Revive(Scene):
	def enter(self):
	print "Yes or No?"	
	action = raw_input("Yes/No:")
	if action == "Yes":
		print "You are now going to be revived by the angel!"
		return revive
	elif action = "No"
		print "You coward!,Then you shall be dead forever until you are will to do that again."
		return death
	else 
		print "Are you a fool?Can even spell the yes or no correctly?"
		return death

class East_Forest(Scene):
	def enter(self):
		print """
			\"This place used to be the dreamland for the brave fighters, 
			but things have changed since it comed,a dragon with red scale and giant wings,
			firing with its dragonbreath, now this place has been a totally miserable hell of fire, 
			all the fighters here either died or now a timid coward who can not fight anymore!
			There is a legend saying that the one who kills the dragon of timid could gains his heart - 
			the heart of brave, but no one has ever proved that.\"
			\n you walk along a rock pavement where everything was burning and suddenly,
			a dragon is flying in the sky, and found you on the road, and diving to you.
			"""
		action = raw_input("> ")
		
		if action == "run":
			print "the dragon is so fast and it reachs you within a few seconds and you were burn by the dragonbreath"
			return death
		elif action == "fight":
			print "You are so brave, no one has ever dared to challenge it since 20 year ago,now i hope you could defeat it and release the residents"
			return dragon_battle 
		else :
			print "The dragon fund you, and too bad it is too hungry, and then it catches you and tear your apart and ate you"
			return death
class West_Forest():
	
	def enter(self)：
		print """
			\"In the west of the forest was the homeland some great honest and hard working dwarf.But since the dragons coming,
			there homeland was nolong exist, the dragon of improbity destroyed the homes and farmlands and nowadays, 
			you can hardly see any of them.We have heard that some of the remains were hiden underground, who knows... \"
			you walk into  the forest and fund the dragon, it is sleeping,
			there are tons of golds around its body, 
			you could take some gold coins back while it is sleep.
			how many coins do you want to take.
			"""
		Numb == raw_input("> ")
		if Num <=50:
			print "You are not greedy,i shall let you go and get what you want"
			print "\'I need the heart of brave, can you give it to me?\' said you"
			print "the dragon take out the heart of the brave and gave it to you and fly away!"
			collection.append("heart_of_brave")
			return central_forest
		elif Num > 50:
			print "\'You greedy little man, how dare you steal my gold\'.the dragon is angry and fired on you"
			return death
			
		eles:
			print "It seems you are wondering too much and the dragon is not so patient so you are doom, the dragon tear you apart."
			return death
			
class South_Forest(Scene):
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
		print "which month has 28days?"
		
		Answer == raw__input("answer:")
		
		if Answer =="february":
		print "You are not wise enought to get the heart of wisedom"
			return death
		elif Answer == "every month":
			print "You got a wise mind, so i shall reward you the heart_of_wisedom"
			collection.append("heart_of_wisedom")
		else:
			print "Wrong answer , sorry! You are just a fool and fool is no good for the world,may be you could be serve as my meal."
			return death
class North_forest():
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
		
		Your_snowball_rolling = randint(1, 500)
		Dragon_snowball-rolling = randint(1,800)
		
		print "You accept the game request and start the snowball rolling game with the dragon"
		print Your_snowball_rolling
		print Dragon_snowball-rolling
		
		if Your_snowball_rolling > = Dragon_snowball-rolling:
			print "You win, you can go through the plateau and i will reward you the heart_of_Love "
			collection.append("heart_of_Love")
			return central_forest
			
		else:
			print "You are such a loser, do not even know how to snow a ball? You smell so taste."
			return death
			
class Dark_wizard_Room(Scene):
	
	def enter(self):
		print "Now you have been transtered to a dark room "
		print "where there is a gleam candle in the house and a shadow is in the room, it is the dark wizard with his magic stick in her hand."
		print "\'Oh!Little boy, it seems you have get through all the trouble to come to my place, but now this is the end of it\'said the wizard"
		
		return battle
		
	
		
class Mystery_cave(Scene):
	
	def enter(self):
		print """
		after you  take the challege , you fallowed the path that directed by voice in your head and  after  2 days, 
		you saw a mystery cave, there is a shinning light in the cave,you were so curious about it and then decide to 
		take a look.After going to the cave, you fund there are some old fashioned box , and there is some gleam shining from the box.
		You opened the box and find a rusty sword and sheild.
		\'these are the sword and sheild left from some ancient hero, they were named sword of truth and sheild of truth,
		it will reveal its true power once they find there true master\' some ancient voice whispered in the air.
		you took up the sword and sheild, somehow , they were trebling, and becoming more and more shining,it seems you were the right person for them.
		"""

		collection.append(sword_of_truth)
		collection.append(sheild_of_truth)
		return entrance_of_forest
	
class central_of_forest(Scene):
	def enter(self):
		print "you have been transfered to the central of the forest"
		
		if collection == [heart_of_Love,heart_of_brave,heart_of_wisedom,heart_of_integrity]:
			return dark_wizard_room
		
		else:
			print "The are four path which leads to the east,south, west and north of the forest, which would like to take?"
		
			direction == raw_input("> ")
				
			if direction == "south":
				return south_of_forest
			elif direction == "north":
				return north_of_forest
			elif direction == "east":
				return east_of_forest:
			elif direction == "west":
				return west_of_forest
			else:
				print "you can't distinguish the directions?It seems you are not gonna survive in this forest.You were lost in the forest and ate by whatever moster?"
				return death
				
class Dragon_battle(Scene):
	
	
	def enter(self):
		dragon_blood = 500
		your_blood = 300
		print "the dragon is furious at you, it sprays dragonbreath at you, you raised your sheild and try to hit it with your sword!"

		while your_blood > 0 and dragon_blood > 0:
			dragon_damage = randint(50, 200)
			your_sword_damage = randint(50, 100)
			your_sheild_defense = 80
			if dragon_damage >= 80:
				your_blond = your_blood - dragon_damage + 80 
				dragon_blood = dragon_blood - your_sword_damage
				print your_blood , draon_blood
			else:
				your_blood = your_blood 
				dragon_blood = dragon_blood - your_sword_damage
		if your_blood <= 0:
			print "your were killed by the dragon"
			return death
		else:
			print "After several round of fighting, you have defeat the draong and get the heart_of_integrity"
			collection.append("heart_of_integrity")
			return central_forest
class Wizard_battle(Scene):
	
		def enter(self):
			
			your_blood = 1000
			wizard_blood = 3000
			
			while your_blood > 0 and wizard_blood > 0:
				your_sword_damage = randint(50, 200)
				your_sheild_defense = randint(50, 200)
				wizard_damage = randint(100, 300)
				
				if wizard_damage > your_sheild_defense:
					your_blood = your_blond - wizard_damage + your_sheild_defense
					wizard_blood = wizard_damage - your_sword_damage
					print your_blond, wizard_blood
					
				else:
					your_blood = your_blood
					wizard_blood = wizard_damage -your_sword_damage
					print your_blood, wizard_blood
			if your_blond <= 0:
				print "you were killed by the wizard"
				return death
			
			else:
				print "You have defeated the evil wizard and save the whole world!"
				print "the dragons and evil creatures are leaving, and residents of the forest are coming back."
				print "Thanks for your effort , my hero!"
				print "The Lost forest once again shining by the sunshine "
				print "The end!"
				exit(0)
			

