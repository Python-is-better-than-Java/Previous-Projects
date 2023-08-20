def playes25():
    import pygame
    import pygame.locals
    import tkinter as tk
    import os
    import random
    import pickle
    pygame.init()

    #################################################### Instructions #################################################################
    root = tk.Tk()
    T11 = tk.Text(root, height = 20, width = 110)
    T11.pack()
    T11.insert(tk.END,"HOW TO PLAY:\nFirst input number of players (not more than 10) and the names of those players.\nThe required number of blue squares will be formed.\nThere are 10 doors, out of which 5 doors will let you through the next floor and the other 5 will lead to your death.\nThe player has to go through the end of that door (which is between the black walls).\n\nCONDITIONS TO WIN:\nPass all 25 floors unharmed (starting from floor no. 25 to floor no. 1).\n\nFollowing will result in a playrer's death:\nPassing through an incorrect door in any of the floors.\n\nCONTROLS:\n1. UP Arrowkey or 'w' to move up.\n2. DOWN Arrowkey or 's' to move down.\n3. RIGHT Arrowkey or 'd' to move right.\n4. LEFT Arrowkey or 'a' to move left.")
    T11.configure(font = ("helvetica",15,"bold"))
    root.mainloop()

    ############################################### Number of Players and Their Names ###################################################
    if os.path.exists("EscapeScores.dat"):
        os.remove("EscapeScores.dat")
    else:
        pass
    
    names = []
    ef = []
    do = []
    no = 0
    while no == 0:
        nop = int(input("Enter number of players (maximum 10 players): "))
        if nop <= 10:
            no = nop
        else:
            print("Not more than 10 please")
            print()
            no = 0
    for i in range(0,no):
        na = input("Enter name of player "+str(i+1)+": ")
        names.append(na)
        ef.append([na,0])
    print()

    ######################################## Deciding Floor Number and Displaying It, Game Code ########################################
    fl = 25   
    while fl > 0:
        root = tk.Tk()
        T1 = tk.Text(root, height = 1, width = 20)
        T1.pack()
        T1.insert(tk.END,"Floor number "+str(fl))
        T1.configure(font = ("helvetica",20,"bold"))
        root.mainloop()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((1140,690))
        pygame.display.set_caption("Escape 25 Floors")
        done = True

        ##################################### Create Walls and Players ##################################################
        walls = []
        for i1 in range(0,1210,110):
            walls.append(pygame.Rect(0+i1,335,40,170))
        ch = []
        for k1 in range(len(names)):
            ch.append(pygame.Rect(45+(k1*70),100,38,38))
        pl = ch
        n = 0
        l = []
        for m in range(len(names)):
            l.append(0)

        ################################################ Game Code ##################################################
        while done == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fl = 1
                    done = False
                    
            keys = pygame.key.get_pressed()
                    
            if n > (len(l)-1):
                ############################### Surviving or Losing Conditions ############################### 
                o1 = random.randint(1,2)
                o2 = random.randint(3,4)
                o3 = random.randint(5,6)
                o4 = random.randint(7,8)
                o5 = random.randint(9,10)
                root = tk.Tk()
                T1 = tk.Text(root, height = 1, width = 20)
                T1.pack()
                for h1 in l:
                    if h1 == o1 or h1 == o2 or h1 == o3 or h1 == o4 or h1 == o5:
                        ef[l.index(h1)][1] += 10
                    else:
                        T1.insert(tk.END,names[l.index(h1)]+" has died.\n")
                        T1.configure(font = ("helvetica",20,"bold"))
                        names.remove(names[l.index(h1)])
                        do.append(ef.pop(l.index(h1)))
                        l.remove(h1)
                root.mainloop()
                done = False
                
            else:
                ##################################### Controls ######################################
                if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and pl[n].x <= 1102:
                    pl[n].x += 2
                if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and pl[n].x >= 0:
                    pl[n].x -= 2
                if (keys[pygame.K_UP] or keys[pygame.K_w]) and pl[n].y >= 0:
                    pl[n].y -= 2
                if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and pl[n].y <= 505:
                    pl[n].y += 2

                for wall in walls:
                    if pl[n].colliderect(wall):
                        pl[n].y -= 10
                    
                if pl[n].y >= 505:
                    if 40 < pl[n].x < 110:
                        l[n] = 1
                    elif 150 < pl[n].x < 220:
                        l[n] = 2
                    elif 260 < pl[n].x < 330:
                        l[n] = 3
                    elif 370 < pl[n].x < 440:
                        l[n] = 4
                    elif 480 < pl[n].x < 550:
                        l[n] = 5
                    elif 590 < pl[n].x < 660:
                        l[n] = 6
                    elif 700 < pl[n].x < 770:
                        l[n] = 7
                    elif 810 < pl[n].x < 880:
                        l[n] = 8
                    elif 920 < pl[n].x < 990:
                        l[n] = 9
                    elif 1030 < pl[n].x < 1100:
                        l[n] = 10
                    n += 1

            ########################################### Graphics ##########################################
            screen.fill((255,255,255))
            for wall in walls:
                pygame.draw.rect(screen, (0,0,0), wall)
            for char in ch:
                pygame.draw.rect(screen, (0,0,255), char)

            pygame.display.flip()
##        pygame.quit()

        ################################################### Win/Lose Conditions #############################################
        if len(names) == 0:
            root = tk.Tk()
            T2 = tk.Text(root, height = 1, width = 20)
            T2.pack()
            T2.insert(tk.END,"Everybody has died :(")
            T2.configure(font = ("helvetica",20,"bold"))
            root.mainloop()
            fl = 0
        elif fl == 0 and len(names) != 0:
            root = tk.Tk()
            T1 = tk.Text(root, height = 3, width = 20)
            T1.pack()
            for m3 in names:
                ef[names.index(m3)][1] += 50
                do.append(ef.pop(names.index(m3)))
                T1.insert(tk.END,m3+",\t")
                T1.configure(font = ("helvetica",20,"bold"))
            T1.insert(tk.END,"\nis/are the WINNERS! Congratulations :)")
            T1.configure(font = ("helvetica",20,"bold"))
            root.mainloop()
        else:
            fl -= 1

    ###################################### Sorting List Based on Scores ###########################################################
    for sot in range(0,len(do)):
        for sor in range(0,len(do)-sot-1):
            if do[sor][1] > do[sor+1][1]:
                do[sor],do[sor+1] = do[sor+1],do[sor]

    ###################################### Scoreboard ##############################################
    ffl = open('EscapeScores.dat','wb')
    pickle.dump(do,ffl)
    ffl.close()
    ffl = open('EscapeScores.dat','rb')
    dis = pickle.load(ffl)
    root = tk.Tk() 
    T4 = tk.Text(root, height = 20, width = 50)
    T4.pack()
    T4.insert(tk.END,"Score\t\t\tName")
    T4.configure(font = ("helvetica",20,"bold"))
    for scc in range(len(dis)-1,-1,-1):
        T4.insert(tk.END,"\n"+str(dis[scc][1])+"\t\t\t"+str(dis[scc][0]))
        T4.configure(font = ("helvetica",15,"bold"))
    root.mainloop()
    
##playes25()
