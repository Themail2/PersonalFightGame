import pygame




win = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Fight Game")

class character1():
     def __init__(self):
          pass
          # each char will be uniquely built but I want them to be objects, so they don't
          # need parameters 
     
     def attacks(self, button):
          pass
          #to-do
          #have attack hitbox show up for each unique button push
          #consult game devs bc idk what im doin

          
#main menus and stuff here idk
def main():
    # If this ever becomes false, game execution ends.
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

main()