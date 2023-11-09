#BOTTLE BASH 
import pygame
import sys
import random
import time
import sqlite3

pygame.init()

#Sqlite connections
cn=sqlite3.connect('game_stats.db')
c=cn.cursor()
c.execute("SELECT tbl_name FROM sqlite_schema WHERE tbl_name='gstats'") 
chk=c.fetchall()
if chk==[]:                                         #checking if gstats table exists and creating one if not, to prevent data redundancy 
    c.execute('''CREATE TABLE gstats (Player_Name text,
              Score integer,Difficulty text)''')
    cn.commit()
cn.close()
    
def store_data (pn,hs,df):                             #pn=player name; hs=highscore; function to input user data into DBMS
    cn_1=sqlite3.connect('game_stats.db')
    c_1=cn_1.cursor()                               
    try:
        C=chkplayer(pn,hs,df)
        if C==True:
            exe=("INSERT INTO gstats VALUES(?,?,?)")
            c_1.execute(exe,(pn,hs,df))
            cn_1.commit()
            SS='data entered sucessfully'
            return SS
        else:
            OP='welcome back {0}, your new HighScore is {1}! Difficulty level:{2}'.format(pn,C,df) 
            query="UPDATE gstats SET score=? WHERE Player_Name=? AND Difficulty=?"
            value=C,pn,df
            c_1.execute(query,value)
            cn_1.commit()
            return OP
    except sqlite3.Error as error:
        print('Operation Failed@store_data:', error)
    cn_1.close()

def high_score(df):                                   #function to fetch overall HighScore and PlayerName 
    cn_2=sqlite3.connect('game_stats.db')
    c_2=cn_2.cursor()
    try:
        Qr='SELECT * FROM gstats WHERE Difficulty=? ORDER BY Score DESC'
        c_2.execute(Qr,(df,))    
        HS=c_2.fetchone()
        cn_2.commit()
        return HS
    except sqlite3.Error as error:
        print('Operation Failed@high_score:', error)
    cn_2.close()
    
def clear_table_gstats():                           #function to clear game stats table
    cn_3=sqlite3.connect('game_stats.db')
    c_3=cn_3.cursor()
    try:
        c_3.execute('DELETE FROM gstats')    
        cn_3.commit()
        print('table containing game statistics cleared')
        return 
    except sqlite3.Error as error:
        print('Operation Failed@clear_table_gstats:', error)
    cn_3.close()
    
def chkplayer(p_name,p_score,p_diff):
    cn_4=sqlite3.connect('game_stats.db')
    c_4=cn_4.cursor()
    try:
        exe1=('SELECT * FROM gstats WHERE Player_Name=? AND Difficulty=?') 
        c_4.execute(exe1,(p_name,p_diff))
        p_detail=c_4.fetchone()
        cn_4.commit()
        if p_detail==None:
            return True
        else:
            if p_detail[1]>p_score:
                return p_detail[1]
            else:
                return p_score
    except sqlite3.Error as error:
        print('Operation Failed@chkplayer:', error)
##a='NONE'
##b=0
##a1='NONE'
##b1=0
##a2='NONE'
##b2=0
##store_data(a, b,'easy')
##store_data(a1, b1,'normal')
##store_data(a2, b2,'hard')
#----------------------------------------------------------------------------------------------
SCREEN = pygame.display.set_mode((1300, 690))
pygame.display.set_caption("Menu")
BG = pygame.image.load("project1Background.jpg")
BG = pygame.transform.scale(BG, (1300, 690))

def GAME(dif,Name):
    pygame.init()
    true = True
    name = Name
    life = 4 - dif
    ti = 120 - 30*dif 
    sco = 0
    BB = [(100,0,0),(150,0,0),(125,75,0),(0,0,0),(125,125,0)]
    def timer(s1,s2):
        text3 = font.render("Time: "+str(int(ti-(s2-s1))),True,(0,0,0),(255,255,255))
        trect3 = text3.get_rect()
        trect3.center = (1100,100)
        screen.blit(text3,trect3)
        return int(ti-(s2-s1))
    def countdown(): #To give some time for player to get ready
        t = 3
        while t >= 0:
            time.sleep(1)
            t -= 1
    def score():
        text4 = font.render("Your Score: "+str(sco),True,(0,0,0),(255,255,255))
        trect4 = text4.get_rect()
        trect4.center = (250,200)
        screen.blit(text4,trect4)
    def finalscore(string):
        t = True
        while t == True:
            screen.fill((255,255,255))
            text11 = font.render("Name: "+str(name),True,(0,0,0),(255,255,255))
            trect11 = text11.get_rect()
            trect11.center = (650,50)
            text21 = font.render("Your Score: "+str(sco),True,(0,0,0),(255,255,255))
            trect21 = text21.get_rect()
            trect21.center = (650,200)
            text22 = font.render(string,True,(0,0,0),(255,255,255))
            trect22 = text22.get_rect()
            trect22.center = (650,300)
            text31 = font.render("Click anywhere to continue",True,(0,0,0),(255,255,255))
            trect31 = text31.get_rect()
            trect31.center = (650,500)
            screen.blit(text11,trect11)
            screen.blit(text21,trect21)
            screen.blit(text22,trect22)
            screen.blit(text31,trect31)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if pygame.mouse.get_pressed():
                        pos = pygame.mouse.get_pos()
                        if 0 <= pos[0] <= 1300 and 0 <= pos[1] <= 690:
                            t = False
    screen = pygame.display.set_mode((1300,690))
    capt = pygame.display.set_caption("Bottle Break")
    font = pygame.font.SysFont("Arial Rounded MT Bold",40)
    text1 = font.render("Name: "+str(name),True,(0,0,0),(255,255,255))
    if dif==1:
        HSCORE=high_score('easy')
    elif dif==2:
        HSCORE=high_score('normal')
    elif dif==3:
        HSCORE=high_score('hard')
    HIGHSCORE=("Highest Score:{} , Difficulty:{}").format(HSCORE[1],HSCORE[2])
    text2 = font.render(HIGHSCORE,True,(0,0,0),(255,255,255))
    trect1 = text1.get_rect()
    trect1.center = (650,50)
    trect2 = text2.get_rect()
    trect2.center = (300,100)
    countdown() 
    seconds1 = time.time() 

    try:
        while true == True:
            screen.fill((255,255,255)) 
            screen.blit(text1,trect1) 
            screen.blit(text2,trect2) 
            score()
            bomb = []
            
            if dif == 1:
                bomb = [random.choice([0,1,2,3,4])]
            else:
                blist = [0,1,2,3,4]
                b1 = random.choice(blist)
                blist.remove(b1)
                bomb = [b1,random.choice(blist)] 
            colour = []
            bot = []
            for b in range(0,5):
                bot.append(pygame.Rect(600+b*150,random.randint(300,500),50,150))
                if b in bomb:
                    colour.append(random.choice(BB)) 
                else:
                    colour.append((random.randint(75,205),random.randint(75,205),random.randint(125,205))) 
            text5 = font.render("Bomb Colours: ",True,(0,0,0),(255,255,255))
            trect5 = text5.get_rect()
            trect5.center = (850,200)
            screen.blit(text5,trect5)
            for bombs in range(0,len(BB)):
                pygame.draw.rect(screen,BB[bombs],[1000+50*bombs,190,30,30])
            for bott in range(0,len(bot)):
                pygame.draw.rect(screen,colour[bott],bot[bott])
                pygame.draw.polygon(screen,colour[bott],[(bot[bott].x,bot[bott].y),(bot[bott].x+15,bot[bott].y-20),(bot[bott].x+35,bot[bott].y-20),(bot[bott].x+49.99,bot[bott].y)])
                pygame.draw.rect(screen,colour[bott],[bot[bott].x+18.5,bot[bott].y-35,15,15])
                pygame.draw.rect(screen,(0,0,0),[bot[bott].x-50,bot[bott].y+150,150,690-bot[bott].y-150])
            pygame.display.flip()
                    
            dd = True
            broke = 5 
            while dd == True:
                seconds2 = time.time() 
                zero = timer(seconds1,seconds2) 
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finalscore("You ended the game!")
                        if dif==3:
                            store_data (Name,sco,'hard')
                        elif dif==2:
                            store_data (Name,sco,'normal')
                        elif dif==1:
                            store_data (Name,sco,'easy')
                        true = False
                        screen.exit()

                    for li in range(0,life):
                        pygame.draw.ellipse(screen,(200,0,0),[100*li+40,620,50,50])
                    pygame.display.flip()

                    if event.type == pygame.MOUSEBUTTONUP:
                        if pygame.mouse.get_pressed():
                            pos = pygame.mouse.get_pos()
                            for loc in bot:
                                if loc.y <= pos[1] <= loc.y+150:
                                    if (loc.x <= pos[0] <= (loc.x+50)):
                                        if bot.index(loc) in bomb:
                                            pygame.draw.rect(screen,(255,255,255),[loc.x,loc.y-35,50,185])
                                            pygame.draw.ellipse(screen,(255,255,255),[240-(3-life)*100,620,50,50]) 
                                            bot[bot.index(loc)].x += 1000
                                            bot[bot.index(loc)].y += 1000
                                            life -= 1
                                            if life == 0:
                                                finalscore("All lives spent!")
                                                if dif==3:
                                                    store_data (Name,sco,'hard')
                                                elif dif==2:
                                                    store_data (Name,sco,'normal')
                                                elif dif==1:
                                                    store_data (Name,sco,'easy')
                                                true = False
                                                screen.exit()
                                            else:
                                                pass
                                        else:
                                            sco += 1
                                            score()
                                            pygame.draw.rect(screen,(255,255,255),[loc.x,loc.y-35,50,100])
                                            pygame.draw.polygon(screen,(255,255,255),[(loc.x,loc.y+65),(loc.x+11,loc.y+80),(loc.x+25,loc.y+65)])
                                            pygame.draw.polygon(screen,(255,255,255),[(loc.x+25,loc.y+65),(loc.x+39,loc.y+80),(loc.x+50,loc.y+65)])
                                            pygame.display.flip()
                                            bot[bot.index(loc)].x += 1000
                                            bot[bot.index(loc)].y += 1000
                                            broke -= 1
                                           
                if len(bomb) == broke:
                    break
                elif zero <= 0:
                    finalscore("Time up!")
                    if dif==3:
                        store_data (Name,sco,'hard')
                    elif dif==2:
                        store_data (Name,sco,'normal')
                    elif dif==1:
                        store_data (Name,sco,'easy')
                    true = False
                    screen.exit()
                else:
                    pass
    except:
        None
        
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
            
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("Alferian", size)

def SCORES(dif):
    while True:
        SCORES_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")
        if dif==1:
            HSCORE=high_score('easy')
        elif dif==2:
            HSCORE=high_score('normal')
        elif dif==3:
            HSCORE=high_score('hard')
        HIGHSCORE=("PLAYER NAME:{}    HIGHEST SCORE:{}    DIFFICULTY:{}").format(HSCORE[0],HSCORE[1],HSCORE[2])
        OPTIONS_TEXT = get_font(45).render(HIGHSCORE, True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        PLAY_BACK = Button(image=None, pos=(640, 600), 
                                text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        PLAY_BACK.changeColor(SCORES_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(SCORES_MOUSE_POS):
                        options()
        pygame.display.update()

def start(dif):
    base_font = pygame.font.Font(None, 50)
    user_text = ''
    input_rect = pygame.Rect(200, 150, 900, 50)
    colour = pygame.Color('maroon')
    while True:
        START_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill((0, 0, 100))
        PLAY_TEXT = get_font(45).render("ENTER PLAYER NAME", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_TEXT0 = get_font(25).render("INSTRUCTIONS:", True, "Yellow")
        PLAY_TEXT1 = get_font(25).render("Click on the rectangular base of the bottle to break it.", True, "White")
        PLAY_TEXT2 = get_font(25).render("Do not click on a bomb or you lose a life (bomb colours are shown above the bottles).", True, "White")
        PLAY_TEXT3 = get_font(25).render("You have "+str(4-dif)+" lives in total (shown as red circles in bottom left).", True, "White")
        PLAY_TEXT4 = get_font(25).render("After all bottles in a given iteration are broken, new bottles (and bombs) will be generated.", True, "White")
        PLAY_TEXT5 = get_font(25).render("You have a total time of "+str(120 - 30*dif)+" seconds to break as many bottles as possible.", True, "White")
        PLAY_RECT0 = PLAY_TEXT1.get_rect(center=(340, 250))
        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(340, 280))
        PLAY_RECT2 = PLAY_TEXT1.get_rect(center=(340, 310))
        PLAY_RECT3 = PLAY_TEXT1.get_rect(center=(340, 340))
        PLAY_RECT4 = PLAY_TEXT1.get_rect(center=(340, 370))
        PLAY_RECT5 = PLAY_TEXT1.get_rect(center=(340, 400))
        SCREEN.blit(PLAY_TEXT0, PLAY_RECT0)
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)
        SCREEN.blit(PLAY_TEXT2, PLAY_RECT2)
        SCREEN.blit(PLAY_TEXT3, PLAY_RECT3)
        SCREEN.blit(PLAY_TEXT4, PLAY_RECT4)
        SCREEN.blit(PLAY_TEXT5, PLAY_RECT5)
        START_BUTTON = Button(image=None, pos=(240, 500), 
                            text_input="START", font=get_font(75), base_color="White", hovering_color="Green")
        START_BUTTON.changeColor(START_MOUSE_POS)
        START_BUTTON.update(SCREEN)
        PLAY_BACK = Button(image=None, pos=(1060, 500), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(START_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        pygame.draw.rect(SCREEN, colour, input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255)) 
        SCREEN.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
      
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(START_MOUSE_POS):
                    play()
                if START_BUTTON.checkForInput(START_MOUSE_POS):
                    GAME(dif,user_text)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                # Unicode standard is used for string formation
                else:
                    user_text += event.unicode
    pygame.display.update()
    
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        EASY_BUTTON = Button(image=pygame.image.load("Rectangle1.jpg"), pos=(240, 250), 
                            text_input="EASY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        EASY_BUTTON.changeColor(PLAY_MOUSE_POS)
        EASY_BUTTON.update(SCREEN)
        NORMAL_BUTTON = Button(image=pygame.image.load("Rectangle1.jpg"), pos=(640, 250), 
                            text_input="NORMAL", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        NORMAL_BUTTON.changeColor(PLAY_MOUSE_POS)
        NORMAL_BUTTON.update(SCREEN)
        HARD_BUTTON = Button(image=pygame.image.load("Rectangle1.jpg"), pos=(1040, 250), 
                            text_input="HARD", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        HARD_BUTTON.changeColor(PLAY_MOUSE_POS)
        HARD_BUTTON.update(SCREEN)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if EASY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    start(1)
                if NORMAL_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    start(2)
                if HARD_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    start(3)

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        SCORE_EASY = Button(image=pygame.image.load("Rectangle1.jpg"), pos=(240, 250), 
                            text_input="Easy Difficulty", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        SCORE_EASY.changeColor(OPTIONS_MOUSE_POS)
        SCORE_EASY.update(SCREEN)
        SCORE_NORMAL = Button(image=pygame.image.load("Rectangle1.jpg"), pos=(640, 250), 
                            text_input="Normal Difficulty", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        SCORE_NORMAL.changeColor(OPTIONS_MOUSE_POS)
        SCORE_NORMAL.update(SCREEN)
        SCORE_HARD = Button(image=pygame.image.load("Rectangle1.jpg"), pos=(1040, 250), 
                            text_input="Hard Difficulty", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        SCORE_HARD.changeColor(OPTIONS_MOUSE_POS)
        SCORE_HARD.update(SCREEN)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if SCORE_EASY.checkForInput(OPTIONS_MOUSE_POS):
                    SCORES(1)
                if SCORE_NORMAL.checkForInput(OPTIONS_MOUSE_POS):
                    SCORES(2)
                if SCORE_HARD.checkForInput(OPTIONS_MOUSE_POS):
                    SCORES(3)

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("BOTTLE BASH", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Rectangle1.jpg"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Rectangle1.jpg"), pos=(640, 400), 
                            text_input="HIGH SCORES", font=get_font(70), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Rectangle1.jpg"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
main_menu()
cn.close()
