import pygame

pygame.init()

largura = (300,200)

janela = pygame.display.set_mode(largura)

while True:
   for evento in pygame.event.get():
     if evento.type == pygame.QUIT:
       pygame.quit()
       exit(0)

   janela.fill((0,0,1))
   
   pygame.draw.rect((janela),(255,255,255),(100,50,25,50))
   pygame.draw.rect((janela),(255,255,255),(200,50,25,50))
   pygame.draw.rect((janela),(255,255,255),(100,125,125,25))
   
   pygame.display.flip()