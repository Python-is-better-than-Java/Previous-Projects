run = True

while run == True:
    import pygame
    import pygame.locals
    pygame.init()
    launch = pygame.display.set_mode((1260,680))
    lacapt = pygame.display.set_caption("Brainlink V1.0")
    alrun = True

    font = pygame.font.Font('freesansbold.ttf',30)
    fonts = pygame.font.Font("freesansbold.ttf",30)

    text = fonts.render("CLICK ON WHAT TO PLAY",run,(8,97,11),(255,157,22))
    text1 = font.render("Collect the Treasures",run,(255,200,0),(172,116,135))
    text2 = font.render("Escape 25 Floors",run,(255,200,0),(125,116,135))
    text3 = font.render("Pop the Squares",run,(255,200,0),(105,108,135))
    text4 = font.render("Connect 4",run,(255,200,0),(105,132,198))
    text5 = font.render("Get To 100",run,(255,200,0),(211,83,213))

    textR = text.get_rect()
    textR.center = (630,170)
    textR1 = text.get_rect()
    textR1.center = (240,170)
    textR2 = text.get_rect()
    textR2.center = (1120,170)
    textR3 = text.get_rect()
    textR3.center = (280,520)
    textR4 = text.get_rect()
    textR4.center = (740,520)
    textR5 = text.get_rect()
    textR5.center = (1160,520)

    launch.fill((255,255,255))

    while alrun == True:
        pygame.draw.rect(launch,(172,116,135),[0,0,420,340])
        pygame.draw.rect(launch,(125,116,135),[840,0,420,340])
        pygame.draw.rect(launch,(105,108,135),[0,340,420,340])
        pygame.draw.rect(launch,(105,132,198),[420,340,420,340])
        pygame.draw.rect(launch,(211,83,213),[840,340,420,340])

        pygame.draw.rect(launch,(255,157,22),[420,0,420,340])
        launch.blit(text,textR)

        launch.blit(text1,textR1)
        launch.blit(text2,textR2)
        launch.blit(text3,textR3)
        launch.blit(text4,textR4)
        launch.blit(text5,textR5)

        pygame.display.update()
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                alrun = run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x,y = pygame.mouse.get_pos()
                    if (0 < x < 420) and (0 < y < 340):
                        import Collect_the_Treasures as ct
                        ct.playct()
                        alrun = False
                    elif (840 < x < 1260) and (0 < y < 340):
                        import Escape_25_Floors as es25
                        es25.playes25()
                        alrun = False
                    elif (0 < x < 420) and (340 < y < 680):
                        import Pop_the_Squares as ps
                        ps.playps()
                        alrun = False
                    elif (420 < x < 840) and (340 < y < 680):
                        import Connect_4 as c4
                        c4.playc4()
                        alrun = False
                    elif (840 < x < 1260) and (340 < y < 680):
                        import Get_To_100 as g100
                        g100.playg100()
                        alrun = False
                    else:
                        pass
pygame.quit()
exit()
