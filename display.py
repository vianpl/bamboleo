import pygame, sys, PointCloud, math
from pygame.locals import *
from threading import Thread
from pygame import mixer # Load the required library


class display:
	screenx = 1920 #size of the screen
	screeny = 1080
	graphx = 1200 #size of the graph
	graphy = 800
	pc = PointCloud.PointCloud(screenx, screeny, graphx, graphy)
	fps = 30 # frames per second setting
	GREEN = (  180, 180, 180)
	drawstate = "intro"
	DISPLAYSURF = pygame.display.set_mode((screenx, screeny), 0, 32)
	fpsClock = pygame.time.Clock()
	INTRO1 = pygame.image.load('intro1.png').convert_alpha()
	INTRO2 = pygame.image.load('intro2.png').convert_alpha()
	BAMBOLEO1 = pygame.image.load('bamboleo1.png').convert_alpha()
	BAMBOLEO2 = pygame.image.load('bamboleo2.png').convert_alpha()
	BACKGROUND = pygame.image.load('background.png').convert_alpha()
	fpsindex = 0
	bamboleolengthindex = 0
	bamboleolength = 6
        wrap = 11
        fontsize = 60
        attr = "none"
        chall = "none"
	def __init__(self):
		pygame.init()
		# set up the window
		pygame.display.set_caption('Animation')
		pygame.display.toggle_fullscreen()
		self.myfont = pygame.font.SysFont("impact", self.fontsize)
		self.INTRO1 = pygame.transform.scale(self.INTRO1, (self.screenx, self.screeny))
		self.INTRO2 = pygame.transform.scale(self.INTRO2, (self.screenx, self.screeny))
		self.BAMBOLEO1 = pygame.transform.scale(self.BAMBOLEO1, (self.screenx, self.screeny))
		self.BAMBOLEO2 = pygame.transform.scale(self.BAMBOLEO2, (self.screenx, self.screeny))
		self.BACKGROUND = pygame.transform.scale(self.BACKGROUND, (self.screenx, self.screeny))

	def idledraw(self):
		self.DISPLAYSURF.blit(self.BACKGROUND, (0,0))
		self.pc.update()
		for indx in range(0, self.pc.points-1):
			self.GREEN = ( abs(255*math.cos(indx)*0.002),  abs(255*math.sin(indx*0.001)), abs(255*math.sin(indx*0.002)))
			pygame.draw.aaline(self.DISPLAYSURF,self.GREEN,(self.pc.x[indx], self.pc.y[indx]), (self.pc.x[indx+1], self.pc.y[indx+1]))
			pygame.draw.aaline(self.DISPLAYSURF,self.GREEN,(self.pc.x[indx]+1, self.pc.y[indx]+1), (self.pc.x[indx+1]+1, self.pc.y[indx+1]+1))
			pygame.draw.aaline(self.DISPLAYSURF,self.GREEN,(self.pc.x[indx]-1, self.pc.y[indx]-1), (self.pc.x[indx+1]-1, self.pc.y[indx+1]-1))

	def introdraw(self):
		if self.fpsindex == 0:
			self.DISPLAYSURF.blit(self.BACKGROUND, (0,0))
			self.DISPLAYSURF.blit(self.INTRO1, (0,0))
			self.fpsindex += 1
		if self.fpsindex == int(self.fps/2):
			self.DISPLAYSURF.blit(self.BACKGROUND, (0,0))
			self.DISPLAYSURF.blit(self.INTRO2, (0,0))
			self.fpsindex += 1
		if self.fpsindex == self.fps:
			self.fpsindex = 0
		else:
			self.fpsindex += 1

	def bamboleodraw(self, attribute, challenge):
			if self.fpsindex == 0:
				self.DISPLAYSURF.blit(self.BACKGROUND, (0,0))
				self.DISPLAYSURF.blit(self.BAMBOLEO1, (0,0))
				self.fpsindex += 1
                        elif self.bamboleolengthindex >= self.bamboleolength:
				self.DISPLAYSURF.blit(self.BACKGROUND, (0,0))
				self.DISPLAYSURF.blit(self.INTRO2, (0,0))
				text = self.myfont.render(attribute[:-1], 1, (255, 240, 0))
				textpos = text.get_rect()
				textpos.centerx = self.DISPLAYSURF.get_rect().centerx
				textpos.centery = self.DISPLAYSURF.get_rect().centery
				self.DISPLAYSURF.blit(text, textpos)
				textpos = textpos.move(-int(self.screenx/2*0.7), self.fontsize*2)
                                textlength = len(challenge.split())
                                if textlength < self.wrap:
                                	templist = challenge.split()
				        text = self.myfont.render(" ".join(templist), 1, (255, 240, 0))
                                        self.DISPLAYSURF.blit(text, textpos)
                                else:
                                        templist = challenge.split()[:self.wrap]
                                        text = self.myfont.render(" ".join(templist), 1, (255, 240, 0))
                                        self.DISPLAYSURF.blit(text, textpos)
                                        for i in range(self.wrap, textlength, self.wrap):
				                textpos = textpos.move(0, self.fontsize+10)
                                                if i+self.wrap > textlength:
                                                        templist = challenge.split()[i:textlength]
                                                        text = self.myfont.render(" ".join(templist), 1, (255, 240, 0))
                                                        self.DISPLAYSURF.blit(text, textpos)
                                                else:
                                                        templist = challenge.split()[i:i+self.wrap]
                                                        text = self.myfont.render(" ".join(templist), 1, (255, 240, 0))
                                                        self.DISPLAYSURF.blit(text, textpos)
			elif self.fpsindex == int(self.fps/2):
				self.DISPLAYSURF.blit(self.BACKGROUND, (0,0))
				self.DISPLAYSURF.blit(self.BAMBOLEO2, (0,0))
				self.fpsindex += 1
			elif self.fpsindex == self.fps:
				self.fpsindex = 0
				self.bamboleolengthindex += 1
			else:
				self.fpsindex += 1



	def draw(self):
		if self.drawstate == "idle":
			self.idledraw()
		if self.drawstate == "intro":
			self.introdraw()
		if self.drawstate == "bamboleo":
			self.bamboleodraw(self.attr, self.chall)

	def refresh(self):
		while True:
			keys = pygame.key.get_pressed()
			for event in pygame.event.get():
				if event.type == QUIT or event.type == MOUSEBUTTONDOWN:
					pygame.quit()
					sys.exit()
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                        if self.drawstate == 'intro':
                                                self.drawstate = 'idle'
                                        elif self.drawstate == 'bamboleo':
                                                self.drawstate = 'idle'
			self.draw()
			pygame.display.update()
			self.fpsClock.tick(self.fps)

	def startdisplay(self):
    		self.t = Thread(target=self.refresh)
		self.t.daemon = True
        	self.t.start()

        def playbamboleo(self):
        	mixer.init()
		mixer.music.load('baboleo.mp3')
		mixer.music.play()

