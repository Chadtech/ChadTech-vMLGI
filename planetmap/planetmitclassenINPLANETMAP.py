import os
import pygame
import math

pygame.init()

pygame.font.Font('Command-Prompt-12x16.ttf',16)
screen = pygame.display.set_mode((1600,800))
pygame.display.set_caption("ChadTech vMoonlanderGI")
clock = pygame.time.Clock()

class object:

	def __init__(self,xPos,yPos,xCor,yCor,xVel,yVel,angle,rotation,temp,weight,image):
		self.xPos=xPos
		self.yPos=yPos
		self.xCor=xCor
		self.yCor=yCor
		self.xVel=xVel
		self.yVel=yVel
		self.angle=angle
		self.rotation=rotation
		self.temp=temp
		self.weight=weight
		self.image=image

		self.image.set_colorkey((0,0,0,255))

	def distanceFromLander(self):
		return (((lander.xPos-self.xPos)**2)+((lander.yPos-self.yPos)**2))**(0.5)

lander = object(1200,1200,65200,65200,0,0,0,0,128,1000,pygame.image.load('lander5.png').convert())

weakThrustPower =0.005
mainThrustPower =0.035
weakThrustRotate=0.005

class world:

	def __init__(self,xTile,yTile,background,frame,hud,minimap):
		self.xTile=xTile
		self.yTile=yTile

		self.background = background
		self.frame = frame
		self.hud = hud
		self.minimap = minimap

		self.hud.set_colorkey((0,0,0,255))

theWorld = world(2,2,
	pygame.image.load('allthatisthecase.png').convert(),
	pygame.image.load('quadrants.png').convert(),
	pygame.image.load('hud4.png').convert(),
	pygame.image.load('minimap.png').convert()
	)

scanlines = pygame.image.load('scanlines.png').convert()
scanlines.set_colorkey((0,0,0,255))

#quadFou= pygame.image.load(str(theWorld.xTile)+'x'+str(theWorld.yTile)+'.png').convert()
#quadThe= pygame.image.load(str(theWorld.xTile-1)+'x'+str(theWorld.yTile)+'.png').convert()
#quadTwo= pygame.image.load(str(theWorld.xTile-1)+'x'+str(theWorld.yTile-1)+'.png').convert()
#quadOne= pygame.image.load(str(theWorld.xTile)+'x'+str(theWorld.yTile-1)+'.png').convert()

def worldBlit(quadTwo,quadOne,quadThe,quadFou,window):
	window.blit(quadTwo,[0,0])
	window.blit(quadOne,[800,0])
	window.blit(quadThe,[0,800])
	window.blit(quadFou,[800,800])

def quadUpdate():
	global quadFou
	global quadThe
	global quadTwo
	global quadOne

	global theWorld

	theWorld.xTile = int(lander.xCor)/800 +1
	theWorld.yTile = int(lander.yCor)/800 +1


	quadFou= pygame.image.load(str(theWorld.yTile)+'x'+str((theWorld.xTile))+'.png').convert()
	quadThe= pygame.image.load(str((theWorld.yTile-1))+'x'+str((theWorld.xTile))+'.png').convert()
	quadTwo= pygame.image.load(str((theWorld.yTile-1))+'x'+str((theWorld.xTile-1))+'.png').convert()
	quadOne= pygame.image.load(str(theWorld.yTile)+'x'+str((theWorld.xTile-1))+'.png').convert()

quadUpdate()

blast_strafe = pygame.image.load('blast_strafe.png').convert()
blast_yaw = pygame.image.load('blast_yaw.png').convert()
blast_main = pygame.image.load('blast_main.png').convert()

landinggear = pygame.image.load('landinggear.png').convert()

landinggear.set_colorkey((0,0,0,255))
blast_main.set_colorkey((0,0,0,255))

worldBlit(quadTwo,quadOne,quadThe,quadFou,theWorld.frame)

rungame = True

LF=False
LS=False
LB=False

RF=False
RS=False
RB=False

mainThrust = False

while rungame:
	for event in pygame.event.get():
		pressed = pygame.key.get_pressed()

		if event.type == pygame.KEYDOWN:

			if event.key==pygame.K_w:
				LB=True
			if event.key==pygame.K_a:
				LS=True
			if event.key==pygame.K_c:
				LF=True
			if event.key==pygame.K_u:
				RB=True
			if event.key==pygame.K_k:
				RS=True
			if event.key==pygame.K_b:
				RF=True

			if event.key==pygame.K_f:
				print 'Velocity in (x,y)', int(lander.xVel*1000) ,int(lander.yVel*1000), 'ANGLE', lander.angle%360, '(x,y) coordinates', int(lander.xCor), int(lander.yCor)
			if event.key==pygame.K_SPACE:
				mainThrust=True

			if event.key==pygame.K_ESCAPE:
				rungame=False


		if event.type == pygame.KEYUP:

			if event.key==pygame.K_w:
				LB=False
			if event.key==pygame.K_a:
				LS=False
			if event.key==pygame.K_c:
				LF=False
			if event.key==pygame.K_u:
				RB=False
			if event.key==pygame.K_k:
				RS=False
			if event.key==pygame.K_b:
				RF=False
			if event.key==pygame.K_SPACE:
				mainThrust=False


	if event.type == pygame.QUIT:
		rungame=False

	lander.image = pygame.image.load('lander5.png').convert()

	if mainThrust:
		lander.xVel-=(mainThrustPower*math.sin(math.radians(lander.angle)))
		lander.yVel-=(mainThrustPower*math.cos(math.radians(lander.angle)))
		lander.image.blit(blast_main,[63,85])

	if LB:
		lander.xVel-=(weakThrustPower*math.sin(math.radians(lander.angle)))
		lander.yVel-=(weakThrustPower*math.cos(math.radians(lander.angle)))
		lander.rotation-=weakThrustRotate
		lander.image.blit(pygame.transform.flip(blast_yaw,False,True),[45,72])

	if LS:
		lander.yVel+=(weakThrustPower*math.sin(math.radians(lander.angle)))
		lander.xVel-=(weakThrustPower*math.cos(math.radians(lander.angle)))
		lander.image.blit(pygame.transform.flip(blast_strafe,True,False),[94,67])

	if LF:
		lander.yVel+=(weakThrustPower*math.cos(math.radians(lander.angle)))
		lander.xVel+=(weakThrustPower*math.sin(math.radians(lander.angle)))
		lander.rotation+=weakThrustRotate
		lander.image.blit(pygame.transform.flip(blast_yaw,False,False),[45,57])

	if RB:
		lander.yVel-=(weakThrustPower*math.cos(math.radians(lander.angle)))
		lander.xVel-=(weakThrustPower*math.sin(math.radians(lander.angle)))
		lander.rotation+=weakThrustRotate
		lander.image.blit(pygame.transform.flip(blast_yaw,True,True),[92,72])
	if RS:
		lander.yVel-=(weakThrustPower*math.sin(math.radians(lander.angle)))
		lander.xVel+=(weakThrustPower*math.cos(math.radians(lander.angle)))
		lander.image.blit(pygame.transform.flip(blast_strafe,False,False),[36,67])

	if RF:
		lander.yVel+=(weakThrustPower*math.cos(math.radians(lander.angle)))
		lander.xVel+=(weakThrustPower*math.sin(math.radians(lander.angle)))
		lander.rotation-=weakThrustRotate
		lander.image.blit(pygame.transform.flip(blast_yaw,True,False),[92,57])

	#lander.image.blit(landinggear,[42,74])

	lander.xPos+=lander.xVel
	lander.yPos+=lander.yVel

	lander.xCor+=lander.xVel
	lander.yCor+=lander.yVel

#	if lander.yPos>1140 and theWorld.yTile==3:
#		lander.yPos=1140
#		lander.yVel=0
#		lander.xVel=0
#ff		lander.rotation=0

	if lander.yPos<=400:
		lander.yPos=1200
		if theWorld.yTile!=1:
			theWorld.yTile-=1

		quadUpdate()

		worldBlit(quadTwo,quadOne,quadThe,quadFou,theWorld.frame)

	if lander.yPos>1200:
		lander.yPos=400
		theWorld.yTile+=1

		quadUpdate()

		worldBlit(quadTwo,quadOne,quadThe,quadFou,theWorld.frame)

	if lander.xPos<=400:
		lander.xPos=1200
		theWorld.xTile-=1

		print theWorld.xTile

		quadUpdate()

		worldBlit(quadTwo,quadOne,quadThe,quadFou,theWorld.frame)

	if lander.xPos>1200:
		lander.xPos=400
		theWorld.xTile+=1 

		quadUpdate()

		worldBlit(quadTwo,quadOne,quadThe,quadFou,theWorld.frame)

	#lander.yVel+= 25/(2000-lander.yPos)

	lander.angle+=lander.rotation

	worldX, worldY = pygame.transform.rotate(theWorld.background,lander.angle).get_size()
	worldX = worldX/2 
	worldY = worldY/2

	lander.image.set_colorkey((0,0,0,255))

	# below. However the line of code below might still be important later
	# frame.blit(pygame.transform.rotate(lander,angle),[cordX-landX,cordY-landY])

	theWorld.background.blit(theWorld.frame,[-lander.xPos+400,-lander.yPos+400])

	screen.blit(pygame.transform.rotate(theWorld.background,-lander.angle),[(800-worldX),400-worldY])
	screen.blit(lander.image,[731,331])
	screen.blit(theWorld.hud,[0,0])

	# Minimap
	screen.blit(theWorld.minimap,[1272,2])
	screen.set_at((1274+(int(lander.xCor/800)),4+(int(lander.yCor/800))),(255,255,255))

	#Read outs
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> (x,y) Pos  = ('+str(int(theWorld.xTile))+','+str(int(theWorld.yTile))+')',False,(255,255,255)),[1270,333])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Velocity   = '+str(int(10*(((lander.yVel**2)+(lander.xVel**2))**(0.5)))),False,(255,255,255)),[1270,349])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Ang Vel    = '+str(lander.rotation*10),False,(255,255,255)),[1270,365])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Angle      = '+str(int(lander.angle%360)),False,(255,255,255)),[1270,381])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Temp       = '+str(lander.temp),False,(255,255,255)),[1270,397])

	#Scan Lines
	screen.blit(scanlines,[0,0])

	pygame.display.flip()
	clock.tick(60)

pygame.quit()


# Numerate Files
# Directory Stuff