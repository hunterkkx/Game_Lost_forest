class Battle_system():
	def __init__(self, hero_blood, enemy_blood,enemy_damage, hero_sword_damage, hero_sheild_defense):
		self.hero_blood = hero_blood
		self.enemy_blood = enemy_blood
		self.enemy_damage = enemy_damage
		self.hero_sword_damage = hero_sword_damage
		self.hero_sheild_defense = hero_sheild_defense
		
	def fight(self):
		while self.hero_blood > 0 and self.enemy_blood > 0:
			
			if self.enemy_damage >= self.hero_sheild_defense:
				self.hero_blood = self.hero_blood - self.enemy_damage + self.hero_sheild_defense 
				self.enemy_blood = self.enemy_blood - self.hero_sword_damage 
				print self.hero_blood , self.enemy_blood
			else:
				self.hero_blood = self.hero_blood 
				self.enemy_blood = self.enemy_blood - self.hero_sword_damage
				return self.hero_blood
