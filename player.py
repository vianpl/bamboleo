import math

class player:
	def __init__(self, screenx, screeny):
		self.xposition = screenx/2
		self.yposition = screeny/2
		self.speed = 10
	def updatePosition(self, mouse):
		if self.xposition - mouse[0] == 0:
			angle = 0
		else:	
			angle = math.atan((self.yposition - mouse[1])/(self.xposition - mouse[0]))
 		
 		if (self.xposition - mouse[0]) < 0:
	 		self.xposition += int(self.speed * math.cos(angle))
			self.yposition += int(self.speed * math.sin(angle))
		else:
			self.xposition -= int(self.speed * math.cos(angle))
			self.yposition -= int(self.speed * math.sin(angle))
				