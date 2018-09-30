import pygame
from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode((800,600))

keys = [False,False,False,False]
keepGoing = True
hasAcc = True
hasShift = False
hasPlayed = False
hasPlayed1 = False
hasClicked = False
hasCap = False

sharktimer = 100
sharktimer1 = 0
sharkspeed = 7
sharks = [[850,100,0]]

foodtimer = 200
foodtimer1 = 0
foods = [[850,300]]

sfishpos = [100,300]

state = 0
score = 0
shift = 5

name = ""

fontbig = pygame.font.SysFont("Times",40)
fontsmall = pygame.font.SysFont("Arial",30)
fontname = pygame.font.SysFont("Arial",50,True)

WHITE = (255,255,255)
PURPLE = (200,165,219)
RED = (230,0,0)
BLUE = (55,152,178)
GREEN = (113,232,224)
BLACK = (0,0,0)
YELLOW = (255,237,170)
ORANGE = (255,154,144)
DBLUE = (53,64,210)

##Load pics
sfish = pygame.image.load("saltyfish.PNG")
bgpic = pygame.image.load("bgpic.jpg")
shark = pygame.image.load("shark.PNG")
food = pygame.image.load("food.PNG")
firstimg = pygame.image.load("firstimg.jpg")
secondimg = pygame.image.load("secondimg.png")
endimg = pygame.image.load("endimg.png")
shark2 = pygame.image.load("shark2.PNG")
shark3 = pygame.image.load("shark3.PNG")
shark4 = pygame.image.load("shark4.PNG")
shark5 = pygame.image.load("shark5.PNG")
choice = pygame.image.load("choice.jpg")
sfish2 = pygame.image.load("salty fish2.PNG")
sfish3 = pygame.image.load("sfish3.PNG")
click = pygame.image.load("click.PNG")

click = pygame.transform.scale(click,(120,120))

sfish = pygame.transform.scale(sfish,(50,25))
sfish2 = pygame.transform.scale(sfish2,(50,30))
sfish3 = pygame.transform.scale(sfish3,(40,40))

sfishPics = [sfish,sfish2,sfish3]
indexsf = 0


shark = pygame.transform.scale(shark,(120,60))
shark2 = pygame.transform.scale(shark2,(100,80))
shark3 = pygame.transform.scale(shark3,(80,60))
shark4 = pygame.transform.scale(shark4,(100,75))
shark5 = pygame.transform.scale(shark5,(100,55))

sharkPics = [shark,shark2,shark3,shark4,shark5]



##Load sound
hitBorderSound = pygame.mixer.Sound("hitBorder.wav")
hitFoodSound = pygame.mixer.Sound("hitFood.wav")
hitSharkSound = pygame.mixer.Sound("hitShark.wav")
gameOverSound = pygame.mixer.Sound("gameOver.wav")
bgm = pygame.mixer.Sound("Salty fish.wav")






# -------------------------------------------------------------------
while keepGoing:

    if state == 0:

        #Reset
        sharktimer = 100
        sharktimer1 = 0
        sharkspeed = 7
        sharks = [[850,100,0]]

        foodtimer = 200
        foodtimer1 = 0
        foods = [[850,300]]

        sfishpos = [100,300]

        score = 0
        name = ""
        
        firstimg = pygame.transform.scale(firstimg,(800,600))
        screen.blit(firstimg,(0,0))
        
    elif state == 1:
        secondimg = pygame.transform.scale(secondimg,(800,600))
        screen.blit(secondimg,(0,0))


    elif state == 2:
        choice = pygame.transform.scale(choice,(800,600))
        screen.blit(choice,(0,0))

        name_print = fontname.render(name,True,BLACK)
        screen.blit(name_print,(150,450))

        ##Click
        if hasClicked:
            if indexsf == 0:
                screen.blit(click,(150,150))
            elif indexsf == 1:
                screen.blit(click,(385,150))
            elif indexsf == 2:
                screen.blit(click,(635,150))


        
    elif state == 3:

        if hasPlayed == False:
            bgm.play()
            hasPlayed = True
        
        sharktimer -= 1
        foodtimer -= 1

        screen.fill((0,0,0))

        ##Bgpic
        bgpic = pygame.transform.scale(bgpic,(800,600))
        screen.blit(bgpic,(0,0))

        t = fontsmall.render("Your score is "+str(score),True,(0,0,0))
        screen.blit(t,(600,530))
        title = fontbig.render("Hello, "+name+"! Welcome to SALTY FISH's world!",True,DBLUE)
        name_rect = title.get_rect()
        name_rect.centerx = screen.get_rect().centerx
        name_rect.y = 30
        screen.blit(title,name_rect)

        ##Draw the salty fish
        screen.blit(sfishPics[indexsf],sfishpos)

        ##Draw the shark
        if sharktimer == 0:
            num = random.randint(0,4) #number of sharks
            sharks.append([850,random.randint(60,540),num])
            sharktimer = 100 - (sharktimer1*2)
            if sharktimer1 >= 40: #shark max number
                sharktimer1 = 40
            else:
                sharktimer1 += 7

        sfish_rect = pygame.Rect(sfish.get_rect())
        sfish_rect.left = sfishpos[0]
        sfish_rect.top = sfishpos[1]



            #Delete shark when out of range
        index = 0
        for s in sharks:
            if s[0] <= -100:
                sharks.pop(index)
            s[0] -= sharkspeed #shark speed

            #Check for collisions
            
            for sha in sharks:
                sha_rect = pygame.Rect(shark.get_rect())
                sha_rect.left = sha[0]
                sha_rect.top = sha[1]
                
                if sfish_rect.colliderect(sha_rect):
                    hitSharkSound.play()
                    state = 4

            index += 1

            #Draw
        for s in sharks:
            screen.blit(sharkPics[s[2]],(s[0],s[1]))


        ##Draw the food
        if foodtimer == 0:
            foods.append([920,random.randint(60,540)])
            foodtimer = 200 - (foodtimer1*2)
            if foodtimer1 >= 35: #food max number
                foodtimer1 = 35
            else:
                foodtimer1 += 5

            #Delete food when out of range
        indexf = 0
        for f in foods:
            if f[0] <= -100:
                foods.pop(indexf)
            f[0] -= 4 #food speed

            #Check for collision
            index1 = 0
            for foo in foods:
                foo_rect = pygame.Rect(food.get_rect())
                foo_rect.left = foo[0]
                foo_rect.top = foo[1]
                
                if sfish_rect.colliderect(foo_rect):
                    hitFoodSound.play()
                    score += 1
                    foods.pop(index1)
            
            indexf += 1

            #Draw
        for f in foods:
            food = pygame.transform.scale(food,(15,15))
            screen.blit(food,f)

        ##Accelerates shark when gets 10 points
        if (score)%5 == 1:
            hasAcc = False
        if (score)%5 == 0 and hasAcc == False:
            sharkspeed += 2
            hasAcc = True
            
        ##Check if the salty fish go out of range
        if sfishpos[0] <= -1 or sfishpos[0] >= 751 or sfishpos[1] <= -1 or sfishpos[1] >= 576:
            hitBorderSound.play()
            state = 4

    elif state == 4:
        bgm.stop()
        endimg = pygame.transform.scale(endimg,(800,600))
        screen.blit(endimg,(0,0))
        t = fontsmall.render("Your score is "+str(score),True,RED)
        screen.blit(t,(300,100))

        #-----------------------------------------------

    for event in pygame.event.get():
        if event.type == QUIT:
            keepGoing = False
        if event.type == pygame.KEYDOWN:
            if state == 0 or state == 1:
                if event.key == K_SPACE:
                    state += 1
            elif state == 2:
                if event.key == K_LSHIFT or event.key == K_RSHIFT:
                    hasCap = True
                if event.key == K_RETURN:
                    
                    state += 1
                elif event.key == K_1 :
                    indexsf = 0
                    hasClicked = True
                elif event.key == K_2 :
                    indexsf = 1
                    hasClicked = True
                elif event.key == K_3 :
                    indexsf = 2
                    hasClicked = True
                elif event.key >= 48 and event.key <= 122:
                    if hasCap:
                        name += chr(event.key-32)
                    else:
                        name += chr(event.key)
                    #Delete wrong letter
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                
            elif state == 3:
                if event.key==K_UP:
                    keys[0]=True
                elif event.key==K_LEFT:
                    keys[1]=True
                elif event.key==K_DOWN:
                    keys[2]=True
                elif event.key==K_RIGHT:
                    keys[3]=True
                elif event.key == K_LSHIFT or event.key == K_RSHIFT:
                    hasShift = True
                
            
            
            if event.key == K_F1 and state == 4:
                state = 0
                hasPlayed = False
                hasPlayed1 = False
                hasClicked = False
                
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False
            elif (event.key == K_LSHIFT or event.key == K_RSHIFT) and state == 3:
                hasShift = False
            if (event.key == K_LSHIFT or event.key == K_RSHIFT) and state == 2:
                hasCap = False
            


    ##Move the fish
    if hasShift:
        shift = 10
    else:
        shift = 5
    if keys[0]:
        sfishpos[1]-=shift
    elif keys[2]:
        sfishpos[1]+=shift
    if keys[1]:
        sfishpos[0]-=shift
    elif keys[3]:
        sfishpos[0]+=shift

    pygame.display.update()





pygame.quit()




    
