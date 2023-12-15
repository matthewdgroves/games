import pygame, random, sys
from pygame.locals import *

windowWidth = 600
windowHeight = 600
textColor = (0, 0, 0)
backgroundColor = (255, 255, 255)
FPS = 60
baddieMinSize = 15
baddieMaxSize = 40
generalSpeed = -3
addNewBaddieRate = 30
giftMinSize = 10
giftMaxSize = 20
addNewGiftRate = 12
playerMoveRate = 6

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return

def playerHasHitBaddie(playerRect, baddies):
    for i in baddies:
        if playerRect.colliderect(i['rect']):
            return True
    return False

def playerHasHitGift(playerRect, gifts):
    for i in gifts:
        if playerRect.colliderect(i['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textColor = (255, 0, 0)
    textobj = font.render(text, 1, textColor)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Set up pygame, the window, and the mouse cursor.
pygame.init()
#pygame.mixer.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Ski')
pygame.mouse.set_visible(True)

# Set up the fonts.
font = pygame.font.SysFont(None, 48)

# Set up sounds.
#gameOverSound = pygame.mixer.Sound('game_over.wav')
#pygame.mixer.music.load('background_music.mp3')
#getGiftSound = pygame.mixer.Sound('get_gift.wav')

# Set up images.
playerImage = pygame.image.load('berdski.png')
playerImage = pygame.transform.scale(playerImage, (40, 40))
player = playerImage.get_rect()

baddieImage = pygame.image.load('trees.png')
baddieImage = pygame.transform.scale(baddieImage, (10, 10))

giftImage = pygame.image.load('gift.png')
giftImage = pygame.transform.scale(giftImage, (10, 10))

# Show the "Start" screen.
windowSurface.fill(backgroundColor)
drawText('SKI', font, windowSurface, 215, (windowHeight / 3))
drawText('Collect presents for the Skier!', font, windowSurface, 100, 250)
drawText('Avoid the trees with the arrow keys.', font, windowSurface, 25, 300)
drawText('Press any key to start.', font, windowSurface, 125, 350)
pygame.display.update()
waitForPlayerToPressKey()


topScore = 0
while True:
    # Set up the start of the game.
    baddies = []
    print(baddies)
    gifts = []
    score = 0
    player.topleft = (windowWidth / 2, 50)
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False
    morePointCheat = False
    allGiftCheat = False
    baddieAddCounter = 0
    giftAddCounter = 0
    #pygame.mixer.music.play(-1, 0.0)

    while True: # The game loop runs while the game part is playing                

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

        #Key controls.
            if event.type == KEYDOWN:
                if event.key == K_p:
                    morePointCheat = True
                if event.key == K_g:
                    allGiftCheat = True
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
                if event.key == K_p:
                    morePointCheat = False
                if event.key == K_g:
                    allGiftCheat = False
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


        baddieAddCounter += 1
        if baddieAddCounter == addNewBaddieRate:
            baddieAddCounter = 0
            baddieSize = random.randint(baddieMinSize, baddieMaxSize)
            newBaddie = {'rect': pygame.Rect(random.randint(0, windowWidth - baddieSize), 600 - baddieSize, baddieSize, baddieSize),
                        'speed': generalSpeed,
                        'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
                        }
            baddies.append(newBaddie)


        giftAddCounter += 1
        if giftAddCounter == addNewGiftRate:
            giftAddCounter = 0
            giftSize = random.randint(giftMinSize, giftMaxSize)
            newGift = {'rect': pygame.Rect(random.randint(0, windowWidth - giftSize), 600 - giftSize, giftSize, giftSize),
                        'speed': generalSpeed,
                        'surface':pygame.transform.scale(giftImage, (giftSize, giftSize)),
                        }
            gifts.append(newGift)

        # Move the player around.
        if moveLeft and player.left > 0:
            player.move_ip(-1 * playerMoveRate, 0)
        if moveRight and player.right < windowWidth:
            player.move_ip(playerMoveRate, 0)
        if moveUp and player.top > 0:
            player.move_ip(0, -1 * playerMoveRate)
        if moveDown and player.bottom < windowHeight:
            player.move_ip(0, playerMoveRate)

        #Moves trees and gifts up. 
        for i in baddies:
                i['rect'].move_ip(0, i['speed']) 
        for i in gifts:
                i['rect'].move_ip(0, i['speed'])

        # Delete baddies that have gone past the top.
        for i in baddies[:]:
             if i['rect'].top < 0:
                 baddies.remove(i)

        #Delete gifts that have gone past the top.
        for i in gifts[:]:
            if i['rect'].top < 0:
                gifts.remove(i)

        # Draw the game world on the window.
        windowSurface.fill(backgroundColor)
        windowSurface.blit(playerImage, player)

        # Draw each baddie.
        for i in baddies:
            windowSurface.blit(i['surface'], i['rect'])

        # Draw each gift.              
        for i in gifts:
            windowSurface.blit(i['surface'], i['rect'])

        # Draw the score and top score.
        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)
        pygame.display.update()

    # Check if any of the baddies/gifts have hit the player, apply cheat protocols Y or N.
        if allGiftCheat == False:
            baddieImage = pygame.image.load('trees.png')
            baddieImage = pygame.transform.scale(baddieImage, (10, 10))
            if playerHasHitBaddie(player, baddies) == True:
                if score > topScore:
                    topScore = score
                break
        if allGiftCheat == True:
            for i in baddies[:]:
                baddieImage = giftImage
                baddieImage = pygame.transform.scale(giftImage, (10, 10))
                if player.colliderect(i['rect']):
                    score = score + 1
                    baddies.remove(i)

        if morePointCheat == True:
            for i in gifts[:]:
                if player.colliderect(i['rect']):
                    #getGiftSound.play()
                    score = score + random.randint(5, 15)
                    gifts.remove(i)
        if morePointCheat == False:
            for i in gifts[:]:
                if player.colliderect(i['rect']):
                    #getGiftSound.play()
                    score = score + 1
                    gifts.remove(i)

        mainClock.tick(FPS)

    # Stop the game and show the "Game Over" screen.
    #pygame.mixer.music.stop()
    #gameOverSound.play()

    drawText('GAME OVER', font, windowSurface, 185, 250)
    drawText('Press a key to play again.', font, windowSurface, 100, 300)
    pygame.display.update()
    waitForPlayerToPressKey()
    #gameOverSound.stop()
