import pygame
from os import path

class Player():
        def __init__(self):
                self.x, self.y = 88, SCR_HEI/2
                self.speed = 3
                self.padWid, self.padHei = 8, 64
                self.score = 0
                self.scoreFont = pygame.font.Font(None, 64)
       
        def scoring(self):
                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                screen.blit(scoreBlit, (88, 50))
                if self.score == 10:
                        print ("player 1 wins!")
                        exit()
       
        def movement(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                        self.y -= self.speed
                elif keys[pygame.K_s]:
                        self.y += self.speed
       
                if self.y <= 0:
                        self.y = 0
                elif self.y >= SCR_HEI-64:
                        self.y = SCR_HEI-64
                        

        def reset(self):
                self.x, self.y = 88, SCR_HEI/2
                self.position = (self.x, self.y)
                
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))
 
class Player2():
        def __init__(self):
                self.x, self.y = SCR_WID-88, SCR_HEI/2
                self.speed = 12
                self.padWid, self.padHei = 8, 64
                self.score = 0
                self.scoreFont = pygame.font.Font(None, 64)
       
        def scoring(self):
                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                screen.blit(scoreBlit, (SCR_WID-88, 50))
                if self.score == 10:
                        print ("Player 2 wins!")
                        exit()
       
        def movement(self):
                keys = pygame.key.get_pressed()
#                if keys[pygame.K_UP]:
#                        self.y -= self.speed
#                elif keys[pygame.K_DOWN]:
#                        self.y += self.speed

                if self.y < ball.y:
                        self.y += self.speed
                elif ball.y < self.y:
                        self.y -=self.speed
                        
                if self.y <= 0:
                        self.y = 0
                elif self.y >= SCR_HEI-64:
                        self.y = SCR_HEI-64

                        
        def reset(self):
                self.x, self.y = SCR_WID-88, SCR_HEI/2
                self.position = (self.x, self.y)
                
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))
 
class Ball(Player,Player2):
        def __init__(self):
                self.x, self.y = SCR_WID/2, SCR_HEI/2
                self.speed_x = -3
                self.speed_y = 3
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
 
                if self.x <= 0:
                        self.__init__()
                        player2.score += 1
                        self.flag = 0
                        self.speed_x = -3
                        player.reset()
                        player2.reset()
                elif self.x >= SCR_WID-self.size:
                        self.__init__()
                        player.score += 1
                        self.flag = 0
                        self.speed_x = 3
                        player.reset()
                        player2.reset()
                ##wall col
                #paddle col
                #player
                print(self.x,self.y)
                if (self.flag != 1):
                        for n in range(-self.size, player.padHei):
                                if 87 < self.x < 89:
                                        if self.y == player.y + n:
                                                if self.x <= player.x + player.padWid:
                                                        self.speed_x *= -1
                                                        self.flag = 1
                                                        break
                                n += 1
                #player2
                if (self.flag != 2):
                        for n in range(-self.size, player2.padHei):
                                if SCR_WID - 89 < self.x < SCR_WID - 87:
                                        if self.y == player2.y + n:
                                                if self.x >= player2.x - player2.padWid:
                                                        self.speed_x *= -1
                                                        self.flag = 2
                                                        break
                                n += 1
                ##paddle col
 
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 8, 8))
                
        def getSurface(self):
            image_data2 = pygame.display.get_surface()
            
            return image_data2
 
SCR_WID, SCR_HEI = 764, 764
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
pygame.display.set_caption("Pong")
pygame.font.init()
clock = pygame.time.Clock()
FPS = 60


ball = Ball()
player = Player()
player2 = Player2()


def main(argv):
    
    while True:
            #process
            for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    print ("Game exited by user")
                                    exit()
            ##process
            #logic
            ball.movement()
            player.movement()
            player2.movement()
            ##logic
            #draw
            screen.fill((0, 0, 0))
            ball.draw()
            player.draw()
            player.scoring()
            player2.draw()
            player2.scoring()
            ##draw
            #_______
            pygame.display.flip()
            #clock.tick(FPS)

if __name__ == "__main__":
    from sys import argv
    main(argv)
