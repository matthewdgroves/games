import pygame, random, sys
from pygame.locals import *

windowWidth = 600
windowHeight = 600
textColor = (0, 0, 0)
backgroundColor = (210, 230, 255)
FPS = 60
baddieMinSize = 70
baddieMaxSize = 90
baddieMinSpeed = 6
baddieMaxSpeed = 10
addNewBaddieRate = 40
playerMoveRate = 6 
RED = (255, 0, 0)


#the baddie min size makes it so the baddies are not microscopic and baddie max makes them so they are not huge. By increasing the baddie min size and max size the game would get harder as the baddies are harder to avoid the bigger they are. Similarly, by increasing the baddie min speed and max speed the game would get harder as the baddies are harder to avoid the faster they come down.
#By increasing the add new baddie rate, more baddies would come down which would be harder to avoid. By minimizing the player move rate would make the player move slower making it harder to avoid the baddies, however, increasing player speed (reasonably) would make it easier to avoid because you could move faster. By decreasing the size, speed, and number of baddies it would make the game easier.



def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
                #clear coins
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return

def playerHasHitBaddie(playerRect, baddies):
    for i in baddies:
        if playerRect.colliderect(i['rect']):
            return True
    return False
#in final B the colliderect was the statement that would have the actions if you hit the food played out. It would add points to your score and erase the food from the playing screen. In final C the collidirect is the if statement in the function that ends the game in the function by having the function return true. If the player does not collide with the baddie rectangle (not engaging the if statement) it returns false and the game continues. T
#the i in (i['rect']): is the index for how long the for loop will go. It effects the newBaddie line because the it resets with a new I indivdual bad guy of random size and speed. 


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, textColor)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Set up pygame, the window, and the mouse cursor.
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Flappy Bird Clone')
pygame.mouse.set_visible(False)

# Set up the fonts.
font = pygame.font.SysFont(None, 48)

# # Set up sounds.
gameOverSound = pygame.mixer.Sound('gameOverFlappy.wav')
pygame.mixer.music.load('backGroundFlappy.mp3')

# Set up images.
playerImage = pygame.image.load('flappy.png')
playerImage = pygame.transform.scale(playerImage, (40, 40))
player = playerImage.get_rect()

#the player is set equal to the player image that has been stretched by the tranformation in the line before so that the image will always be equivalent with the rectangle of the player because the player will not be growing in this game.

baddieImage = pygame.image.load('pipe.png')
baddieImage = pygame.transform.scale(baddieImage, (150, 150))


#the coin
food_size = 30
foodImage = pygame.image.load('coin.png')
foodStretchedImage = pygame.transform.scale(foodImage, (food_size, food_size))
#the difference is that foodimage is the image the food blocks are which you can change to an imported image, however, the  stretched variable is how the main eater block grows as its eats the other food.
foodCounter = 0
food_starting_num = 100

foods = []



# Show the "Start" screen.
windowSurface.fill(backgroundColor)
drawText('Avoid the Poles', font, windowSurface, (windowWidth / 3), (windowHeight / 3))
drawText('Press a key to start.', font, windowSurface, (windowWidth / 3) - 30, (windowHeight / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

topScore = 0

        
while True:
    # Set up the start of the game.
    baddies = []
    score = 0
    player.topleft = (windowWidth / 2, windowHeight - 50)
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False
    reverseCheat = False
    slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
    
    
    for i in range(1):
        foods.append(pygame.Rect(random.randint(0, windowWidth - food_size), random.randint(0, windowHeight - food_size), food_size, food_size))
     

    while True: # The game loop runs while the game part is playing.
        score += 1 # Increase score.
                
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        
#the cheat code when press Z makes the baddies go up and changes your score to zero
#the cheat code when you press x makes the baddies slow down so it is easier to avoid
            if event.type == KEYDOWN:
                if event.key == K_z:
                    reverseCheat = True
                if event.key == K_x:
                    slowCheat = True
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == K_z:
                    reverseCheat = False
                    score = 0
                if event.key == K_x:
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                        terminate()
                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False

            if event.type == MOUSEMOTION:
                player.centerx = event.pos[0]
                player.centery = event.pos[1]
# the Mousemotion if statement engages when the user interacts with the mouse and then uses the mouse to move the character to avoid the baddies!
                
        # Add new baddies at the top of the screen, if needed.
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
            
            
            
            
                # Move the player around.
        if moveLeft and player.left > 0:
            player.move_ip(-1 * playerMoveRate, 0)
        if moveRight and player.right < windowWidth:
            player.move_ip(playerMoveRate, 0)
        if moveUp and player.top > 0:
            player.move_ip(0, -1 * playerMoveRate)
        if moveDown and player.bottom < windowHeight:
            player.move_ip(0, playerMoveRate)
        player.move_ip(0, .5*playerMoveRate)

        # Move the baddies down.
        for i in baddies:
            if not reverseCheat and not slowCheat:
                i['rect'].move_ip(-6, 0)
            elif reverseCheat:
                i['rect'].move_ip(1, 0)
            elif slowCheat:
                i['rect'].move_ip(0, 0)
                
            #reversecheat makes the baddies slowly revease and stop cheat makes stops the poles/baddies in the place
            
      #  for i in foods:
       #     i['rect'].move_ip(-6,0)
        if baddieAddCounter == addNewBaddieRate:
            baddieAddCounter = 0
            baddieSize = 150
#             random.randint(baddieMinSize, baddieMaxSize)
            newBaddie = {'rect':pygame.Rect(550, random.randint(0, windowHeight - baddieSize),60, 180),
                        'speed': random.randint(baddieMinSpeed, baddieMaxSpeed),
                        'surface':pygame.transform.scale(baddieImage, (60, 180)),
                        }

            baddies.append(newBaddie)
        foodCounter = foodCounter + 1
       
        
        if foodCounter >= food_starting_num:
            foodCounter = 0
            foods.append(pygame.Rect(random.randint(0, windowWidth - 20), random.randint(0, windowHeight - 20), 20, 20))
        
        
                
        # Delete baddies that have fallen past the bottom.
        for i in baddies[:]:
            if i['rect'].top > windowHeight:
                baddies.remove(i)

        # Draw the game world on the window.
        windowSurface.fill(backgroundColor)

        # Draw the score and top score.
        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)
   
        #for i in range(len(foods)):
        #    pygame.draw.rect(windowSurface, RED, foods[i])
            

        for food in foods[:]:
            if player.colliderect(food):
                score = score + 500
                foods.remove(food)
        # Draw the player's rectangle.
        windowSurface.blit(playerImage, player)

        # Draw each baddie.
        for i in baddies:
            windowSurface.blit(i['surface'], i['rect'])
            
        # Draw the food
        for i in foods:
            windowSurface.blit(foodStretchedImage, i)
        
        pygame.display.update()

        # Check if any of the baddies have hit the player.
        if playerHasHitBaddie(player, baddies) == True:
            if score > topScore:
                topScore = score #sets a new top score if you topped the old one
            break #quits this loop, which is the inner of the two While loops way up top
                     # this sends you down to the "stop the game and show the 'Game Over' section of code. It then all runs again because of the outer while loop

        mainClock.tick(FPS)

    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText('GAME OVER', font, windowSurface, (windowWidth / 3), (windowHeight / 3))
    drawText('Press a key to play again.', font, windowSurface, (windowWidth / 3) - 80, (windowHeight / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()

    gameOverSound.stop()