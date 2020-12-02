import random
import time
import pygame, sys
from pygame.locals import *

pygame.init()

def drawWall (wallX):
  amount = len(wallX)
  for i in range(0, amount):
    for a in range(wallX[i][0], wallX[i][2],30):
        window.blit(wallPicture, (a,wallX[i][1]))

def text_objects(text,font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def leftWon():
  text = font.render('Player One Won!', True, PINK)
  textredRect = text.get_rect()
  textX = window.get_width() / 2 - textredRect.width / 2
  textY = window.get_height() / 2 - textredRect.height / 2
  window.blit(text, [textX, textY])
  pygame.display.flip()
  time.sleep(5)
  pygame.quit()

def rightWon():
  text = font.render('Player Two Won!', True, PINK)
  textredRect = text.get_rect()
  textX = window.get_width() / 2 - textredRect.width / 2
  textY = window.get_height() / 2 - textredRect.height / 2
  window.blit(text, [textX, textY])
  pygame.display.flip()
  time.sleep(5)
  pygame.quit()

def drawLeftChar():
  global leftWalkCount
  
  if leftWalkCount + 1 >= 27:
    leftWalkCount = 0
  
  if leftPersonDirectionLeft: #til að teikna rétta átt á character
    window.blit(leftPersonWalkLeft[leftWalkCount//3], (leftPersonX-24,leftPersonY-42))
    leftWalkCount +=1
  elif leftPersonDirectionRight:
    window.blit(leftPersonWalkRight[leftWalkCount//3], (leftPersonX-26,leftPersonY-42))
    leftWalkCount +=1
  else:
    window.blit(leftChar, (leftPersonX-26,leftPersonY-47))

def drawRightChar():
  global rightWalkCount
  
  if rightWalkCount + 1 >= 27:
    rightWalkCount = 0
  
  if rightPersonDirectionLeft: #til að teikna rétta átt á character
    window.blit(rightPersonWalkLeft[rightWalkCount//3], (rightPersonX-24,rightPersonY-42))
    rightWalkCount +=1
  elif rightPersonDirectionRight:
    window.blit(rightPersonWalkRight[rightWalkCount//3], (rightPersonX-26,rightPersonY-42))
    rightWalkCount +=1
  else:
    window.blit(rightChar, (rightPersonX-26,rightPersonY-47))

def leftDied():
  global leftPersonX
  global leftPersonY
  global leftDeathCount 
  global leftShotCount
  leftDeathCount -= 1
  leftShotCount = 0
  leftPersonX = 500
  leftPersonY = 20
  leftPersonDirectionLeft = False
  leftPersonDirectionRight = False

def rightDied():
  global rightPersonX
  global rightPersonY
  global rightDeathCount
  global rightShotCount
  rightDeathCount -=1
  rightShotCount = 0
  rightPersonX = 500
  rightPersonY = 20
  rightPersonDirectionLeft = False
  leftPersonDirectionRight = False

def shoot(x,y):
  pygame.draw.line(window, RED, (x,y), (x, (y - 5)), 6)

window = pygame.display.set_mode((1000, 700), 0, 32)
pygame.display.set_caption('Lokaverkefni')

leftPersonWalkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
leftPersonWalkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('spaceBack.jpg')
leftChar = pygame.image.load('standing.png')
wallPicture = pygame.image.load('gras2.png')

rightPersonWalkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
rightPersonWalkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
rightChar = pygame.image.load('standing.png')

fps = 60
fpsClock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED =   (255 ,0, 0)
BLUE =  (0, 0, 255)
PINK =  (255, 192, 203)

color = BLACK

leftPersonJumping = False
leftJumpCount = 0

rightPersonJumping = False
rightJumpCount = 0

# þú átt að geta hoppað þegar þú tettur af, það er þannig í super smash bros sem er the inspiration for this game 

leftPersonDirectionLeft = False
leftPersonDirectionRight = False

rightPersonDirectionLeft = False
rightPersonDirectionRight = False

leftWalkCount = 0
rightWalkCount = 0

personSize = 10
leftPersonX = 355
leftPersonY = 380

rightPersonX = 595
rightPersonY = 380

xSpeedLeft = 0
ySpeedLeft = 0

xSpeedRight = 0
ySpeedRight = 0

leftDeathCount = 3
leftShotCount = 0

rightDeathCount = 3
rightShotCount = 0

showPlayer1X = leftPersonX
showPlayer1Y = leftPersonY + 100

showPlayer2X = rightPersonX
showPlayer2Y = rightPersonY + 100

leftShot = False
leftNew = True

rightShot = False
rightNew = True

wallWidth = 30

wallX = [[300,400,700,400], [190, 490, 250, 490], [760, 490, 810, 490], [ 300, 570, 450, 570], [550, 570, 720, 570],
          [760, 315, 810, 315 ],[190, 315, 250, 315], [550, 220, 720, 220], [ 300, 220, 450, 220]]

while True:
  window.blit(bg,(0,0))
  drawWall(wallX)

  if leftPersonY >= 700:
    leftDied()
  elif rightPersonY >= 700:
    rightDied()
  elif leftPersonX >= 1000:
    leftPersonX = 1000
  elif rightPersonX >= 1000:
    leftPersonX = 1000
  elif leftPersonX <= 0:
    leftPersonX = 0
  elif rightPersonX <= 0:
    rightPersonX = 0

  keys = pygame.key.get_pressed()

  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      pygame.quit()
      sys.exit()
    elif event.type == pygame.KEYDOWN:
        if (event.key == pygame.K_a):
          leftPersonDirectionRight = False
          leftPersonDirectionLeft = True
          xSpeedLeft = -1

        elif (event.key == pygame.K_d):
          leftPersonDirectionRight = True
          leftPersonDirectionLeft = False
          xSpeedLeft = 1

        elif (event.key == pygame.K_LEFT):
          rightPersonDirectionRight = False
          rightPersonDirectionLeft = True
          xSpeedRight = -1

        elif (event.key == pygame.K_RIGHT):
          rightPersonDirectionRight = True
          rightPersonDirectionLeft = False
          xSpeedRight = 1

        elif (event.key == K_SPACE):
          leftPersonJumping = True

        elif (event.key == pygame.K_UP):
          rightPersonJumping = True

        elif (event.key == pygame.K_q):
          leftShot = True

        elif(event.key == pygame.K_DOWN):
          rightShot = True

        elif event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
          
    elif event.type == KEYUP:
      if (event.key == K_a):
        leftPersonDirectionRight = False
        leftPersonDirectionLeft = False
        leftWalkCount = 0
        xSpeedLeft = 0

      elif (event.key == K_d):
        leftPersonDirectionRight = False
        leftPersonDirectionLeft = False
        leftWalkCount = 0
        xSpeedLeft = 0

      if (event.key == K_LEFT):
        rightPersonDirectionLeft = False
        rightPersonDirectionRight = False
        rightWalkCount = 0
        xSpeedRight = 0

      elif (event.key == K_RIGHT):
        rightPersonDirectionLeft = False
        rightPersonDirectionRight = False
        rightWalkCount = 0
        xSpeedRight = 0
      elif event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
    
  if leftPersonJumping == True:
    leftJumpCount += 1
    if leftJumpCount < 20:
      leftPersonY -= 7
    elif leftJumpCount >= 20 and leftJumpCount < 24:
      leftPersonY += 0
    elif leftJumpCount > 24:
      leftPersonY += 2

  if rightPersonJumping == True:
    rightJumpCount += 1
    if rightJumpCount < 20:
      rightPersonY -= 7
    elif rightJumpCount >= 20 and rightJumpCount < 24:
      rightPersonY += 0
    elif rightJumpCount > 24:
      rightPersonY += 2

  leftPersonX += xSpeedLeft
  leftPersonY += ySpeedLeft

  rightPersonX += xSpeedRight
  rightPersonY += ySpeedRight

  if rightDeathCount == 0:
    leftWon()

  elif leftDeathCount == 0:
    rightWon()

  if rightShotCount == 3:
    rightDied()

  if leftShotCount == 3:
    leftDied()

  fjx = len(wallX)
  if leftJumpCount == 0:
    leftPersonY += 2

  for i in range(0, fjx):
    if leftPersonY > wallX[i][1] - 14 and leftPersonY < wallX[i][3]+6 and leftPersonX > wallX[i][0] - 10 and leftPersonX <= wallX[i][2] + 1:
      leftPersonY -= 2
      leftPersonJumping = False
      leftJumpCount = 0
      
  if rightJumpCount == 0:
    rightPersonY += 2
  for i in range(0, fjx):
    if rightPersonY > wallX[i][1] - 14 and rightPersonY < wallX[i][3]+6 and rightPersonX > wallX[i][0] - 10 and rightPersonX <= wallX[i][2] + 1:
      rightPersonY -= 2
      rightPersonJumping = False
      rightJumpCount = 0

  if leftShot: 
    if leftNew:
      bulletDirection = leftPersonDirectionLeft
      bulletDirectionAgain = leftPersonDirectionRight
      shootX = leftPersonX + 15
      shootY = leftPersonY - 13

    if bulletDirection == True and bulletDirectionAgain == False:
      shoot(shootX, shootY)
      shootX -= 10
      leftNew = False

    elif bulletDirection == False and bulletDirectionAgain == True:
      shoot(shootX, shootY)
      shootX += 10
      leftNew = False

    elif bulletDirection == False and bulletDirectionAgain == False:
      leftShot = False

    if shootY < 0 or shootX < 0 or shootX > 1000:
      leftShot= False
      leftNew = True
      
    if rightPersonY-25 < shootY and rightPersonY + 20 > shootY and rightPersonX < shootX and rightPersonX + 25 > shootX:
      rightShotCount += 1
      leftShot = False
      leftNew = True
  
  if rightShot: 
    if rightNew:
      bulletDirection = rightPersonDirectionLeft
      bulletDirectionAgain = rightPersonDirectionRight
      shootX2 = rightPersonX + 15
      shootY2 = rightPersonY - 13

    if bulletDirection == True and bulletDirectionAgain == False:
      shoot(shootX2, shootY2)
      shootX2 -= 10
      rightNew = False

    elif bulletDirection == False and bulletDirectionAgain == True:
      shoot(shootX2, shootY2)
      shootX2 += 10
      rightNew = False

    elif bulletDirection == False and bulletDirectionAgain == False:
      rightShot = False

    if shootY2 < 0 or shootX2 < 0 or shootX2 > 1000:
      rightShot= False
      rightNew = True

    if leftPersonY - 25 <= shootY2 and leftPersonY + 20 >= shootY2 and leftPersonX <= shootX2 and leftPersonX + 25 >= shootX2:
      leftShotCount += 1
      rightShot = False
      rightNew = True

  text = font.render("Player One Lives: ", True, WHITE)
  text2 = font.render(str(leftDeathCount), True, WHITE)
  text_rect = text.get_rect()
  text_rect = text2.get_rect()
  text3 = font.render("Player Two Lives: ", True, WHITE)
  text4 = font.render(str(rightDeathCount), True, WHITE)
  text_rect = text3.get_rect()
  text_rect = text4.get_rect()

  
  window.blit(text, [10, 10])
  window.blit(text2, [222, 10])
  window.blit(text3, [10, 35])
  window.blit(text4, [222, 35])
  drawLeftChar()
  drawRightChar()
  pygame.display.update()
  fpsClock.tick(fps)

