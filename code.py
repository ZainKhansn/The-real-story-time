import pygame
import time
import replit
import threading
import random
import numpy as np
pygame.init()
replit.clear()
flag4 = True
flag3 = True
X = 300
Y = 100
day_night = 1
BLUE = (0, 0, 255)
RED = (255, 0, 0)
des = 0
green = (0, 255, 0)
size = 3
background_col = (0,32,68)
brown = (101, 67, 33)
BLACK = (0, 0, 0) 
green = (0, 100, 0)
image = pygame.image.load(r'camp_fire.png')
SPcolor = tuple(np.random.randint(30, 255, size))
tim = random.randint(6, 14)
cause = 0

def split(word):
  return [char for char in word]
score_font = pygame.font.SysFont("Times New Roman", 20)
width = 540
height = 280 
screen = pygame.display.set_mode((width, height))

def background():
  

  global des
  pygame.display.set_caption("Story")
  replit.clear()
  print("Instructions: \n 1.Expand your screen to make it bigger. \n 2. Press on the screen to move the character with W,A,S,D\n 3. Lastly Be careful dont make any mistake")
  time.sleep(7)
  replit.clear()
  instruct = input("Do you get the instructions?(Y/N)")
  if instruct == "Y":
    print("OK lets continue")
    time.sleep(3)
  if instruct == "N":
  
    print("Well that sucks lets continue")
    time.sleep(3)
  else:
    time.sleep(3)
    print("That sucks lets continue")
  replit.clear()
  print("Congratualations it is april break and you are going to Hawaii!")
  print("During the first hour of the flight everything is fine but then...")
  time.sleep(7)
  replit.clear()
  print("The plane crashes and..")
  time.sleep(3)
  replit.clear()
  print("You wake up on an island and find yourself stranded alone!!!")
  time.sleep(5)
  replit.clear()
  des = input("Do you wonder around(1)\n or stay put and walk around your island?(2)")
  time.sleep(2)
  replit.clear()
  if des == "1":
    print("From the impact of the plane crash you and the rest of the passengers passed away:(.")
    time.sleep(1)
  if des =="2":
    print("Ok stay on the island and find resources to live- Item 1, 2, 3")
    

    
  elif des != "1" or des != "2":
    print("pick 1 or 2(restart program)")
    time.sleep(1)
    quit()
items = 0    
let = 0

b = threading.Thread(target=background)
ti = 3
def te():

  global let
  global tim
  global cause
  for letter in fire_camp:

    letter = str(letter)
    f = input("Press " + letter + "!: ")
    let+=1
    if tim == 0 and let < 8 or letter != f:
      cause = 1
      #print(str(cause) + " cause = 1")
      print("You did not make it in time finish the building before it gets dark or pressed the wrong button!")
      time.sleep(4)
      replit.clear()
    if tim > 0 and let == 9:
      cause = 2
      #print(str(cause) + " cause = 2")
      print("You did it now you will have a safe shelter and fire during the night")
    if f == letter:
      continue
  
def tme_counter():
  global tim
  global let
  for i in range(tim):  
    time.sleep(1)
    tim -= 1

def causeing():
  global cause
  global X10
  global base
  global ply
  global helicopter
  if sin == 3:
          
    screen.fill(background_col)
    base = pygame.draw.rect(screen, brown, pygame.Rect(120, 15, 320, 250))
    ply = pygame.draw.rect(screen, SPcolor, pygame.Rect(X, Y, 10, 10))
    helicopter = pygame.draw.rect(screen, BLACK, pygame.Rect(X10, Y10, 20, 20))  
    X10+=1  

cau = threading.Thread(target=causeing) 
times = threading.Thread(target=tme_counter)      
x = threading.Thread(target=te)
z = 5
if z == 5:
  b.start()
if z == 6:
  x.start()
  times.start()
if z == 7:
  cau.start()
lives = 10

flag2 = True
flags5 = True
flag1 = True
flags6 = True
flags7 = True
flags8 = True
flags9 = True
tim1 = 3
X10 = -20
Y10 = 150
while True:
  Health = score_font.render("Health: " + str(lives), True, BLACK)

  if z == 5:
    t = score_font.render("Time left " + str(tim1), True, brown)
    item = score_font.render("ITEMS FOUND: " + str(items), True, BLACK)
  screen.fill(background_col)
  x1 = width / 2 + 90
  y1 = height / 2 + 115
  x2 = width / 2
  y2 = height / 2
  x3 = width /2 + 125
  y3 = height/2 + 100
  helicopter = pygame.draw.rect(screen, BLACK, pygame.Rect(X10, Y10, 20, 20))  
  base = pygame.draw.rect(screen, brown, pygame.Rect(120, 15, 320, 250))
  ply = pygame.draw.rect(screen, SPcolor, pygame.Rect(X, Y, 10, 10))
  

  
  textRect = item.get_rect()
  textRect3 = item.get_rect()
  textRect.center = (x1, y1) 
  textRect4 = Health.get_rect()
  textRect4.center = (x3, y3) 
  textRect3.center = (x2, y2) 
  screen.blit(Health, textRect4)
  if des == "1":
    time.sleep(1)
    quit()
  if des == "2" and flags5:
    flags5 = False
    print("+ 4 Health")
    lives += 4
  if des == "2":
    
    

    screen.blit(item, textRect)
    screen.blit(t, textRect)
    screen.blit(Health, textRect4)
    sticks = pygame.draw.rect(screen, brown, pygame.Rect(200, 100, 5, 40))
    water = pygame.draw.rect(screen, brown, pygame.Rect(300, 50, 30, 40))

    fire = pygame.draw.rect(screen, brown, pygame.Rect(230, 15, 40, 40))
    
    if ply.colliderect(fire) and flags9:
      flags9 = False
      fire = pygame.draw.rect(screen, RED, pygame.Rect(230, 15, 40, 40))
      items+=1
      print("You have found sparks!")
      print("Health +2")
      lives += 2
  
    if ply.colliderect(fire):
      fire = pygame.draw.rect(screen, RED, pygame.Rect(230, 15, 40, 40))

    
    if ply.colliderect(water) and flag3:
      flag3 = False
      water = pygame.draw.rect(screen, BLUE, pygame.Rect(300, 50, 30, 40))
      items+=1
      print("You have found water!")
      print("Health +2")
      lives += 2
    if ply.colliderect(water):
      water = pygame.draw.rect(screen, BLUE, pygame.Rect(300, 50, 30, 40))

          
    if ply.colliderect(sticks) and flag1:
      flag1 = False
      sticks = pygame.draw.rect(screen, BLACK, pygame.Rect(200, 100, 5, 40))
      items +=1
      print("You have found sticks!")
      print("Health +2")
      lives += 2
    if ply.colliderect(sticks):
      sticks = pygame.draw.rect(screen, BLACK, pygame.Rect(200, 100, 5, 40))
    
    ti = 3




    if items == 3:
      fire = pygame.draw.rect(screen, RED, pygame.Rect(230, 15, 40, 40))
      sticks = pygame.draw.rect(screen, BLACK, pygame.Rect(200, 100, 5, 40))
      water = pygame.draw.rect(screen, BLUE, pygame.Rect(300, 50, 30, 40))
      replit.clear()
      print("Okay now press a series of combinations to build a camp and a fire before the time runs out!")
      times.start()

# Driver code\

      fire_camp = "fire_camp"
      z = 6
      
      if z == 6:
        t = score_font.render("Time GIVEN: " + str(tim), True, BLACK)
        item = score_font.render("ITEM FOUND: " + str(items), True, brown)


        items+= 1
        
        x.start()
    
    if cause == 1:
      screen.fill(BLACK)
      t = score_font.render("Time GIVEN: " + str(tim), True, BLACK)
      ply = pygame.draw.rect(screen, SPcolor, pygame.Rect(X, Y, 10, 10))
      
    if cause ==1 and flags7:
      flags7 == False
      print("-10 health")
      lives -= 20
      if lives <= 0:
        print("Oh Oh you ran out of lives")
        time.sleep(5)
        for i in range(1, 101):
          i = int(i)
          i+=1
          i = str(i)
          print("Program terminating in " + i +"%." )
          time.sleep(.06)
          replit.clear()
        pygame.quit()
    if cause == 2:
      
      t = score_font.render("Time GIVEN: " + str(tim), True, BLACK)
      percent = day_night / 3000 
      sume = percent * 100
      sume = str(sume)
      if cause ==2:
        print(sume + " %  until day")
        sume = float(sume)
      #change
      time.sleep(.0000001)
      replit.clear()
      screen.fill(BLACK)
      image = pygame.transform.scale(image, (120, 90))
      screen.blit(image, (textRect3))
      

      ply = pygame.draw.rect(screen, SPcolor, pygame.Rect(X, Y, 10, 10))
      day_night += 1
      if sume >= 100:
        flags10 = True
        cause = 3
        fin = 3
        sin = 3
        z = 7
        if z == 7:
          cau.start()
        if fin == 3 and flags6:
          flags6 = False
          print("It is still night and you got lots of good sleep but what is that sound?(+4 health)")
          lives += 4
          hel =1
 

        
  
        if cause == 3 and flags8:
          flags8 = False
          print("Look up it is a helicopter passing by!")
          wave = input("Do you wave with one or two hands(1 or 2): ")
          if wave == "1":
            print("The pilot circled around the island for a few seconds and left because the pilot thought you were a wacko waving at him.")
            time.sleep(10)
            print("Oh Oh you ran out of lives")
            time.sleep(2)
            for i in range(1, 101):
              i = int(i)
              i+=1
              i = str(i)
              print("Program terminating in " + i +"%." )
              time.sleep(.006)
              replit.clear()
            pygame.quit()
          if wave == "2":
            screen.fill(green)
          if wave == "2":
            
            print("Congrats that is the international emergency hand signal for (save me) so the helicopter circled around the island and saved you (+100000 health)")
            time.sleep(10)
            
            for i in range(1, 101):
              i = int(i)
              i+=1
              i = str(i)
              print("Program terminating in " + i +"%." )
              time.sleep(.06)
              replit.clear()
            pygame.quit()
           
          
        
  event = pygame.event.poll()

  if event.type == pygame.KEYDOWN:
  
    if event.key == pygame.K_w:
      Y -= 10
  
  
    if event.key == pygame.K_s:
      Y += 10
  
      
    if event.key == pygame.K_a:
      X -= 10
  
  
    if event.key == pygame.K_d:
      X += 10


  pygame.display.update()
      
     
