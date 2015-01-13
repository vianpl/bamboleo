from spotify_control import SpotifyControl
from random import randint
from time import sleep
import threading, linecache, re, display

class Bamboleo:

    CHALLENGES_FILE_NAME = "pruebas"
    ATTRIBUTES_FILE_NAME = "ropa"
    MAX_TIME = 10
    MIN_TIME = 5
    def __init__(self):
	self.spotify = SpotifyControl()
	self.challenges = open(self.CHALLENGES_FILE_NAME, 'r')
	self.attributes = open(self.ATTRIBUTES_FILE_NAME, 'r')
	self.numchallenges = sum(1 for line in self.challenges if line.strip())
	self.numattributes = sum(1 for line in self.attributes if line.strip())
	self.timetowait = randint(self.MIN_TIME, self.MAX_TIME)
	self.state = 'intro'
	self.disp = display.display()
	self.disp.startdisplay()

    def printinfo(self):
	print self.numattributes
	print self.numchallenges
	print self.timetowait

    def timer(self):
	sleep(self.timetowait)
	self.disp.drawstate = 'bamboleo'

    def startcounting(self):
	self.t = threading.Thread(target=self.timer)
	self.t.daemon = True
	self.t.start()

    def getattribute(self):
	randattr = randint(1, self.numattributes)
	self.disp.attr = linecache.getline(self.ATTRIBUTES_FILE_NAME, randattr)

    def getchallenge(self):
	randattr = randint(1, self.numchallenges)
	self.disp.chall = linecache.getline(self.CHALLENGES_FILE_NAME, randattr)
	print self.disp.chall

    def bamboleo(self):
	self.t.join()
	self.spotify.playpause()
	self.disp.playbamboleo()

    def getattr(self):
    	self.getattribute()
	self.getchallenge()


b = Bamboleo()
while True:
    if b.disp.drawstate == 'idle' and b.state == "intro":
	b.startcounting()
	b.getattr()
	b.state = 'idle'
	sleep(1)
    elif b.state == 'bamboleo' and b.disp.drawstate == 'idle':
	b.state = 'idle'
	b.startcounting()
	b.spotify.playpause()
	b.getattr()
	b.disp.bamboleolengthindex = 0
	sleep(1)
    elif b.state == 'idle' and b.disp.drawstate == 'bamboleo':
	b.bamboleo()
	b.state = 'bamboleo'
	sleep(1)
    else:
	sleep(1)
