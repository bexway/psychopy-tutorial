from __future__ import division
import time
import sys
import random
import csv
import math
from numpy import linspace
from psychopy import visual,event,core



win = visual.Window([400,400], units='pix', monitor='testMonitor', color=[.4, .7, 1], colorSpace="rgb")
msPerFrame = visual.getMsPerFrame(win)[0]

square = visual.Rect(win,lineWidth=0,fillColor="red",size=[.2,.2],pos=[0,-.35], units="height")
grass = visual.Rect(win,lineWidth=0,fillColor=[30, 229, 15], fillColorSpace="rgb255",size=[2,.3],pos=[0,-.45], units="height")

numframes = 200
frames = linspace(0,math.pi,numframes)
count=0
minimum = -.35
maximum = .15
height = maximum + -minimum
while not event.getKeys(keyList=['q']):
	if count>=numframes:
		count=0

	x=frames[count]
	spos = height * math.sin(x)
	spos += minimum
	#ypos = starHeight * sin(x);
	square.setPos([0,spos])
	grass.draw()
	square.draw()
	win.flip()
	count += 1

sys.exit()