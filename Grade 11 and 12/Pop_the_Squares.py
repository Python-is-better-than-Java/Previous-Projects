def playps():
    import pygame
    import pygame.locals
    import tkinter as tk
    import os
    import random
    import pickle
    pygame.init()

    root = tk.Tk()
    T11 = tk.Text(root, height = 20, width = 110)
    T11.pack()
    T11.insert(tk.END,"HOW TO PLAY:\nIn this game, the green circle is the player.\nThe brownish-pink shapes are walls. The player cannot go through them (there may be exceptions in a few walls).\nThe player needs to pop the dark blue square (target square) by colliding with it.\nWhen a dark blue square is popped, one of the 14 other brown squares will become dark blue, which also has to be popped.\nThis continues until you pop 15 dark blue squares.\n\nFollowing will result in 'GAME OVER'-\n1. Colliding with a brown square.\n2. Colliding with any of the 4 cyan colour 'barriers' surrounding the target square.\n\nIf you successfully pop all 15 target squares, you WIN THE GAME!\n\nCONTROLS:\n1. UP Arrowkey or 'w' to move up.\n2. DOWN Arrowkey or 's' to move down.\n3. RIGHT Arrowkey or 'd' to move right.\n4. LEFT Arrowkey or 'a' to move left.")
    T11.configure(font = ("helvetica",15,"bold"))
    root.mainloop()

    ######################## Creating the Screen ############################
    screen = pygame.display.set_mode((1360,690))
    capt = pygame.display.set_caption("Pop the Squares")
    done = True

    ########################## Creating the Player, Squares and Walls ###############################
    if os.path.exists("PopScores.dat"):
        os.remove("PopScores.dat")
    else:
        pass
    
    L = []
    sc = []
    for i in range(1,31):
        L.append(pygame.Rect(random.randint(0,1360),random.randint(10,650),random.randint(50,150),random.randint(50,150)))
    char = pygame.Rect(0,0,15,15)
    V = []
    W1 = []
    G1 = []
    G2 = []
    G3 = []
    G4 = []
    for j in range(1,16):
        ab = random.randint(150,1210)
        ac = random.randint(100,550)
        V.append(pygame.Rect(ab,ac,40,40))
        W1.append(pygame.Rect(ab,ac,40,40))
        G1.append(pygame.Rect(ab+50,ac+10,20,20))
        G2.append(pygame.Rect(ab+10,ac+50,20,20))
        G3.append(pygame.Rect(ab-30,ac+10,20,20))
        G4.append(pygame.Rect(ab+10,ac-30,20,20))

    ############################### Game code #############################################
    while done == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False

        ##################### Controls ######################        
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (char.x <= 1350):
            char.x += 1
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (char.x >= 5):
            char.x -= 1
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and (char.y >= 5):
            char.y -= 1
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (char.y <= 680):
            char.y += 1

        ################## Placements and Movements of the Player and Squares #########################
        
        for i2 in L:
            if char.colliderect(i2):
                if i2.x <= char.x:
                    char.x += 1
                if i2.x >= char.x:
                    char.x -= 1
                if i2.y >= char.y:
                    char.y -= 1
                if i2.y <= char.y:
                    char.y += 1

            for j2 in V:
                if j2.colliderect(i2):
                    if i2.x <= j2.x:
                        j2.x += 1
                    if i2.x >= j2.x:
                        j2.x -= 1
                    if i2.y >= j2.y:
                        j2.y -= 1
                    if i2.y <= j2.y:
                        j2.y += 1

        for j3 in W1:
            for i3 in V:
                j3.x = i3.x
                j3.y = i3.y
        for j4 in G1:
            for i4 in V:
                j4.x = i4.x + 50
                j4.y = i4.y + 10
        for j5 in G2:
            for i5 in V:
                j5.x = i5.x + 10
                j5.y = i5.y + 50
        for j6 in G3:
            for i6 in V:
                j6.x = i6.x - 30
                j6.y = i6.y + 10
        for j7 in G4:
            for i7 in V:
                j7.x = i7.x + 10
                j7.y = i7.y - 30

        #################################### Win/Lose Conditions #############################################
        for c1 in range(0,len(G1)):
            if (char.colliderect(G1[c1]) or char.colliderect(G2[c1]) or char.colliderect(G3[c1]) or char.colliderect(G4[c1])):
                fyay = open('PopScores.dat','wb')
                pickle.dump(sc,fyay)
                fyay.close()
                fyay = open('PopScores.dat','rb')
                finish2 = pickle.load(fyay)
                fyay.close()
                sumsco = 0
                for fin2 in finish2:
                    sumsco += fin2
                root = tk.Tk()
                T5 = tk.Text(root, height = 1, width = 60)
                T5.pack()
                T5.insert(tk.END,"You collided with a barrier. GAME OVER. Your score is "+str(sumsco))
                T5.configure(font = ("helvetica",20,"bold"))
                root.mainloop()
                done = False
                break
                    
        for a1 in W1:
            for b1 in V:
                if char.colliderect(a1) and char.colliderect(b1):
                    V.remove(b1)
                    sc.append(10)
                if char.colliderect(a1) == False and char.colliderect(b1) == True:
                    V.remove(b1)
                    fyay = open('PopScores.dat','wb')
                    pickle.dump(sc,fyay)
                    fyay.close()
                    fyay = open('PopScores.dat','rb')
                    finish = pickle.load(fyay)
                    fyay.close()
                    sumsco = 0
                    for fin in finish:
                        sumsco += fin
                    root = tk.Tk()
                    T1 = tk.Text(root, height = 1, width = 60)
                    T1.pack()
                    T1.insert(tk.END,"You collided with a brown square. GAME OVER. Your score is "+str(sumsco))
                    T1.configure(font = ("helvetica",20,"bold"))
                    root.mainloop()
                    done = False
                    break
            break

        ################################## Win Decleration and Score ########################################
        if V == []:
            sc.append(20)
            fyay = open('PopScores.dat','wb')
            pickle.dump(sc,fyay)
            fyay.close()
            fyay = open('PopScores.dat','rb')
            wonall = pickle.load(fyay)
            fyay.close()
            sumscowon = 0
            for al in wonall:
                sumscowon += al
            root = tk.Tk()
            T2 = tk.Text(root, height = 1, width = 35)
            T2.pack()
            T2.insert(tk.END,"YOU WON! Your final score is "+str(sumscowon))
            T2.configure(font = ("helvetica",20,"bold"))
            root.mainloop()
            done = False

        ################################### Graphics #####################################
        screen.fill((255,255,255))
        for i in L:
            pygame.draw.rect(screen, (200,150,115), i)
        pygame.draw.ellipse(screen, (0,150,0), char)
        for j in V:
            pygame.draw.rect(screen, (200,100,10), j)
        for k in W1:
            pygame.draw.rect(screen,(20,12,50), k)
        for m1 in G1:
            pygame.draw.rect(screen,(0,150,150), m1)
        for m2 in G2:
            pygame.draw.rect(screen,(0,150,150), m2)
        for m3 in G3:
            pygame.draw.rect(screen,(0,150,150), m3)
        for m4 in G4:
            pygame.draw.rect(screen,(0,150,150), m4)
        pygame.display.flip()
##    pygame.quit()
##playps()
