import pygame
import pong3 as game
import cv2

class Agent:
    
    i = 0

    def __init__(self):
        self.ball = game.Ball()
        self.player = game.Player()
        self.player2 = game.Player2()
        self.player2 = game.Player2()
        
    def saveImage(self,image_data):
        
        image_resized = pygame.surfarray.array3d(image_data)
        image_resized = cv2.resize(image_resized,None, fx=0.1,fy = 0.1)
        #x_t1_greyscale = cv2.cvtColor(x_t1_resized, cv2.COLOR_BGR2GRAY)
        #ret, x_t1 = cv2.threshold(x_t1_greyscale, 1, 255, cv2.THRESH_BINARY)
        
        #pygame.image.save(image_resized,str(self.i)+'.jpg')
        #pygame.image.save(image_data,str(self.i)+'.jpg')
        cv2.imwrite(str(self.i)+'.jpg',image_resized)
        self.i=self.i+1
    
    def mainLoop(self):
        while True:
            for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    print ("Game exited by user")
                                    exit()
            ##process
            #logic
            game.screen.fill((0, 0, 0))
            game.ball.movement()
            game.player.movement()
            game.player2.movement()
            game.player3.movement()
            ##logic
            #draw
            game.ball.draw()
            game.player.draw()
            game.player2.draw()
            game.player3.draw()
            self.saveImage(self.ball.getSurface())
            
            game.player.scoring()
            game.player2.scoring()
            game.player3.scoring()
            ##draw
            #_______
            pygame.display.flip()
            print(self.i)
            game.clock.tick(game.FPS)
        
  
def main(argv):
    agent = Agent()
    agent.mainLoop()
    
if __name__ == "__main__":
    from sys import argv
    main(argv)
