from random import randint, choice
from pickle import load, dump
from threading import Timer
import msvcrt, os, time
global txt_game_over
global txt_you_won
global txt_you_lose
global time
global hs
global score
global t
cd = None


def start() :
    global txt_game_over
    global txt_you_won
    global txt_you_lose
    txt2048_1 = '\n\n\n\n\n\n\n\n' + '''                   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
                  |                                         |
                  |         ╗         ╗    ╗    ╗       ╗   |
                  |   ╚════  ╗   ╔═    ╗   ║    ║   ╔══  ╗  |
                  |         ╔╝   ║  ╔  ║        ║ ╚     ╔╝  |
                  |     ╔═══╝      ╔╝  ║ ╚════  ║   ╔══  ╗  |
                  |          ╗ ╚      ╔╝        ║ ╚     ╔╝  |
                  |   ╚══════╝  ╚═════╝       ╚═╝  ╚════╝   |
		  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|'''

    txt2048_2 = '\n\n\n\n\n\n\n\n' + '''                  ╔═════════════════════════════════════════╗
                  ║                                         ║
                  ║   ██████╗   ██████╗  ██╗  ██╗  █████╗   ║
                  ║   ╚════██╗ ██╔═████╗ ██║  ██║ ██╔══██╗  ║
                  ║    █████╔╝ ██║██╔██║ ███████║ ╚█████╔╝  ║
                  ║   ██╔═══╝  ████╔╝██║ ╚════██║ ██╔══██╗  ║
                  ║   ███████╗ ╚██████╔╝      ██║ ╚█████╔╝  ║
                  ║   ╚══════╝  ╚═════╝       ╚═╝  ╚════╝   ║
                  ╚═════════════════════════════════════════╝'''

    txt_game_over = '\n\n\n\n\n\n\n' + '''   	██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
       ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
       ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
       ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
       ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
        ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝'''

    txt_you_won = '\n\n\n\n\n\n\n' + '''     	    ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗
            ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║
             ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║
              ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║
               ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║
               ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝'''

    txt_you_lose = '\n\n\n\n\n\n\n\n' + u'''      	  ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗
          ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝
           ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗  
            ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝  
             ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗
             ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝'''
    
    for x in range(3):  
        print(txt2048_1)
        time.sleep(0.2)
        os.system('cls')
        print(txt2048_2)
        time.sleep(0.8)
        os.system('cls')
        time.sleep(0.2)
    os.system('cls')



def menu():
    m11 = '\n\n' + '''                                  ╔═════════════╗
                                  ║   New Game  ║
                                  ╚═════════════╝
                                   
                                      Resume     
                                   
                                   
                                       Modes     
                                   
                                   
                                    Statistics   
                                   
                                   
                                    How To Play
                                   
                                   
                                       About    
                                   
                                   
                                     Quit Game   
                                   '''

    m12 = '\n\n' + '''                                   
                                      New Game   
                                   
                                  ╔═════════════╗
                                  ║   Resume    ║
                                  ╚═════════════╝
                                   
                                       Modes     
                                   
                                   
                                    Statistics   
                                   
                                   
                                    How To Play
                                   
                                   
                                       About
                                   
                                   
                                     Quit Game   
                                   '''

    m13 = '\n\n' + '''                                   
                                      New Game   
                                   
                                   
                                      Resume     
                                   
                                  ╔═════════════╗
                                  ║    Modes    ║
                                  ╚═════════════╝
                                   
                                    Statistics   
                                   
                                   
                                    How To Play  
                                   
                                   
                                       About     
                                   
                                   
                                     Quit Game   
                                   '''

    m14 = '\n\n' + '''                                   
                                      New Game   
                                   
                                   
                                      Resume     
                                   
                                   
                                       Modes     
                                   
                                  ╔═════════════╗
                                  ║ Statistics  ║
                                  ╚═════════════╝
                                   
                                    How To Play  
                                   
                                   
                                       About     
                                   
                                   
                                     Quit Game   
                                   '''

    m15 = '\n\n' + '''                                   
                                      New Game   
                                   
                                   
                                      Resume     
                                   
                                   
                                       Modes     
                                   
                                   
                                    Statistics   
                                   
                                  ╔═════════════╗
                                  ║ How To Play ║
                                  ╚═════════════╝
                                   
                                       About     
                                   
                                   
                                     Quit Game   
                                   '''

    m16 = '\n\n' + '''                                   
                                      New Game   
                                   
                                   
                                      Resume     
                                   
                                   
                                       Modes     
                                   
                                   
                                    Statistics   
                                   
                                   
                                    How To Play  
                                   
                                  ╔═════════════╗
                                  ║    About    ║
                                  ╚═════════════╝
                                   
                                     Quit Game   
                                   '''

    m17 = '\n\n' + '''                                   
                                      New Game   
                                   
                                   
                                      Resume     
                                   
                                   
                                       Modes     
                                   
                                   
                                    Statistics   
                                   
                                   
                                    How To Play  
                                   
                                   
                                       About     
                                   
                                  ╔═════════════╗
                                  ║  Quit Game  ║
                                  ╚═════════════╝'''


    m01 = '\n\n\n' + '''                                  ╔═════════════╗
                                  ║   New Game  ║
                                  ╚═════════════╝
                                   
                                       Modes     
                                   
                                   
                                    Statistics   
                                   
                                   
                                    How To Play  
                                   
                                   
                                       About     
                                   
                                   
                                     Quit Game   
                                   '''


    m02 = '\n\n\n' + '''                                   
                                      New Game   
                                   
                                  ╔═════════════╗
                                  ║    Modes    ║
                                  ╚═════════════╝
                                   
                                    Statistics   
                                   
                                   
                                    How To Play  
                                   
                                   
                                       About     
                                   
                                   
                                     Quit Game   
                                   '''

    m03 = '\n\n\n' + '''                                   
                                      New Game   
                                   
                                   
                                       Modes     
                                   
                                  ╔═════════════╗
                                  ║ Statistics  ║
                                  ╚═════════════╝
                                   
                                    How To Play  
                                   
                                   
                                       About     
                                   
                                   
                                     Quit Game   
                                   '''

    m04 = '\n\n\n' + '''                                   
                                      New Game   
                                   
                                   
                                       Modes     
                                   
                                   
                                    Statistics   
                                   
                                  ╔═════════════╗
                                  ║ How To Play ║
                                  ╚═════════════╝
                                   
                                       About     
                                   
                                   
                                     Quit Game   
                                   '''

    m05 = '\n\n\n' + '''                                   
                                      New Game   
                                   
                                   
                                       Modes     
                                   
                                   
                                    Statistics   
                                   
                                   
                                    How To Play  
                                   
                                  ╔═════════════╗
                                  ║    About    ║
                                  ╚═════════════╝
                                   
                                     Quit Game   
                                   '''

    m06 = '\n\n\n' + '''                                   
                                      New Game   
                                   
                                   
                                       Modes     
                                   
                                   
                                    Statistics   
                                   
                                   
                                    How To Play  
                                   
                                   
                                       About     
                                   
                                  ╔═════════════╗
                                  ║  Quit Game  ║
                                  ╚═════════════╝'''


    menu = {1 : [m11, m12, m13, m14, m15, m16, m17], 0 : [m01, m02, m03, m04, m05, m06]}
    if not os.path.exists('_lib.pyd'):
        p = 0
        size, mode = '4x4', 'classic'
    else :
        file = open('_lib.pyd', 'rb')
        data = load(file)
        file.close()
        size, mode = data['savegame']['psize'], data['savegame']['pmode']
        if data['savegame'][size][mode][0] == [] :
            p = 0
        else :
            p = 1
    i = p
    while True :
        print(menu[p][i])
        nav = keypress()
        while nav != 'return' and nav != 'spacebar' :
            if nav == 'up' :
                i = i - 1
            elif nav == 'down' :
                i = i + 1
            else :
                nav = keypress()
                continue

            if i not in [x for x in range(len(menu[p]))] :
                if i < 0 :
                    i = 0
                else :
                    i = len(menu[p]) - 1
                nav = keypress()
                continue
            os.system('cls')
            print(menu[p][i])
            nav = keypress()

        if p == 0 :
            if i == 0 :
                return size, mode
            elif i == 1 :
                size, mode = modes(size, mode)
                if os.path.exists('_lib.pyd') :
                    file = open('_lib.pyd', 'rb')
                    data = load(file)
                    file.close()
                    if data['savegame'][size][mode][0] != [] :
                        p = 1
                        i = 2
                        continue
            elif i == 2 :
                statistics()
            elif i == 3 :
                howtoplay()
            elif i == 4 :
                about()
            else :
                if quitgame() :
                    quit()
        else :
            if i == 0 :
                file = open('_lib.pyd', 'rb')
                data = load(file)
                file.close()
                data['savegame'][size][mode] = [[], 0]
                file = open('_lib.pyd', 'wb')
                dump(data, file)
                file.close()
                return size, mode
            elif i == 1 :
                return size, mode
            elif i == 2 :
                size, mode = modes(size, mode)
                file = open('_lib.pyd', 'rb')
                data = load(file)
                file.close()
                if data['savegame'][size][mode][0] == [] :
                    p = 0
                    i = 1
                    continue
            elif i == 3 :
                statistics()
            elif i == 4 :
                howtoplay()
            elif i == 5 :
                about()
            else :
                if quitgame() :
                    exit(0)


def modes(psize, pmode):
    os.system('cls')
    print('\n\n\n\n\n\n\t\t\t\t  SELECT MODE\n\n')
    s1 = '''            ╔══════════╗                                             
            ║ Practice ║      Classic        X-Tile        Survival  
            ╚══════════╝                                             '''
    s2 = '''                            ╔══════════╗                             
              Practice      ║ Classic  ║     X-Tile        Survival  
                            ╚══════════╝                             '''
    s3 = '''                                          ╔══════════╗               
              Practice        Classic     ║  X-Tile  ║     Survival  
                                          ╚══════════╝               '''
    s4 = '''                                                         ╔══════════╗
              Practice        Classic        X-Tile      ║ Survival ║
                                                         ╚══════════╝'''

    i1 = '\n\n' + '''                       Your goal is to create 2048 tile!
                         You have option to undo up to
                                20 last moves.'''
    i2 = '\n\n' + '''                       Your goal is to create 2048 tile!
                          You can't undo your moves.'''
    i3 = '\n\n' + '''                       Your goal is to create 2048 tile!
                         X tile cannot be merged. Beat
                                new challenge!'''
    i4 = '\n\n' + '''                          Survive as long as you can.
                            Create new tiles to get
                          additional time: 16-64 = 2
                                   seconds.'''

    x4 = '''                           ╔═══════╗                 
                           ║ 4 x 4 ║          5 x 5  
                           ╚═══════╝                 '''
    x5 = '''                                            ╔═══════╗
                             4 x 4          ║ 5 x 5 ║
                                            ╚═══════╝'''
    
    
    select_mode = [s1, s2, s3, s4]
    modeinfo = [i1, i2, i3, i4]
    modemap = ['practice', 'classic', 'xtile', 'survival']
    select_size = [x4, x5]
    sizemap = ['4x4', '5x5']
    i = modemap.index(pmode)
    j = sizemap.index(psize)
    print(select_mode[i])
    print(modeinfo[i])
    nav = keypress()
    while nav != 'return' and nav != 'spacebar' :
        if nav == 'left' :
            i = i - 1
        elif nav == 'right' :
            i = i + 1
        else :
            nav = keypress()
            continue

        if i not in [x for x in range(4)] :
            if i < 0 :
                i = 0
            else :
                i = 3
            nav = keypress()
            continue
        os.system('cls')
        print('\n\n\n\n\n\n\t\t\t\t  SELECT MODE\n\n')
        print(select_mode[i])
        print(modeinfo[i])
        nav = keypress()
    mode = modemap[i]
    os.system('cls')
    print('\n\n\n\n\n\n\n\n\t\t\t\t  SELECT SIZE\n\n')
    print(select_size[j])
    nav = keypress()
    while nav != 'return' and nav != 'spacebar' :
        if nav == 'left' :
            j = 0
        elif nav =='right' :
            j = 1
        else :
            nav = keypress()
            continue
        
        os.system('cls')
        print('\n\n\n\n\n\n\n\n\t\t\t\t  SELECT SIZE\n\n')
        print(select_size[j])
        nav = keypress()
    size = sizemap[j]
    os.system('cls')
    return size, mode


def statistics():
    if os.path.exists('_lib.pyd') :
        file = open('_lib.pyd', 'rb')
        data = load(file)
        p4 = data['best']['4x4']['practice']
        c4 = data['best']['4x4']['classic']
        x4 = data['best']['4x4']['xtile']
        s4 = data['best']['4x4']['survival']
        p5 = data['best']['5x5']['practice']
        c5 = data['best']['5x5']['classic']
        x5 = data['best']['5x5']['xtile']
        s5 = data['best']['5x5']['survival']
    else :
        p4 = c4 = x4 = s4 = p5 = c5 = x5 = s5 = 0
    os.system('cls')
    print('\n\n\n\n\t\t\t\tStatistic : Best Score\n\n')
    print('\t\t\t╔'+'═'*17+ '╦' +'═'*9+'╦' +'═'*9+'╗')
    print('\t\t\t║ {0:15s} ║ {1:7s} ║ {2:7s} ║'.format('', '  4x4', '  5x5'))
    print('\t\t\t╠'+'═'*17+ '╬' +'═'*9+'╬' +'═'*9+'╣')
    print('\t\t\t║ {0:15s} ║ {1:7d} ║ {2:7d} ║'.format('Practice', p4, p5))
    print('\t\t\t╠'+'═'*17+ '╬' +'═'*9+'╬' +'═'*9+'╣')
    print('\t\t\t║ {0:15s} ║ {1:7d} ║ {2:7d} ║'.format('Classic', c4, c5))
    print('\t\t\t╠'+'═'*17+ '╬' +'═'*9+'╬' +'═'*9+'╣')
    print('\t\t\t║ {0:15s} ║ {1:7d} ║ {2:7d} ║'.format('X-Tile', x4, x5))
    print('\t\t\t╠'+'═'*17+ '╬' +'═'*9+'╬' +'═'*9+'╣')
    print('\t\t\t║ {0:15s} ║ {1:7d} ║ {2:7d} ║'.format('Survival', s4, s5))
    print('\t\t\t╚'+'═'*17+ '╩' +'═'*9+'╩' +'═'*9+'╝')
    print('\n\n\t\t\t    Press any key to return to menu')
    keypress()
    os.system('cls')


def howtoplay():
    os.system('cls')
    print('\n\n\n\n\n\n\t\t\t\t    HOW TO PLAY\n\n')
    print('\t\t\tUp Arrow Key\t: Slide Up')
    print('\t\t\tDown Arrow Key\t: Slide Down')
    print('\t\t\tLeft Arrow Key\t: Slide Left')
    print('\t\t\tRight Arrow Key\t: Slide Right')
    print('\t\t\tEscape Key\t: Return to Menu')
    print('\t\t\tBackspace Key\t: Undo Move (In Practice Mode)')
    print('\n\n\n\t\t\tPress any key to return to menu')
    keypress()
    os.system('cls')


def about():
    os.system('cls')
    print('\n\n\n\n\n\n\n')
    print('\t'*3 + '     ╔════════════════════╗     ')
    print('\t'*3 + '     ║  APP DEVELOPED BY  ║     ')
    print('\t'*3 + '     ║ ------------------ ║     ')
    print('\t'*3 + '     ║   Kushal Chauhan   ║     ')
    print('\t'*3 + '     ╚════════════════════╝     ')
    print('\n\n\n\n\n\n\t\t\tPress any key to return to menu')
    keypress()
    os.system('cls')
    
    
    
def quitgame():
    s1 = '''                        ╔══════════╗                      
                        ║   Yeah   ║              Nope    
                        ╚══════════╝                      '''

    s2 = '''                                              ╔══════════╗
                            Yeah              ║   Nope   ║
                                              ╚══════════╝'''
    select = [s1, s2]
    os.system('cls')
    print('\n\n\n\n\n\n')
    print('\t\t\t\t   Leave Game ?\n\n')
    i = 1
    print(select[i])
    nav = keypress()
    while nav != 'return' and nav != 'spacebar' :
        if nav == 'left' :
            i = 0
        elif nav == 'right' :
            i = 1
        else :
            nav = keypress()
            continue
        
        os.system('cls')
        print('\n\n\n\n\n\n')
        print('\t\t\t\t   Leave Game ?\n\n')
        print(select[i])
        nav = keypress()
    os.system('cls')
    if i == 0 :
        return True
    else :
        return False
    
    
def initialize(size, mode):
    if os.path.exists('_lib.pyd'):
        file = open('_lib.pyd', 'rb')
        data = load(file)
        file.close()
        if data['savegame'][size][mode][0] != []:
            tiles = data['savegame'][size][mode][0]
        else :
            if mode == 'xtile' :
                tiles = start_xtile(size)
            else :
                tiles = start_classic(size)
            data['savegame'][size][mode] = [tiles, 0]
        data['savegame']['psize'] = size
        data['savegame']['pmode'] = mode
    else :
        if mode == 'xtile' :
            tiles = start_xtile(size)
        else :
            tiles = start_classic(size)
        data = {'best' : \
                {'4x4' : {'classic' : 0, 'practice' : 0, 'xtile' : 0, 'survival' : 0},\
                 '5x5' : {'classic' : 0, 'practice' : 0, 'xtile' : 0, 'survival' : 0}},\
                'savegame' : {'psize' : size, 'pmode' : mode, \
                              '4x4' : {'classic' : [[], 0], 'practice' : [[], 0],\
                                       'xtile' : [[], 0], 'survival' : [[], 0]},\
                              '5x5' : {'classic' : [[], 0], 'practice' : [[], 0],\
                                       'xtile' : [[], 0], 'survival' : [[], 0]}}}
        data['savegame'][size][mode][0] = tiles
    file = open('_lib.pyd', 'wb')
    dump(data, file)
    file.close()
    return tiles


def start_classic(size):
    if size == '4x4':
        a = 4
    else :
        a = 5
    tiles = [['' for i in range(a)] for j in range(a)]
    i1, j1 = randint(0, a-1), randint(0, a-1)
    tiles[i1][j1] = 2
    i2, j2 = randint(0, a-1), randint(0, a-1)
    while i1 == i2 and j1 == j2 :
        i2, j2 = randint(0, a-1), randint(0, a-1)
    tiles[i2][j2] = 2
    return tiles


def start_xtile(size):
    if size == '4x4':
        a = 4
    else :
        a = 5
    tiles = [['' for i in range(a)] for j in range(a)]
    ix, jx = randint(0, a-1), randint(0, a-1)
    tiles[ix][jx] = '█'*(a+1)
    i1, j1 = randint(0, a-1), randint(0, a-1)
    while i1 == ix and j1 == jx :
        i1, j1 = randint(0, a-1), randint(0, a-1)
    tiles[i1][j1] = 2
    i2, j2 = randint(0, a-1), randint(0, a-1)
    while (i2 == ix and j2 == jx) or (i2 == i1 and j2 == j1) :
        i1, j1 = randint(0, a-1), randint(0, a-1)
    tiles[i2][j2] = 2
    return tiles

def gameplay(l, size, mode):
    global txt_game_over
    global txt_you_won
    global txt_you_lose
    global cd, hs, score, t
    pl = [list(row) for row in l]
    file = open('_lib.pyd', 'rb')
    data = load(file)
    hs = data['best'][size][mode]
    file.close()
    score = data['savegame'][size][mode][1]
    ps = score
    k = 1
    new_high_score = won = False
    os.system('cls')
    if mode == 'survival' :
        if 'time' in data :
            cd = data['time']
        else :
            cd = 15
            data['time'] = 15
            file = open('_lib.pyd', 'wb')
            dump(data, file)
            file.close()
        display(l, mode, True)
    else :
        display(l, mode)
    while True:
        swap = keypress()
        os.system('cls')
        if swap == 'up' :
            inc, won = up(l, won, mode)
            score += inc
        elif swap == 'left':
            inc, won = left(l, won, mode)
            score += inc
        elif swap == 'down':
            inc, won = down(l, won, mode)
            score += inc
        elif swap == 'right':
            inc, won = right(l, won, mode)
            score += inc
        elif swap == 'esc' :
            if mode == 'survival' :
                t.cancel()
            break
        elif swap == 'backspace' and mode == 'practice' :
            if len(data['moves']) != 0 :
                if len(data['moves'][0][0]) == int(size[0]):
                    k2 = k4 = 0
                    for row in l:
                        k2 += row.count(2)
                        k4 += row.count(4)
                    if not(k2 == 2 and k4 == 0) :
                        l, score = data['moves'].pop()
                        file = open('_lib.pyd', 'wb')
                        dump(data, file)
                        file.close()
                        pl = [list(row) for row in l]
                        ps = score
            os.system('cls')
            display(l, mode)
            continue
        else :
            os.system('cls')
            display(l, mode)
            continue

        data['savegame'][size][mode ][0]= l
        data['savegame'][size][mode][1] = score
        if mode == 'practice' and pl != l :
            if 'moves' not in data :
                data['moves'] = [[pl, ps]]
            else :
                if len(data['moves']) != 0 :
                    if len(data['moves'][0][0]) == int(size[0]):
                        data['moves'].append([pl, ps])
                    else :
                        data['moves'] = [[pl, ps]]
                else :
                    data['moves'].append([pl, ps])
            if len(data['moves']) > 20 :
                data['moves'].pop(0)
        if mode == 'survival' :
            data['time'] = cd
            os.system('cls')
            display(l, mode)
        file = open('_lib.pyd', 'wb')
        dump(data, file)
        file.close()
        pl = [list(row) for row in l]
        ps = score
        if hs < score :
            hs = score
            new_high_score = True
            data['best'][size][mode] = score
            file = open('_lib.pyd', 'wb')
            dump(data, file)
            file.close()
        if won and k == 1 :
            os.system('cls')
            for x in range(5, 0, -1):  
                print(txt_you_won)
                print('\n\n\n\t\t\t\tYOUR SCORE :', int(score))
                print('\n\t\t\t      GAME WILL CONTINUE IN\n')
                print('\t\t\t\t\t', x)
                time.sleep(1)
                os.system('cls')
                time.sleep(0.2)
            os.system('cls')
            display(l, mode)
            k = 2
        if game_over(l) or (mode == 'survival' and cd <=0) :
            data['savegame'][size][mode][0] = []
            data['savegame'][size][mode][1] = 0
            if mode == 'practice' :
                del data['moves']
            if mode == 'survival' :
                del data['time']
            file = open('_lib.pyd', 'wb')
            dump(data, file)
            file.close()
            if mode != 'survival' :
                os.system('cls')
                display(l, mode)
                keypress()
            if won :
                txt = txt_game_over
            else :
                txt = txt_you_lose
        
            if not new_high_score :
                os.system('cls')
                for x in range(3):
                    print(txt)
                    print('\n\n\n\t\t\t\tYOUR SCORE :', int(score))
                    time.sleep(1)
                    os.system('cls')
                    time.sleep(0.2)
            else :
                os.system('cls')
                for x in range(5):  
                    print(txt)
                    print('\n\n\n\t\t\t\tYOUR SCORE :', int(score))
                    print('\n\t\t\t\t  NEW HIGHSCORE')
                    time.sleep(1)
                    os.system('cls')
                    time.sleep(0.2)
            break
        

def display(tiles, mode, recurse = False):
    global cd, hs, score, t
    l = len(tiles)
    p = '''				  PRACTICE MODE
                     You have option to undo your last move.'''
    c = '''				  CLASSIC MODE
                      Join the numbers to get a 2048 tile!'''
    x = '''		   		   X-TILE MODE
                            X tile cannot be merged.'''
    s = '''				  SURVIVAL MODE
                   Tiles bigger than 8 give you additional time.'''
    modes = {'practice' : p, 'classic' : c, 'xtile' : x, 'survival' : s}
    os.system('cls')
    if l == 4 :
        print('\n')
        print(modes[mode])
        if mode == 'survival':
            if cd < 0 :
                c = 0
            else :
                c = cd
            print('\n')
            print('\t\t\t                           {0:02d}:{1:02d} '.\
                  format(c//60, c%60))
        else :
            print('\n\n\n')
        print('\t\t\t╔═══════╦═══════╦═══════╦═══════╗')
        for i in range (3):
            print('\t\t\t║ {0:5s} ║ {1:5s} ║ {2:5s} ║ {3:5s} ║'.\
                  format(str(tiles[i][0]).rjust(5), str(tiles[i][1]).rjust(5),\
                         str(tiles[i][2]).rjust(5), str(tiles[i][3]).rjust(5)))
            print('\t\t\t╠═══════╬═══════╬═══════╬═══════╣')
        print('\t\t\t║ {0:5s} ║ {1:5s} ║ {2:5s} ║ {3:5s} ║'.\
              format(str(tiles[3][0]).rjust(5), str(tiles[3][1]).rjust(5),\
                     str(tiles[3][2]).rjust(5), str(tiles[3][3]).rjust(5)))
        print('\t\t\t╚═══════╩═══════╩═══════╩═══════╝')
        print('\n'*5)
    else :
        print('\n')
        print(modes[mode])
        if mode == 'survival' :
            if cd < 0 :
                c = 0
            else :
                c = cd
            print('\n')
            print('\t\t                                        {0:02d}:{1:02d} '.\
                  format(c//60, c%60))
        else :
            print('\n\n\n')
        print('\t\t╔════════╦════════╦════════╦════════╦════════╗')
        for i in range (4):
            print('\t\t║ {0:6s} ║ {1:6s} ║ {2:6s} ║ {3:6s} ║ {4:6s} ║'.\
                  format(str(tiles[i][0]).rjust(6), str(tiles[i][1]).rjust(6), \
                         str(tiles[i][2]).rjust(6), str(tiles[i][3]).rjust(6),\
                         str(tiles[i][4]).rjust(6)))
            print('\t\t╠════════╬════════╬════════╬════════╬════════╣')
        print('\t\t║ {0:6s} ║ {1:6s} ║ {2:6s} ║ {3:6s} ║ {4:6s} ║'.\
              format(str(tiles[4][0]).rjust(6), str(tiles[4][1]).rjust(6), \
                     str(tiles[4][2]).rjust(6), str(tiles[4][3]).rjust(6),\
                     str(tiles[4][4]).rjust(6)))
        print('\t\t╚════════╩════════╩════════╩════════╩════════╝')
        print('\n'*3)
    print('    HIGHSCORE :',int(hs), '\t\t\t\t\t    YOUR SCORE :', int(score))
    if mode == 'survival' and recurse:
        cd -= 1
        t = Timer(1.0, lambda: display(tiles, mode, True))
        t.start()
        infile = open('_lib.pyd', 'rb')
        data = load(infile)
        infile.close()
        data['time'] = cd
        outfile = open('_lib.pyd', 'wb')
        dump(data, outfile)
        outfile.close()
        if cd < 0 :
            t.cancel()
            cd -= 17


        
def chance(l):
    size = len(l)
    i, j = randint(0, size-1), randint(0, size-1)
    while l[i][j] != '' :
        i, j = randint(0, size-1), randint(0, size-1)
    k = randint(0, 9)
    options = []
    for a in range(10):
        if a == k :
            options += [4]
        else :
            options += [2]
    l[i][j] = choice(options)



def keypress():
    keys = {18656 : 'up', 20704 : 'down', 19424 : 'left', 19936 : 'right',\
            13 : 'return', 27 : 'esc', 15104 : 'f1', 8 : 'backspace',\
            9 : 'tab' , 21472 : 'delete', 32 : 'spacebar', 16128 : 'f5'}
    while True:
        if msvcrt.kbhit():
            a = ord(msvcrt.getch())           
            if a == 0 or a == 224:          
               b = ord(msvcrt.getch())     
               x = a + (b*256)             
               key = x
               break
            else:
               key = a
               break
    if key in keys :
        return keys[key]
    

def up(tiles, won, mode):
    global cd
    inc = 0
    moved = False
    size = len(tiles)
    for k in range(size-1) :
        for i in range(size-1) :
            for j in range(size) :
                if tiles[i][j] == '' and tiles[i+1][j] != '' :
                    tiles[i][j], tiles[i+1][j] = tiles[i+1][j], tiles[i][j]
                    moved = True
                    
    for i in range(size-1):
        for j in range(size):
            if tiles[i][j] == tiles[i+1][j] :
                tiles[i][j] *= 2
                if tiles[i][j] == 2048 :
                    won = True
                if tiles[i][j] != '' :
                    if tiles[i][j] >= 16 and tiles[i][j] <=64\
                       and mode == 'survival':
                        cd += 2
                    inc += int(tiles[i][j])
                tiles[i+1][j] = ''
                if tiles[i][j] != tiles[i+1][j] :
                    moved = True
                
    for k in range(size-1) :
        for i in range(size-1) :
            for j in range(size) :
                if tiles[i][j] == '' :
                    tiles[i][j], tiles[i+1][j] = tiles[i+1][j], tiles[i][j]
    if moved :
        chance(tiles)
    display(tiles, mode)
    return inc, won



def down(tiles, won, mode):
    global cd
    inc = 0
    moved = False
    size = len(tiles)
    for k in range(size-1) :
        for i in range(1, size) :
            for j in range(size) :
                if tiles[i][j] == '' and tiles[i-1][j] != '' :
                    tiles[i][j], tiles[i-1][j] = tiles[i-1][j], tiles[i][j]
                    moved = True

    for i in range(size-1,0, -1):
        for j in range(size):
            if tiles[i][j] == tiles[i-1][j] :
                tiles[i][j] *= 2
                if tiles[i][j] == 2048 :
                    won = True
                if tiles[i][j] != '' :
                    if tiles[i][j] >= 16 and tiles[i][j] <=64\
                       and mode == 'survival':
                        cd += 2
                    inc += int(tiles[i][j])
                tiles[i-1][j] = ''
                if tiles[i][j] != tiles[i-1][j] :
                    moved = True
                
    for k in range(size-1) :
        for i in range(1, size) :
            for j in range(size) :
                if tiles[i][j] == '' :
                    tiles[i][j], tiles[i-1][j] = tiles[i-1][j], tiles[i][j]
    if moved :
        chance(tiles)
    display(tiles, mode)
    return inc, won



def left(tiles, won, mode):
    global cd
    inc = 0
    moved = False
    size = len(tiles)
    for k in range(size-1) :
        for i in range(size) :
            for j in range(size-1) :
                if tiles[i][j] == '' and tiles[i][j+1] != '' :
                    tiles[i][j], tiles[i][j+1] = tiles[i][j+1], tiles[i][j]
                    moved = True
    for i in range(size):
        for j in range(size-1):
            if tiles[i][j] == tiles[i][j+1] :
                tiles[i][j] *= 2
                if tiles[i][j] == 2048 :
                    won = True
                if tiles[i][j] != '' :
                    if tiles[i][j] >= 16 and tiles[i][j] <=64\
                       and mode == 'survival':
                        cd += 2
                    inc += int(tiles[i][j])
                tiles[i][j+1] = ''
                if tiles[i][j] != tiles[i][j+1]:
                    moved = True
                
    for k in range(size-1) :
        for i in range(size) :
            for j in range(size-1) :
                if tiles[i][j] == '' :
                    tiles[i][j], tiles[i][j+1] = tiles[i][j+1], tiles[i][j]
    if moved :
        chance(tiles)
    display(tiles, mode)
    return inc, won



def right(tiles, won, mode):
    global cd
    inc = 0
    moved = False
    size = len(tiles)
    for k in range(size-1) :
        for i in range(size) :
            for j in range(1, size) :
                if tiles[i][j] == '' and tiles[i][j-1] != '' :
                    tiles[i][j], tiles[i][j-1] = tiles[i][j-1], tiles[i][j]
                    moved = True
    for i in range(size):
        for j in range(size-1,0,-1):
            if tiles[i][j] == tiles[i][j-1] :
                tiles[i][j] *= 2
                if tiles[i][j] == 2048 :
                    won = True
                if tiles[i][j] != '' :
                    if tiles[i][j] >= 16 and tiles[i][j] <=64\
                       and mode == 'survival':
                        cd += 2
                    inc += int(tiles[i][j])
                tiles[i][j-1] = ''
                if tiles[i][j] != tiles[i][j-1] :
                    moved = True
                
    for k in range(size-1) :
        for i in range(size) :
            for j in range(1, size) :
                if tiles[i][j] == '' :
                    tiles[i][j], tiles[i][j-1] = tiles[i][j-1], tiles[i][j]
    if moved :
        chance(tiles)
    display(tiles, mode)
    return inc, won


    
def game_over(tiles):
    size = len(tiles)
    for i in range(size) :
        for j in range(size) :
            if tiles[i][j] == '' :
                return False
            
            elif i == 0 or j == 0 :
                if i == size-1 :
                    l = [tiles[i][j+1]]
                elif j == size-1 :
                    l = [tiles[i+1][j]]
                    
                else :    
                    l = [tiles[i][j+1], tiles[i+1][j]]
                    
                if i != 0 :
                    l += [tiles[i-1][j]]
                if j != 0 :
                    l += [tiles[i][j-1]]
                
            elif i == size-1 or j == size-1 :
                if i == 0 :
                    l = [tiles[i][j-1]]
                elif j == 0 :
                    l = [tiles[i-1][j]]
                else :
                    l = [tiles[i][j-1], tiles[i-1][j]]
                    
                if i != size-1 :
                    l += [tiles[i+1][j]]
                if j != size-1 :
                    l += [tiles[i][j+1]]
            else :
                l = [tiles[i][j+1], tiles[i+1][j], tiles[i-1][j], tiles[i][j-1]]
                
            if tiles[i][j] in l :
                return False
    return True

start()
while True :
    size, mode = menu()
    l = initialize(size, mode)
    gameplay(l, size, mode)

