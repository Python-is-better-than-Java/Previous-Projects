def playg100():
    import pygame
    import random
    import pygame.locals
    import os
    import pickle
    import tkinter as tk
    pygame.init()

    ################################################ Instructions ########################################################
    root = tk.Tk()
    T11 = tk.Text(root, height = 20, width = 110)
    T11.pack()
    T11.insert(tk.END,"HOW TO PLAY:\nChoose number of players (2-5) and difficulty level (1-3).\nThe player selects any number between 1 and 6 to move his/her character those many steps across a particular row of the board.\nIf the player steps on a 'bomb', which vary as per the difficulty level, are randomly spread across the board and are invisible, he/she moves back 1/2/3/4 steps depending on number of boxes behind the player.\nIts possible for the player to step on a bomb and go one step back, only to end up on another bomb and hence, go back another step. It can continue that way until the box the player is standing on has no bomb.\nIf the character is near the end of the row and the number of steps he/she has chosen exceeds the remaining number of boxes on that row, he/she is automatically taken to the first square of the next row, regardless of the number chosen.\n\nCONDITIONS TO WIN:\nThe first player to reach the last square of the last row wins.")
    T11.configure(font = ("helvetica",15,"bold"))
    root.mainloop()
    Wi = []

    ####################################### Difficulty, Number of Players ################################################
    if os.path.exists("Rank.dat"):
        os.remove("Rank.dat")
    else:
        pass
    
    def difficulty(diff = 0):
        while diff == 0:
            diff = int(input("Enter difficulty level (1-3): "))
            if 1 <= diff <= 3:
                return diff
            else:
                print("Difficulty level between 1 and 5 only.")
                diff = 0

    def playerno(np = 0):
        while np == 0:
            np = int(input("Enter number of players (min 2, max 5): "))
            if 2 <= np <= 5:
                return np
            else:
                print("Minimum is 2, maximum is 5. Numbers outside this range are not allowed.")
                np = 0

    def board():
        screen.fill((255,255,255))
        for box1 in range(0,600,120):
            for box2 in range(0,600,120):
                pygame.draw.rect(screen,(255,0,0),[10+box1,10+box2,60,60])
                pygame.draw.rect(screen,(0,255,0),[10+box1,70+box2,60,60])
                pygame.draw.rect(screen,(0,255,0),[70+box1,10+box2,60,60])
                pygame.draw.rect(screen,(255,0,0),[70+box1,70+box2,60,60])

    ######################################### Creating Screen and Players ###################################################

    screen = pygame.display.set_mode((800,650))
    capt = pygame.display.set_caption("Get To 100")
    done = True

    P = []
    char = []
    for i in range(0,playerno(0)):
        P.append(input("Enter name of player " + str(i+1) + ":"))
        char.append(pygame.Rect(15,15,50,50))

    O = []
    for out in range(0, 20+(10*difficulty(0))):
        x11 = 10+random.randrange(65,540,60)
        y11 = 10+random.randrange(5,600,60)
        O.append(pygame.Rect(x11,y11,50,50))
    print()

    ##################################### Game Code #################################################
    while done == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False

        ########################### Inputting Number of Steps #################################       
        for i in P:
            no = 0
            while no == 0:
                no = int(input(i+", enter box no. you want to move forward to (1-6): "))
                print()
                if (1 <= no <= 6):
                    if (((no*60)+char[P.index(i)].x) > 555):
                        if (char[P.index(i)].y == 555):
                            root = tk.Tk()
                            T1 = tk.Text(root, height = 3, width = 60)
                            T1.pack()
                            T1.insert(tk.END,i+", you need less than ",no," steps to finish. Unfortunately, as the number chosen is between 1 and 6, your turn is over.")
                            T1.configure(font = ("helvetica",20,"bold"))
                            root.mainloop()
                            print()
                        else:
                            char[P.index(i)].y += 60
                            char[P.index(i)].x = 15
                            print(i," is in box ",(((10*((char[P.index(i)].y-15)/60))+((char[P.index(i)].x-15)/60))+1))
                    else:
                        char[P.index(i)].x += (no*60)
                        print(i," is in box ",(((10*((char[P.index(i)].y-15)/60))+((char[P.index(i)].x-15)/60))+1))
                else:
                    root = tk.Tk()
                    T2 = tk.Text(root, height = 2, width = 65)
                    T2.pack()
                    T2.insert(tk.END,i+", the number of steps must be between 1 and 6 only. Try again.")
                    T2.configure(font = ("helvetica",20,"bold"))
                    root.mainloop()
                    print()
                    no = 0

        ##################################### Consequences of Stepping on a Bomb #########################################
        for out in O:
            for cha in char:
                if cha.colliderect(out):
                    if cha.x == 135:
                        cha.x -= 60
                        print("As ",P[char.index(cha)]," stepped on bomb(s), hence he/she is now in box number ",(((10*((cha.y-15)/60))+((cha.x-15)/60))+1))
                    elif cha.x == 195:
                        cha.x -= 120
                        print("As ",P[char.index(cha)]," stepped on bomb(s), hence he/she is now in box number ",(((10*((cha.y-15)/60))+((cha.x-15)/60))+1))
                    elif cha.x == 255:
                        cha.x -= 180
                        print("As ",P[char.index(cha)]," stepped on bomb(s), hence he/she is now in box number ",(((10*((cha.y-15)/60))+((cha.x-15)/60))+1))
                    else:
                        cha.x -= 240
                        print("As ",P[char.index(cha)]," stepped on bomb(s), hence he/she is now in box number ",(((10*((cha.y-15)/60))+((cha.x-15)/60))+1))
        
        ##################################### Declaring Winners ##########################################
        for cha in char:
            if (cha.y > 555) or (cha.x == 555 and cha.y == 555):
                Wi.append(P[char.index(cha)])
                rank = len(Wi)
                root = tk.Tk()
                T3 = tk.Text(root, height = 3, width = 50)
                T3.pack()
                T3.insert(tk.END,P[char.index(cha)]+" HAS FINISHED THE GAME AND TAKEN RANK NO. "+str(rank))
                T3.configure(font = ("helvetica",20,"bold"))
                root.mainloop()
                P.pop(char.index(cha))
                char.pop(char.index(cha))

        ################################## Graphics #######################################
        board()
        if len(char) == 0:
            done = False
        else:
            pass
            
        for cha in char:
            pygame.draw.ellipse(screen,(0,0,255),cha)
        pygame.display.flip()

    ########################################## Scoreboard ###############################################
    ranks= open('Rank.dat','wb')
    pickle.dump(Wi,ranks)
    ranks.close()
    ranks = open('Rank.dat','rb')
    firank = pickle.load(ranks)
    root = tk.Tk()
    T3 = tk.Text(root, height = 10, width = 40)
    T3.pack()
    T3.insert(tk.END,"Rank\t\tName")
    T3.configure(font = ("helvetica",20,"bold"))
    for ira in firank:
        T3.insert(tk.END,"\n"+str(firank.index(ira)+1)+"\t\t"+ira)
        T3.configure(font = ("helvetica",15,"bold"))
    root.mainloop()
##    pygame.quit()

##playg100()
