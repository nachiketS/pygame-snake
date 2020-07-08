import random
import pygame
pygame.init()

win = pygame.display.set_mode((480,480))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

foodxy = [random.randrange(0,480,24),random.randrange(0,480,24)]
down = pygame.image.load('snakeheadd.png')
up = pygame.image.load('snakeheadu.png')
left = pygame.image.load('snakeheadl.png')
right = pygame.image.load('snakeheadr.png')
body = pygame.image.load('body.png')

class snakex(object):
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.val = 24
		self.runCount = 0
		self.direction = 'down'
		self.length = 1	
		self.prevx = x
		self.prevy = y
		self.tempx = x
		self.tempy = y
		self.xl = [self.x]*self.length
		self.yl = [self.y]*self.length 
		self.xy = [[0,0]] * self.length
		self.moveCounter= 0
		self.snakehead = down 

	def draw(self, win):
		win.fill((0,0,0))
		
			# return True
		
		# pygame.draw.rect(win,(0,128,0),(self.x,self.y,snek.width,snek.height))
		win.blit(self.snakehead,(self.x,self.y))
		# pygame.draw.rect(win,(100,0,100),(self.xl[1],self.yl[1],snek.width,snek.height))
		# pygame.draw.rect(win,(100,0,100),(self.xl[0],self.yl[0],snek.width,snek.height))

		for i in range(self.length-1,-1,-1):
			win.blit(body,(self.xy[i][0],self.xy[i][1]))
			# pygame.draw.rect(win,(0,150,0),(self.xy[i][0],self.xy[i][1],snek.width,snek.height))
		self.xy.append([self.x,self.y])
		self.yl.append(self.y)
		self.xy.pop(0)
		self.yl.pop(0)
		# self.xl[0] = self.xl[1]
		# self.yl[0] = self.yl[1]
		# self.xl[1] = self.x
		# self.yl[1] = self.y

		# self.xl[2] = 
		# self.yl[2] = 
		# self.tempx = self.prevx
		# self.tempy = self.prevy	
		# self.prevx = self.x
		# self.prevy = self.y
		print("x",self.x,self.xl)
		print("y",self.y,self.yl)
		pygame.draw.rect(win,(255,255,0),(foodxy[0],foodxy[1],24,24))

		pygame.display.update()

	def random_generator(self):
		new = [random.randrange(0,480,24), random.randrange(0,480,24)]
		if new in self.xy:
			return self.random_generator()
		return new

	
snek = snakex(48,48,24,24)
run = True
while run:
	clock.tick(5)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	# win.blit(surface,(0,0))
		if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			if snek.direction == 'left':
				snek.direction = 'left'
			else:
				snek.direction = 'right'
				snek.snakehead = right

		if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			if snek.direction == 'right':
				snek.direction = 'right'
			else:
				snek.direction = 'left'
				snek.snakehead = left

		if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			if snek.direction == 'down':
				snek.direction = 'down'
			else:
				snek.direction = 'up'
				snek.snakehead = up

		if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			if snek.direction =='up':
				snek.direction = 'up'
			else:	
				snek.direction = 'down'
				snek.snakehead = down


	if snek.direction == 'down':
		snek.y+=snek.val
		if([snek.x,snek.y] in snek.xy):
			print("Game Over")
			run =  False
		if(snek.y > 480):
			print('Game Over')
			run = False
			# return True
	if snek.direction == 'up':
		snek.y-=snek.val
		if ([snek.x,snek.y] in snek.xy):
			print("Game Over")
			run = False
		if(snek.y < 0):
			print('Game Over')
			run = False
			# return True
	if snek.direction == 'left':
		snek.x-=snek.val
		if ([snek.x,snek.y] in snek.xy):
			print("Game Over")
			run = False
		if snek.x < 0 :
			run = False
			print('Game Over')

			# return True
	if snek.direction == 'right':
		snek.x+=snek.val
		if([snek.x,snek.y] in snek.xy):
			print("Game Over")
			run  = False
		if(snek.x >= 480):
			print("Game Over")
			run = False
	if [snek.x,snek.y] == foodxy:
		foodxy = snek.random_generator()
		snek.length+=1
		snek.xy.append([snek.x,snek.y])
	# keys = pygame.key.get_pressed()
	# if keys[pygame.K_LEFT]:
	# 	# snek.x-=snek.val
	# 	snek.direction = 'left'
	# 	if snek.x<0:
	# 		run = False
	# # if keys[pygame.K_RIGHT]:
	# # 	# snek.x+=snek.val
	# # 	snek.direction = 'right'
	# # 	if snek.x>500-snek.width:
	# # 		run = False
	# if keys[pygame.K_UP]:
	# 	# snek.y-=snek.val
	# 	snek.direction = 'up'
	# 	if snek.y<0:
	# 		run = False
	# if keys[pygame.K_DOWN]:
	# 	# snek.y+=snek.val
	# 	snek.direction = 'down'
	# 	if snek.y>500 - snek.height:
	# 		run = False
	# pygame.draw.rect(win,(100,255,100),(snek.x,snek.y,snek.width,snek.height))
	# pygame.display.update()
	snek.draw(win)
	# if not(snek.draw(win)):
	# 	run = False
