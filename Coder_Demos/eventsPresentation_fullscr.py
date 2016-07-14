from __future__ import division
from psychopy import visual,event,core
import time
import sys
import random
import csv
import math
from numpy import linspace

win = visual.Window([1366, 768], units='height', fullscr=True, monitor='testMonitor', color=[74, 196, 237], 
	colorSpace="rgb255")

square = visual.Rect(win,lineWidth=0,fillColor="red",size=[.2,.2],pos=[0,-.35], 
	units="height")
grass = visual.Rect(win,lineWidth=0,fillColor=[30, 229, 15], fillColorSpace="rgb255",
	size=[5,.3],pos=[0,-.45], units="height")

numframes = 200
#numframes is the number of frames for each jump
framesArray = linspace(0,math.pi,numframes)
#frames is the list of points used to calculate the square's height.
#It's an array that contains numframes points, spaced equally from 0 to pi
#This is to accomodate the sine curve used to plot these points.
count=0
#count is an iterater
minimum = -.35
#The minimum point is the lowest point the square will be at.
maximum = .15
#The maximum point is the highest point the square will be at.
height = abs(maximum) + abs(minimum)
#the height is the full distance the square will traverse

parametersfile = open('eventsparameters.csv', 'r')
parametersreader = csv.DictReader(parametersfile)
responsefile = open('eventsresponses.csv', 'wb')
responsefields = ['Response', 'RT']
responsewriter = csv.DictWriter(responsefile, responsefields)
responsewriter.writeheader()
timer = core.Clock()

for trial in parametersreader:
	height = float(trial['height'])
	square.fillColor = trial['color']
	#Set parameters
	count = 0
	#Reset the iterater at the start of each trial
	while not event.getKeys(keyList=['q']):
	#We'll stay in this while loop until the user presses 'q'
		if count>=numframes:
			count=0
			#Resets the iterater
			core.wait(.25)
		x=framesArray[count]
		#x grabs the corresponding point between 0 and pi
		squarepos = (height * math.sin(x)) + minimum
		#The position for the square is:
		#   the point on the sine curve (which is between 0 and 1)
		#  *the maximum height (so how hight it is depends on the sine curve fraction)
		#  +minimum (so that it accounts for the position is started at; in our case, it's lower)
		square.setPos([0,squarepos])
		#We change the position of the square object to new position
		grass.draw()
		square.draw()
		#Then redraw our shapes
		win.flip()
		#And then put them on-screen!
		count += 1
		#Finally, we increment our iterator so we calculate a new number on the next run

	#Response screen
	background = visual.Rect(win,lineWidth=0,fillColor="black",size=[5,5],pos=[0,0], 
	units="height")
	#Cover up the background with black; the square should be the same size as the window
	responseText = visual.TextStim(win,text='Was that cool?', height=.05, units="height", 
		color='white',pos=[0,0])
	promptText = visual.TextStim(win,text='Press f for yes and j for no',
		height=.025, color='white',pos=[0,-.25], units="height")
	background.draw()
	responseText.draw()
	promptText.draw()
	#Create the text, then draw it.
	win.flip()
	timer.reset()
	#start the timer
	while True:
		response=event.waitKeys(keyList=['f','j'])[0]
		break
		#Wait for a response, and leave the loop when you have it
	rt = timer.getTime()
	responsewriter.writerow({'Response': response, 'RT': rt})
	#Write the row of data

		


parametersfile.close()
responsefile.close()
sys.exit()