def playct():
    import random
    import pygame
    import pygame.locals
    import tkinter as tk
    pygame.init()
    clock = pygame.time.Clock()

    ########################################### Instructions ################################################################
    root = tk.Tk()
    T11 = tk.Text(root, height = 20, width = 110)
    T11.pack()
    T11.insert(tk.END,"ABOUT THE GAME:\nIn this game, the yellow circle is the player.\nThe 3 blue circles are the 'Treasures', while the red circles are 'mines' (number of mines vary with difficulty level).\nThe mines in the game will randomly become visible and then invisible at particular intervals of time (you can see 100 mines at any point in time).\nIf the mine becomes invisible, it is not to be assumed that there are no more mines on that box.\n\nFollowing will result in 'GAME OVER':\nStepping on a mine before collecting all 3 treasures.\n\nCONDITIONS TO WIN:\nCollect all 3 treasures without stepping on any mine.\n\nCONTROLS:\n1. UP Arrowkey or 'w' to move up.\n2. DOWN Arrowkey or 's' to move down.\n3. RIGHT Arrowkey or 'd' to move right.\n4. LEFT Arrowkey or 'a' to move left.")
    T11.configure(font = ("helvetica",15,"bold"))
    root.mainloop()

    ################################# Setting Difficulty #############################################
    def difficulty(diff = 0):
        while diff == 0:
            diff = int(input("Enter difficulty level (1-5): "))
            if 1 <= diff <= 5:
                return diff
            else:
                print("Difficulty level must be between 1 and 5 only.")
                diff = 0

    ############################## Creating Screen, Player, Mines and Treasures ################################
    screen = pygame.display.set_mode((1360,690))
    capt = pygame.display.set_caption("Collect the Treasures")

    char = pygame.Rect(10,2,17,17)
    tres = []
    for ac in range(3):
        x11 = 10+random.randrange(17,673,17)
        y11 = 2+random.randrange(17,665,17)
        tres.append(pygame.Rect(x11,y11,17,17))
    mines = []
    for ab in range(0,60*difficulty(0)):
        x12 = 10+random.randrange(17,673,17)
        y12 = 2+random.randrange(17,665,17)
        ww = 0
        for tre in tres:
            if (x12 == tre.x) and (y12 == tre.y):
                ww += 1
            if ww == 0:
                mines.append(pygame.Rect(x12,y12,17,17))
            else:
                pass

    move = 17
    pygame.display.flip()
    done = True

    #################################################### Game Code #######################################################
    while done == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False

        ################################ Controls ##################################
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and char.x <= 666:
            char.x += move
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and char.y <= 650:
            char.y += move
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and char.y >= 19:
            char.y -= move
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and char.x >= 27:
            char.x -= move

        ################################# Win/Lose Conditions ###################################
        for mine in mines:
            if char.x == mine.x and char.y == mine.y:
                root = tk.Tk()
                T1 = tk.Text(root, height = 1, width = 49)
                T1.pack()
                T1.insert(tk.END,"YOU STEPPED ON A MINE. BETTER LUCK NEXT TIME.")
                T1.configure(font = ("helvetica",20,"bold"))
                root.mainloop()
                mines.remove(mine)
                done = False
                
        for tre in tres:
            if char.x == tre.x and char.y == tre.y:
                root = tk.Tk()
                T2 = tk.Text(root, height = 1, width = 25)
                T2.pack()
                T2.insert(tk.END,"YOU FOUND A TREASURE!")
                T2.configure(font = ("helvetica",20,"bold"))
                root.mainloop()
                tres.remove(tre)
##                if tres == []:
                if len(tres) == 0:
                    root = tk.Tk()
                    T3 = tk.Text(root, height = 1, width = 40)
                    T3.pack()
                    T3.insert(tk.END,"CONGRATULATIONS! YOU WON THE GAME!")
                    T3.configure(font = ("helvetica",20,"bold"))
                    root.mainloop()
                    done = False

        ############################## Graphics #########################################
        screen.fill((255,255,255))

        for i in range(0,680,34):
            for j in range(0,680,34):
                pygame.draw.rect(screen, (0,0,0), [10+i,2+j,17,17], 0)
                pygame.draw.rect(screen, (150,150,150), [10+i,19+j,17,17], 0)
                pygame.draw.rect(screen, (150,150,150), [27+i,2+j,17,17], 0)
                pygame.draw.rect(screen, (0,0,0), [27+i,19+j,17,17], 0)

        ivi = random.randint(2,8)
        for mine in range(0,len(mines),ivi):
            pygame.draw.ellipse(screen, (255,0,0), mines[mine])
        for tre in tres:
            if tre.x == mines[mine].x and tre.y == mines[mine].y:
                pass
            else:
                pygame.draw.ellipse(screen, (0,255,0),tre)

        pygame.draw.ellipse(screen, (255,255,0), char)
        
        pygame.display.flip()
        clock.tick(2)
                
##    pygame.quit()

##playct()
