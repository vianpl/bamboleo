import math, random
wide = 3.3*math.pi 

class PointCloud:
	points = 440

	def __init__(self, screenx, screeny, graphx, graphy):
		self.ratio_step = 100
		self.ratio1 = 111
		self.ratio2 = 1200
		self.axis = list()
		self.x = list()
		self.y = list()
		self.screenx = screenx/2
		self.screeny = screeny/2
		self.grapx = graphx/2
		self.grapy = graphy/2
		for indx in range(0, self.points):
			self.axis.insert(indx, indx*(wide/self.points))
			self.x.insert(indx,0)
			self.y.insert(indx,0)

	def update(self):
		self.ratio1 += 0.003
		self.ratio2 += 0.005
		for indx in range(0, self.points):
			self.x[indx] = math.cos(self.ratio1*self.axis[indx])*self.grapx+self.screenx
			self.y[indx] = math.sin(self.ratio2*self.axis[indx])*self.grapy+self.screeny

