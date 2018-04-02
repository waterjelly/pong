import pygame
import random
 
class Player1():
        def __init__(self):
                self.x, self.y = 16, SCR_HEI/2
                self.speed = 6
                self.padWid, self.padHei = 8, 64
                self.score = 0
                self.scoreFont = pygame.font.SysFont('ActionIsShaded', 64)
       
        def scoring(self):
                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                screen.blit(scoreBlit, (32, 16))
                if self.score == 3:
                        print ("player 1 wins!")
                        ReStart()
       
        def movement(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                        self.moveUp()
                elif keys[pygame.K_s]:
                        self.moveDown()
       
                if self.y <= 0:
                        self.y = 0
                elif self.y >= SCR_HEI-64:
                        self.y = SCR_HEI-64
        def moveUp(self):
                self.y -= self.speed

        def moveDown(self):
                self.y += self.speed
                
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))
 
class Player2():
        def __init__(self):
                self.x, self.y = SCR_WID-16, SCR_HEI/2
                self.speed = 6
                self.padWid, self.padHei = 8, 64
                self.score = 0
                self.scoreFont = pygame.font.SysFont('ActionIsShaded', 64)
       
       
        def scoring(self):
                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                screen.blit(scoreBlit, (SCR_HEI+92, 16))
                if self.score == 3:
                        print ("Player 2 wins!")
                        ReStart()
       
        def movement(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                        self.moveUp()
                elif keys[pygame.K_DOWN]:
                        self.moveDown()
       
                if self.y <= 0:
                        self.y = 0
                elif self.y >= SCR_HEI-64:
                        self.y = SCR_HEI-64
        def moveUp(self):
                self.y -= self.speed

        def moveDown(self):
                self.y += self.speed
                
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))

randarr = [0,1] 
class Ball():
        gameplayed = 1
        def __init__(self):
                if(random.choice(randarr)==0):
                        self.speed_x = 5
                
                else:
                        self.speed_x = -5

                
                if(random.choice(randarr)==0):
                        self.speed_y = 5
                
                else:
                        self.speed_y = -5
                self.x, self.y = SCR_WID/2, SCR_HEI/2
                self.size = 8
       
        def movement(self):
                self.x += self.speed_x
                self.y += self.speed_y
 
                #wall col
                if self.y <= 0:
                        self.speed_y *= -1
                elif self.y >= SCR_HEI-self.size:
                        self.speed_y *= -1
 
                if self.x <= 0:
                        self.__init__()
                        player2.score += 1
                elif self.x >= SCR_WID-self.size:
                        self.__init__()
                        player1.score += 1
                ##wall col
                #paddle col
                #player
                for n in range(-self.size, player1.padHei):
                        if self.y == player1.y + n:
                                if self.x <= player1.x + player1.padWid:
                                        self.speed_x *= -1
                                        break
                        n += 1
                #player2
                for n in range(-self.size, player2.padHei):
                        if self.y == player2.y + n:
                                if self.x >= player2.x - player2.padWid:
                                        self.speed_x *= -1
                                        break
                        n += 1
                ##paddle col
 
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 8, 8))
        
 
SCR_WID, SCR_HEI = 640, 480
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
pygame.display.set_caption("Pong")
pygame.font.init()
clock = pygame.time.Clock()
FPS = 60
ball = Ball()
player1 = Player1()
player2 = Player2()

        
def GameOver():
        exit()
        
def ReStart():
        print ("restart")
        ball.__init__()
        player1.__init__()
        player2.__init__()
        ball.gameplayed += 1

 
while True:
        #process
        for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                print ("Game exited by user")
                                exit()
        ##process
        #logic
        ball.movement()
        player1.movement()
        player2.movement()
        ##logic
        #draw
        screen.fill((0, 0, 0))
        ball.draw()
        player1.draw()
        player1.scoring()
        player2.draw()
        player2.scoring()
        #Print Position
        print ('{},{},{},{},{},{},{},{},{}'.format(int(player1.x),int(player1.y),int(player2.x),int(player2.y),int(ball.x),int(ball.y),player1.score,player2.score,ball.gameplayed))
        ##draw
        #_______
        pygame.display.flip()
        clock.tick(FPS)
