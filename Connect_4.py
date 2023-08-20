def playc4():
    import tkinter as tk
    import pygame
    import pygame.locals
    pygame.init()

    root = tk.Tk()
    T33 = tk.Text(root, height = 20, width = 110)
    T33.pack()
    T33.insert(tk.END,"HOW TO PLAY:\nThere will be 2 players.\nPlayer 1 will have to left-click on one of the bottom circles to fill red colour into it.\nPlayer 2 has to do the same during his/her turn, but the circle he/she chooses will be filled with yellow colour.\nIf the player selects any circle other than the bottom one, the bottom-most circle which is empty will be filled by default with the player's colour.\n\nCONDITIONS TO WIN:\nThe first player to fill 4 continuous circles with his/her colour either vertically, horizontally or diagonally wins the game.\n\nCONTROLS:\nMouse Left-Click to fill the player's colour to the empty circle.")
    T33.configure(font = ("helvetica",15,"bold"))
    root.mainloop()
    
    p1_player=input('Enter your name player 1: ')
    p2_player=input('Enter your name player 2: ')

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1360,690))
    capt = pygame.display.set_caption("Connect 4")
    done = True
    y1 = y2 = y3 = y4 = y5 = y6 = y7 = 570

    screen.fill((0,0,255))
    for i1 in range(0,660,110):
        for j1 in range(0,1320,198):
            pygame.draw.ellipse(screen,(255,255,255),[30+j1,20+i1,100,100],0)

    for i2 in range(0,1188,198):
        pygame.draw.rect(screen,(0,0,0),[170+i2,0,15,690],0)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    ## Checks who has won

    def win(cn4):

        win_1=False
        win_2=False

        ## Vertical win check
        for i in range(7):
            for j in range(3):
                if cn4[i][j]==cn4[i][j+1]==cn4[i][j+2]==cn4[i][j+3]==1:
                    win_1=True
                    win_1_cord=[[i,j],[i,j+1],[i,j+2],[i,j+3]]
                elif cn4[i][j]==cn4[i][j+1]==cn4[i][j+2]==cn4[i][j+3]==2:
                    win_2=True
                    win_2_cord=[[i,j],[i,j+1],[i,j+2],[i,j+3]]
                else:
                    pass

        ## Horizontal win check
        for i in range(6):
            for j in range(4):
                if cn4[j][i]==cn4[j+1][i]==cn4[j+2][i]==cn4[j+3][i]==1:
                    win_1=True
                    win_1_cord=[[j,i],[j+1,i],[j+2,i],[j+3,i]]
                elif cn4[j][i]==cn4[j+1][i]==cn4[j+2][i]==cn4[j+3][i]==2:
                    win_2=True
                else:
                    pass

        ## Increasing diagnol check
        for i in range(3):
            for j in range(4):
                if cn4[j][i]==cn4[j+1][i+1]==cn4[j+2][i+2]==cn4[j+3][i+3]==1:
                    win_1=True
                elif cn4[j][i]==cn4[j+1][i+1]==cn4[j+2][i+2]==cn4[j+3][i+3]==2:
                    win_2=True
                else:
                    pass


        ## Decreasing diagnol check
        for i in range(4):
            for j in range(5,2,-1):
                if cn4[i][j]==cn4[i+1][j-1]==cn4[i+2][j-2]==cn4[i+3][j-3]==1:
                    win_1=True
                elif cn4[i][j]==cn4[i+1][j-1]==cn4[i+2][j-2]==cn4[i+3][j-3]==2:
                    win_2=True
                else:
                    pass

        if win_1==True:
            return('p1')
        elif win_2==True:
            return('p2')
        else:
            return(None)





    ## Checks whether game has ended or not

    def still_play(cn4):
        play=False
        for i in range(len(cn4)):
            for j in range(len(cn4[i])):
                if cn4[i][j]==0 and win(cn4)==None:
                    play=True
                    break
                else:
                    pass
        return(play)





    ## Checks whether column is full or not

    def col_full(cn4):
        k=True
        for i in range(len(cn4)):
            if cn4[i]==0:
                k=False
                break
        return(k)





    ## Master Code

    cn4=[[0 for i in range(6)] for i in range(7)]

    while still_play(cn4)==True:

        ##Player 1

        while True:
            p1 = 0
            ############## Controls and Graphics ################
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x,y = pygame.mouse.get_pos()
                        if x >= 0 and x <= 170 and y1 >= 20:
                            p1 = 1
                            pygame.draw.ellipse(screen, (255,0,0), [30,y1,100,100])
                            y1 -= 110
                        if x >= 185 and x <= 355 and y2 >= 20:
                            p1 = 2
                            pygame.draw.ellipse(screen, (255,0,0), [228,y2,100,100])
                            y2 -= 110
                        if x >= 370 and x <= 540 and y3 >= 20:
                            p1 = 3
                            pygame.draw.ellipse(screen, (255,0,0), [426,y3,100,100])
                            y3 -= 110
                        if x >= 555 and x <= 725 and y4 >= 20:
                            p1 = 4
                            pygame.draw.ellipse(screen, (255,0,0), [624,y4,100,100])
                            y4 -= 110
                        if x >= 740 and x <= 910 and y5 >= 20:
                            p1 = 5
                            pygame.draw.ellipse(screen, (255,0,0), [822,y5,100,100])
                            y5 -= 110
                        if x >= 925 and x <= 1105 and y6 >= 20:
                            p1 = 6
                            pygame.draw.ellipse(screen, (255,0,0), [1020,y6,100,100])
                            y6 -= 110
                        if x >= 1120 and x <= 1360 and y7 >= 20:
                            p1 = 7
                            pygame.draw.ellipse(screen, (255,0,0), [1218,y7,100,100])
                            y7 -= 110
            pygame.display.flip()
            
            if p1<=7 and p1>0 and type(p1)==int and col_full(cn4[p1-1])==False:
                break
            else:
                # if (col_full(cn4[p1-1])==True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                #     root = tk.Tk()
                #     T11 = tk.Text(root, height = 1, width = 80)
                #     T11.pack()
                #     T11.insert(tk.END,"Column is full. Please choose another column.")
                #     T11.configure(font = ("helvetica",20,"bold"))
                #     root.mainloop()
                pass

        for i in range(len(cn4[p1-1])):
            if cn4[p1-1][i]==0:
                cn4[p1-1][i]=1
                break	

        if still_play(cn4)==False:
            break


        ## Player 2

        while True:
            p2 = 0
            ############## Controls and Graphics ###############
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x,y = pygame.mouse.get_pos()
                        if x >= 0 and x <= 170 and y1 >= 20:
                            p2 = 1
                            pygame.draw.ellipse(screen, (255,255,0), [30,y1,100,100])
                            y1 -= 110
                        elif x >= 185 and x <= 355 and y2 >= 20:
                            p2 = 2
                            pygame.draw.ellipse(screen, (255,255,0), [228,y2,100,100])
                            y2 -= 110
                        elif x >= 370 and x <= 540 and y3 >= 20:
                            p2 = 3
                            pygame.draw.ellipse(screen, (255,255,0), [426,y3,100,100])
                            y3 -= 110
                        elif x >= 555 and x <= 725 and y4 >= 20:
                            p2 = 4
                            pygame.draw.ellipse(screen, (255,255,0), [624,y4,100,100])
                            y4 -= 110
                        elif x >= 740 and x <= 910 and y5 >= 20:
                            p2 = 5
                            pygame.draw.ellipse(screen, (255,255,0), [822,y5,100,100])
                            y5 -= 110
                        elif x >= 925 and x <= 1105 and y6 >= 20:
                            p2 = 6
                            pygame.draw.ellipse(screen, (255,255,0), [1020,y6,100,100])
                            y6 -= 110
                        elif x >= 1120 and x <= 1360 and y7 >= 20:
                            p2 = 7
                            pygame.draw.ellipse(screen, (255,255,0), [1218,y7,100,100])
                            y7 -= 110
            pygame.display.flip()
            
            if p2<=7 and p2>0 and type(p1)==int and col_full(cn4[p2-1])==False:
                break
            else:
                if col_full(cn4[p2-1])==True:
                    root = tk.Tk()
                    T22 = tk.Text(root, height = 1, width = 80)
                    T22.pack()
                    T22.insert(tk.END,"Column is full. Please choose another column.")
                    T22.configure(font = ("helvetica",20,"bold"))
                    root.mainloop()
                    
        for j in range(len(cn4[p2-1])):
            if cn4[p2-1][j]==0:
                cn4[p2-1][j]=2
                break	

        if still_play(cn4)==False:
            break

    ## Declaring winner
    if win(cn4)=='p1':
        root = tk.Tk()
        T1 = tk.Text(root, height = 1, width = 50)
        T1.pack()
        T1.insert(tk.END,p1_player+" is the WINNER! Congratulations :)")
        T1.configure(font = ("helvetica",20,"bold"))
        root.mainloop()
    elif win(cn4)=='p2':
        root = tk.Tk()
        T2 = tk.Text(root, height = 1, width = 50)
        T2.pack()
        T2.insert(tk.END,p2_player+" is the WINNER! Congratulations :)")
        T2.configure(font = ("helvetica",20,"bold"))
        root.mainloop()
    elif win(cn4)==None:
        root = tk.Tk()
        T3 = tk.Text(root, height = 1, width = 50)
        T3.pack()
        T3.insert(tk.END,"TIE :|")
        T3.configure(font = ("helvetica",20,"bold"))
        root.mainloop()
