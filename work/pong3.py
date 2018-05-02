import pygame
from os import path

class Player(pygame.sprite.Sprite):
        def __init__(self):
                self.x, self.y = 88, 350
                self.speed_x = 0
                self.speed_y = 12
                self.padWid, self.padHei = 8, 64
                self.score = 0
                self.scoreFont = pygame.font.Font(None, 64)

                self.size = (self.padWid,self.padHei)
                self.position = (self.x, self.y)
                
                pygame.sprite.Sprite.__init__(self)

                self.load_file()
                
        def load_file(self):
                game_folder = path.dirname(__file__)
                img_folder = path.join(game_folder, 'img')
                self.image = pygame.image.load(path.join(img_folder, 'player.png')).convert_alpha()
                self.rect = self.image.get_rect()
       
        def scoring(self):
                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                screen.blit(scoreBlit, (30, 300))
                if self.score == 10:
                        print ("player 1 wins!")
                        exit()
        def reset(self):
                self.x, self.y = 88, 350
                self.position = (self.x, self.y)
                
       
        def movement(self):
                keys = pygame.key.get_pressed()
                #if keys[pygame.K_w]:
                #        self.y -= self.speed_y
                #elif keys[pygame.K_s]:
                #        self.y += self.speed_y

                if self.y < ball.y:
                        self.y += self.speed_y
                elif ball.y < self.y:
                        self.y -=self.speed_y
                if self.y <= 92:
                        self.y = 92
                elif self.y >= 624:
                        self.y = 624
                self.position = (self.x,self.y)
       
        def draw(self):
                self.rect.center = self.position
                screen.blit(self.image, (self.x,self.y-32))
 
class Player2(pygame.sprite.Sprite):
        def __init__(self):
                self.x, self.y = 344, 200 
                self.speed_x = 10.5
                self.speed_y = 6
                self.padWid, self.padHei = 8, 64
                self.score = 0
                self.scoreFont = pygame.font.Font(None, 64)

                self.size = (self.padWid,self.padHei)
                self.position = (self.x, self.y)
                
                pygame.sprite.Sprite.__init__(self)

                self.load_file()
                
        def load_file(self):
                game_folder = path.dirname(__file__)
                img_folder = path.join(game_folder, 'img')
                self.image = pygame.image.load(path.join(img_folder, 'player.png')).convert_alpha()
                self.image = pygame.transform.rotate(self.image, 60)
                self.rect = self.image.get_rect()

                
        def scoring(self):
                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                screen.blit(scoreBlit, (400, 40))
                if self.score == 10:
                        print ("Player 2 wins!")
                        exit()
        def reset(self):
                self.x, self.y = 344, 200 
                self.position = (self.x, self.y)
       
        def movement(self):
#                keys = pygame.key.get_pressed()
#                if keys[pygame.K_UP]:
#                        self.y -= self.speed
#                elif keys[pygame.K_DOWN]:
#                        self.y += self.speed
                if ball.x < self.x:
                        self.x -= self.speed_x
                        self.y -= self.speed_y
                elif self.x < ball.x:
                        self.x += self.speed_x
                        self.y += self.speed_y
       
                if self.x <= 124:
                        self.x = 124
                        self.y = 74
                elif self.x >= 579: #82+525-56 = 551
                        self.x = 579
                        self.y = 334
                self.position = (self.x,self.y)
       
        def draw(self):
                self.rect.center = self.position
                screen.blit(self.image, (self.x-28,self.y-12))


class Player3(pygame.sprite.Sprite):
        def __init__(self):
                self.x, self.y = 344, 500
                self.speed_x = 10.5
                self.speed_y = 6
                self.padWid, self.padHei = 8, 64
                self.score = 0
                self.scoreFont = pygame.font.Font(None, 64)

                self.size = (self.padWid,self.padHei)
                self.position = (self.x, self.y)
                
                pygame.sprite.Sprite.__init__(self)

                self.load_file()
                
        def load_file(self):
                game_folder = path.dirname(__file__)
                img_folder = path.join(game_folder, 'img')
                self.image = pygame.image.load(path.join(img_folder, 'player.png')).convert_alpha()
                self.image = pygame.transform.rotate(self.image, 120)
                self.rect = self.image.get_rect()
       
        def scoring(self):
                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                screen.blit(scoreBlit, (400, 600))
                if self.score == 10:
                        print ("player 3 wins!")
                        exit()
       
        def reset(self):
                self.x, self.y = 344, 500
                self.position = (self.x, self.y)
                
        def movement(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                        self.x -= self.speed_x
                        self.y += self.speed_y
                elif keys[pygame.K_RIGHT]:
                        self.x += self.speed_x
                        self.y -= self.speed_y
                #if ball.x < self.x:
                #        self.x -= self.speed_x
                #        self.y += self.speed_y
                #elif self.x < ball.x:
                #        self.x += self.speed_x
                #        self.y -= self.speed_y
       
                if self.x <= 124:
                        self.x = 124
                        self.y = 626
                elif self.x >= 579:
                        self.x = 579
                        self.y = 366
                self.position = (self.x,self.y)
       
        def draw(self):
                self.rect.center = self.position
                screen.blit(self.image, (self.x-28,self.y-20))
                
 
class Ball(pygame.sprite.Sprite):
        def __init__(self):
                self.x, self.y = SCR_WID/2, SCR_HEI/2
                self.speed_x = 7
                self.speed_y = 4
                self.size = 8
        
                self.scoreFont = pygame.font.Font(None, 64)
                self.flag = 0

                self.load_file()
                
        def load_file(self):
                game_folder = path.dirname(__file__)
                img_folder = path.join(game_folder, 'img')
                self.image = pygame.image.load(path.join(img_folder, 'ball.png')).convert_alpha()
                self.rect = self.image.get_rect()

        def movement(self):
                self.x += self.speed_x
                self.y += self.speed_y
 
                #wall col
                if self.y <= 0:
                        self.speed_y *= -1
                elif self.y >= SCR_HEI-self.size:
                        self.speed_y *= -1
 
                if self.x <= 35:
                        self.__init__()
                        player2.score += 1
                        player3.score += 1
                        self.flag = 0
                        self.speed_x = 7
                        self.speed_y = 1
                        player.reset()
                        player2.reset()
                        player3.reset()
                elif (self.x * 4 / 7) + self.size - 46  >= self.y:
                        self.__init__()
                        player.score += 1
                        player3.score += 1
                        self.flag = 0
                        self.speed_x = -6
                        self.speed_y = -8
                        player.reset()
                        player2.reset()
                        player3.reset()
                elif (self.x * 4 / 7) * (-1) + self.size + 746  <= self.y:
                        self.__init__()
                        player.score += 1
                        player2.score += 1
                        self.flag = 0
                        self.speed_x = 6
                        self.speed_y = 7
                        player.reset()
                        player2.reset()
                        player3.reset()
                ##wall col
                #paddle col
                #player
                
                if (self.flag != 1):       
                        for n in range(0, int(player.padHei/2)):
                                if player.y - n <= self.y <= player.y + n:
                                        if player.x - player.padWid <= self.x * 1.0 <= player.x + player.padWid:
                                                self.speed_x *= -1
                                                self.flag=1
                                                break
                                n += 1
                #player2
                if (self.flag != 2):
                        for n in range(0, int(player2.padHei/2)):
                                if player2.y - (n/2) <= self.y <= player2.y + (n/2):
                                        if player2.x - (n*7/8) <= self.x <= player2.x + (n*7/8):
                                                #self.speed_y *= -1
                                                self.dummy = self.speed_x
                                                self.speed_x = (1 / 2 * self.speed_x + 7 / 8 * self.speed_y)
                                                self.speed_y = (7 / 8 * self.dummy - self.speed_y / 2)
                                                self.flag=2
                                                break
                                n += 1  
                #player3
                if (self.flag != 3):
                        for n in range(-self.size, int(player3.padHei/2)):
                                if player3.y - (n/2) <= self.y <= player3.y + (n/2):
                                        if player3.x - (n*7/8)<= self.x <= player3.x + (n*7/8):
                                                #self.speed_y *= -1
                                                self.dummy = self.speed_x
                                                self.speed_x = (1 / 2 * self.speed_x - 7 / 8 * self.speed_y)
                                                self.speed_y = (-7 / 8 * self.dummy - self.speed_y / 2)
                                                self.flag=3
                                                break
                                n += 1                        
                self.debuging()
                ##paddle col
                self.position = (self.x, self.y)
 
        def debuging(self):
                scoreBlit = self.scoreFont.render(str(self.flag), 1, (255, 255, 255))
                screen.blit(scoreBlit, (350, 350))
                
        def draw(self):
                self.rect.center = self.position
                screen.blit(self.image, self.position)
                
        def getSurface(self):
            image_data = pygame.surfarray.array3d(pygame.display.get_surface())
            
            return image_data
        
        def getScoreSurface(self):
            image_data = pygame.surfarray.array3d(pygame.display.get_surface())
            
            return image_data

 
SCR_WID, SCR_HEI = 764, 764
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
pygame.display.set_caption("Pong")
pygame.font.init()
clock = pygame.time.Clock()
FPS = 60

ball = Ball()
player = Player()
player2 = Player2()
player3 = Player3()


def main(argv):
    while True:
            #process
            for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    print ("Game exited by user")
                                    exit()
            pygame.display.flip()
            #capture
        
            ##process
            #logic
            ball.movement()
            player.movement()
            player2.movement()
            player3.movement()
            ##logic
            #draw
            screen.fill((0,0,0))
            ball.draw()
            player.draw()
            player.scoring()
            player2.draw()
            player2.scoring()
            player3.draw()
            player3.scoring()
            ##draw
            #_______
            clock.tick(FPS)

if __name__ == "__main__":
    from sys import argv
    main(argv)
