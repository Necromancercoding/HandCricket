#revised handcricket
from random import randint
import random
import time
import sys
a=0
b=0
c=0
d=0
toss=['heads','tails']
inning=['bat','bowl']
playershots1=[0,1,2,3,4,5,6,7,8,9,10]
playershots2=[0,1,2,3,4,5,6]
print('Welcome to Handcricket!')
print('(1) To play, you will enter various numbers between 0 to 10 when you are bowling or batting')
print('(2) The computer will also play a certain number, if the numbers match, the batsman will get out')
print('(3) In the initial level, you can throw a number between 0 to 10')
print('(4) In the second level, you can throw a number between 0 and 6')
print('(5) At any point of the game if you feel like quitting, you can do so by pressing ctrl+c')
print('(6) You have been given an option if you would like to proceed to level 2 after winning level 1')
print('(7) You will only reach level 2 if you win level 1')
print('(8) To win any level, you have to beat the computer fair and square, evn a draw means a loss for you')
print('')
print('')
player_name=input('Enter your name: ')
print('')
print('')
print('')
print('')
print('')
print('')
print(' -----------------------------------------------Level 1----------------------------------------------- ')
print('')
print('')
print('')
print('')
print('')
print('')
call=input('enter your call for the toss, for calling out heads, type heads, for calling out tails, type tails: ')
while call not in toss:
    call=input('Read carefully, for calling out heads, type heads, for calling out tails, type tails: ')
d=random.choice(toss)
if call==d:
    print('You have  the toss')
    decision=input('What would you like to do first? Batting or bowling? For batting, type bat, for bowling, type bowl')
    while decision not in inning:
        decision=input('Read carefully, for batting, type bat, for bowling, type bowl')
    if decision=='bat':
        print('Your team is about to start batting')
        print('The First innings is about to start, get ready for the field, boys....')
        print('You have 5 seconds to start')
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        while 2==2:
            playermove=int(input('Enter your chosen shot'))
            while playermove not in playershots1:
                playermove=int(input('Enter your chosen shot between 0 and 10'))
            print('The ball will reach the batsman in 3 seconds')
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
                print('')
            cmove=random.choice(playershots1)
            print('the computer played a ',cmove)
            if playermove!=cmove:
                a+=playermove
                if playermove>=6:
                    print('What a magnificent shot')
                    print('Your current total is ',a,' runs')
                elif playermove<6 and playermove!=0:
                    print('Thats a thoughtful shot')
                    print('Your current total is ',a,' runs')
                elif playermove==0:
                    print('Oops, thats a dot ball, make sure you hit the ball next time')
                    print('Your current total is ',a,' runs')
            elif playermove==cmove:
                print('Oops, your batsman got out at ',a,' runs')
                break
        print('Your batsman made ',a,' runs in the first innings')
        print('Get ready to defend your target now')
        print('You have 5 seconds to start')
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        while 2==2:
            if b>a:
                print('You have lost to the computer, try again next time.')
                sys.exit()
            playermove=int(input('Enter your chosen ball'))
            while playermove not in playershots1:
                playermove=int(input('Enter your chosen ball between 0 and 10'))
            print('The ball will reach the batsman in 3 seconds')
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
                print('')
            cmove=random.choice(playershots1)
            print('The computer played a ',cmove)
            if playermove!=cmove:
                b+=cmove
                if cmove>=6:
                    print('Thats a poor ball')
                    print('The computers current total is ',b,' runs')
                elif cmove<6 and cmove!=0:
                    print('Thats a thoughtful ball')
                    print('The computers current total is ',b,' runs')
                elif cmove==0:
                    print('Yes, thats a dot ball, make sure you bowl more of these')
                    print('The computers current total is  ',b,' runs')
            elif playermove==cmove:
                print('Yes, you bowled out the computer at ',b,' runs')
                print('You have defeated the computer by ',a-b,' runs')
                print('Now you shall ascend to the next level')
                break
                    
    elif decision=='bowl':
        print('Your team is about to start bowling')
        print('The First innings is about to start, get ready for the field, boys....')
        print('You have 5 seconds to start')
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        while 2==2:
            playermove=int(input('Enter your chosen ball'))
            while playermove not in playershots1:
                playermove=int(input('Enter your chosen ball between 0 and 10'))
            print('The ball will reach the batsman in 3 seconds')
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
                print('')
            cmove=random.choice(playershots1)
            print('the computer played a ',cmove)
            if playermove!=cmove:
                b+=cmove
                if cmove>=6:
                    print('Thats a poor ball')
                    print('The computers current total is ',b,' runs')
                elif cmove<6 and cmove!=0:
                    print('Thats a thoughtful ball')
                    print('The computers current total is ',b,' runs')
                elif cmove==0:
                    print('Yes, thats a dot ball, make sure you bowl more of these')
                    print('The computers current total is  ',b,' runs')
            elif playermove==cmove:
                print('Yes, you bowled out the computer at ',b,' runs')
                break
        print('The computer made ',b,' runs in the first innings')
        print('Get ready to chase this target of ',b+1,' now')
        print('You have 5 seconds to start')
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        while 2==2:
            if a>b:
                print('You have succesfully chased the target')
                print('You will now ascend to the next level')
                break
            playermove=int(input('Enter your chosen shot'))
            while playermove not in playershots1:
                playermove=int(input('Enter your chosen shot between 0 and 10'))
            print('The ball will reach the batsman in 3 seconds')
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
                print('')
            cmove=random.choice(playershots1)
            print('the computer played a ',cmove)
            if playermove!=cmove:
                a+=playermove
                if playermove>=6:
                    print('What a magnificent shot')
                    print('Your current total is ',a,' runs')
                elif playermove<6 and playermove!=0:
                    print('Thats a thoughtful shot')
                    print('Your current total is ',a,' runs')
                elif playermove==0:
                    print('Oops, thats a dot ball, make sure you hit the ball next time')
                    print('Your current total is ',a,' runs')
            elif playermove==cmove:
                print('Oops, your batsman got out at ',a,' runs')
                print('Better luck next time!')
                sys.exit()
                        
elif call!=d:
    print('You have lost the toss')
    computer=random.choice(inning)
    print('the computer has chosen to ',computer,' first')
    if computer=='bat':
        print('Your team is about to start bowling')
        print('The First innings is about to start, get ready for the field, boys....')
        print('You have 5 seconds to start')
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        while 2==2:
            playermove=int(input('Enter your chosen ball'))
            while playermove not in playershots1:
                playermove=int(input('Enter your chosen ball between 0 and 10'))
            print('The ball will reach the batsman in 3 seconds')
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
                print('')
            cmove=random.choice(playershots1)
            print('the computer played a ',cmove)
            if playermove!=cmove:
                b+=cmove
                if cmove>=6:
                    print('Thats a poor ball')
                    print('The computers current total is ',b,' runs')
                elif cmove<6 and cmove!=0:
                    print('Thats a thoughtful ball')
                    print('The computers current total is ',b,' runs')
                elif cmove==0:
                    print('Yes, thats a dot ball, make sure you bowl more of these')
                    print('The computers current total is  ',b,' runs')
            elif playermove==cmove:
                print('Yes, you bowled out the computer at ',b,' runs')
                break
        print('The computer made ',b,' runs in the first innings')
        print('Get ready to chase this target of ',b+1,' now')
        print('You have 5 seconds to start')
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        while 2==2:
            if a>b:
                print('You have succesfully chased the target')
                print('You will now ascend to the next level')
                break
            playermove=int(input('Enter your chosen shot'))
            while playermove not in playershots1:
                playermove=int(input('Enter your chosen shot between 0 and 10'))
            print('The ball will reach the batsman in 3 seconds')
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
                print('')
            cmove=random.choice(playershots1)
            print('the computer played a ',cmove)
            if playermove!=cmove:
                a+=playermove
                if playermove>=6:
                    print('What a magnificent shot')
                    print('Your current total is ',a,' runs')
                elif playermove<6 and playermove!=0:
                    print('Thats a thoughtful shot')
                    print('Your current total is ',a,' runs')
                elif playermove==0:
                    print('Oops, thats a dot ball, make sure you hit the ball next time')
                    print('Your current total is ',a,' runs')
            elif playermove==cmove:
                print('Oops, your batsman got out at ',a,' runs')
                print('Better luck next time!')
                sys.exit()
    elif computer=='bowl':
        print('Your team is about to start batting')
        print('The First innings is about to start, get ready for the field, boys....')
        print('You have 5 seconds to start')
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        while 2==2:
            playermove=int(input('Enter your chosen shot'))
            while playermove not in playershots1:
                playermove=int(input('Enter your chosen shot between 0 and 10'))
            print('The ball will reach the batsman in 3 seconds')
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
                print('')
            cmove=random.choice(playershots1)
            print('the computer played a ',cmove)
            if playermove!=cmove:
                a+=playermove
                if playermove>=6:
                    print('What a magnificent shot')
                    print('Your current total is ',a,' runs')
                elif playermove<6 and playermove!=0:
                    print('Thats a thoughtful shot')
                    print('Your current total is ',a,' runs')
                elif playermove==0:
                    print('Oops, thats a dot ball, make sure you hit the ball next time')
                    print('Your current total is ',a,' runs')
            elif playermove==cmove:
                print('Oops, your batsman got out at ',a,' runs')
                break
        print('Your batsman made ',a,' runs in the first innings')
        print('Get ready to defend your target now')
        print('You have 5 seconds to start')
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        while 2==2:
            if b>a:
                print('You have lost to the computer, try again next time.')
                sys.exit()
            playermove=int(input('Enter your chosen ball'))
            while playermove not in playershots1:
                playermove=int(input('Enter your chosen ball between 0 and 10'))
            print('The ball will reach the batsman in 3 seconds')
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
                print('')
            cmove=random.choice(playershots1)
            print('The computer played a ',cmove)
            if playermove!=cmove:
                b+=cmove
                if cmove>=6:
                    print('Thats a poor ball')
                    print('The computers current total is ',b,' runs')
                elif cmove<6 and cmove!=0:
                    print('Thats a thoughtful ball')
                    print('The computers current total is ',b,' runs')
                elif cmove==0:
                    print('Yes, thats a dot ball, make sure you bowl more of these')
                    print('The computers current total is  ',b,' runs')
            elif playermove==cmove:
                print('Yes, you bowled out the computer at ',b,' runs')
                print('You have defeated the computer by ',a-b,' runs')
                print('Now you shall ascend to the next level')
                break
print('You have 10 seconds to start the next level')
for i in range(10,0,-1):
    time.sleep(1)
    print(i)
    print('')
print('')
print('')
print('')
print('')
print('')
print('')
quitchoice=input('Do you want to proceed to the next level? If yes type yes, if no type no')
if quitchoice='no':
    sys.exit()
#Level 2
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print(' -----------------------------------------------Level 2----------------------------------------------- ')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('Welcome to level 2 of handcricket')
print('The instructions are the same except that now you have a narrower choice of shots which makes games shorter and harder')
print('Enter numbers between 0 and 6')
print('')
print('')
print('')
print('')
print('')
print('')
call=input('enter your call for the toss, for calling out heads, type heads, for calling out tails, type tails: ')
while call not in toss:
    call=input('Read carefully, for calling out heads, type heads, for calling out tails, type tails: ')
d=random.choice(toss)
if call==d:
    print('You have  the toss')
    decision=input('What would you like to do first? Batting or bowling? For batting, type bat, for bowling, type bowl')
    while decision not in inning:
        decision=input('Read carefully, for batting, type bat, for bowling, type bowl')
    if decision=='bat':
        print('Your team is about to start batting')
        print('The First innings is about to start, get ready for the field, boys....')
        print('You have 5 seconds to start')
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        while 2==2:
            playermove=int(input('Enter your chosen shot'))
            while playermove not in playershots2:
                playermove=int(input('Enter your chosen shot between 0 and 6'))
            print('The ball will reach the batsman in 3 seconds')
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
                print('')
            cmove=random.choice(playershots2)
            print('the computer played a ',cmove)
            if playermove!=cmove:
                c+=playermove
                if playermove>=4:
                    print('What a magnificent shot')
                    print('Your current total is ',c,' runs')
                elif playermove<4 and playermove!=0:
                    print('Thats a thoughtful shot')
                    print('Your current total is ',c,' runs')
                elif playermove==0:
                    print('Oops, thats a dot ball, make sure you hit the ball next time')
                    print('Your current total is ',c,' runs')
            elif playermove==cmove:
                print('Oops, your batsman got out at ',c,' runs')
                break
        print('Your batsman made ',c,' runs in the first innings')
        print('Get ready to defend your target now')
        print('You have 5 seconds to start')
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        while 2==2:
            if d>c:
                print('You have lost to the computer, try again next time.')
                sys.exit()
            playermove=int(input('Enter your chosen ball'))
            while playermove not in playershots2:
                playermove=int(input('Enter your chosen ball between 0 and 6'))
            print('The ball will reach the batsman in 3 seconds')
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
                print('')
            cmove=random.choice(playershots2)
            print('The computer played a ',cmove)
            if playermove!=cmove:
                d+=cmove
                if cmove>=4:
                    print('Thats a poor ball')
                    print('The computers current total is ',d,' runs')
                elif cmove<4 and cmove!=0:
                    print('Thats a thoughtful ball')
                    print('The computers current total is ',d,' runs')
                elif cmove==0:
                    print('Yes, thats a dot ball, make sure you bowl more of these')
                    print('The computers current total is  ',d,' runs')
            elif playermove==cmove:
                print('Yes, you bowled out the computer at ',d,' runs')
                print('You have defeated the computer by ',c-d,' runs')
                print(player_name,'You have won the title, may you have a great day ahead!')
                sys.exit()
                    
    elif decision=='bowl':
        print('Your team is about to start bowling')
        print('The First innings is about to start, get ready for the field, boys....')
        print('You have 5 seconds to start')
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        while 2==2:
            playermove=int(input('Enter your chosen ball'))
            while playermove not in playershots2:
                playermove=int(input('Enter your chosen ball between 0 and 6'))
            print('The ball will reach the batsman in 3 seconds')
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
                print('')
            cmove=random.choice(playershots2)
            print('the computer played a ',cmove)
            if playermove!=cmove:
                d+=cmove
                if cmove>=4:
                    print('Thats a poor ball')
                    print('The computers current total is ',d,' runs')
                elif cmove<4 and cmove!=0:
                    print('Thats a thoughtful ball')
                    print('The computers current total is ',d,' runs')
                elif cmove==0:
                    print('Yes, thats a dot ball, make sure you bowl more of these')
                    print('The computers current total is  ',d,' runs')
            elif playermove==cmove:
                print('Yes, you bowled out the computer at ',d,' runs')
                break
        print('The computer made ',d,' runs in the first innings')
        print('Get ready to chase this target of ',d+1,' now')
        print('You have 5 seconds to start')
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        while 2==2:
            if c>d:
                print('You have succesfully chased the target')
                print(player_name,'You have won the title, may you have a great day ahead!')
                sys.exit()
            playermove=int(input('Enter your chosen shot'))
            while playermove not in playershots2:
                playermove=int(input('Enter your chosen shot between 0 and 6'))
            print('The ball will reach the batsman in 3 seconds')
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
                print('')
            cmove=random.choice(playershots2)
            print('the computer played a ',cmove)
            if playermove!=cmove:
                c+=playermove
                if playermove>=4:
                    print('What a magnificent shot')
                    print('Your current total is ',c,' runs')
                elif playermove<4 and playermove!=0:
                    print('Thats a thoughtful shot')
                    print('Your current total is ',c,' runs')
                elif playermove==0:
                    print('Oops, thats a dot ball, make sure you hit the ball next time')
                    print('Your current total is ',c,' runs')
            elif playermove==cmove:
                print('Oops, your batsman got out at ',c,' runs')
                print('Better luck next time!')
                sys.exit()
                        
elif call!=d:
    print('You have lost the toss')
    computer=random.choice(inning)
    print('the computer has chosen to ',computer,' first')
    if computer=='bat':
        print('Your team is about to start bowling')
        print('The First innings is about to start, get ready for the field, boys....')
        print('You have 5 seconds to start')
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        while 2==2:
            playermove=int(input('Enter your chosen ball'))
            while playermove not in playershots2:
                playermove=int(input('Enter your chosen ball between 0 and 6'))
            print('The ball will reach the batsman in 3 seconds')
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
                print('')
            cmove=random.choice(playershots2)
            print('the computer played a ',cmove)
            if playermove!=cmove:
                d+=cmove
                if cmove>=4:
                    print('Thats a poor ball')
                    print('The computers current total is ',d,' runs')
                elif cmove<4 and cmove!=0:
                    print('Thats a thoughtful ball')
                    print('The computers current total is ',d,' runs')
                elif cmove==0:
                    print('Yes, thats a dot ball, make sure you bowl more of these')
                    print('The computers current total is  ',d,' runs')
            elif playermove==cmove:
                print('Yes, you bowled out the computer at ',d,' runs')
                break
        print('The computer made ',d,' runs in the first innings')
        print('Get ready to chase this target of ',d+1,' now')
        print('You have 5 seconds to start')
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        while 2==2:
            if c>d:
                print('You have succesfully chased the target')
                print(player_name,'You have won the title, may you have a great day ahead!')
                sys.exit
            playermove=int(input('Enter your chosen shot'))
            while playermove not in playershots2:
                playermove=int(input('Enter your chosen shot between 0 and 6'))
            print('The ball will reach the batsman in 3 seconds')
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
                print('')
            cmove=random.choice(playershots2)
            print('the computer played a ',cmove)
            if playermove!=cmove:
                c+=playermove
                if playermove>=4:
                    print('What a magnificent shot')
                    print('Your current total is ',c,' runs')
                elif playermove<4 and playermove!=0:
                    print('Thats a thoughtful shot')
                    print('Your current total is ',c,' runs')
                elif playermove==0:
                    print('Oops, thats a dot ball, make sure you hit the ball next time')
                    print('Your current total is ',c,' runs')
            elif playermove==cmove:
                print('Oops, your batsman got out at ',c,' runs')
                print('Better luck next time!')
                sys.exit()
    elif computer=='bowl':
        print('Your team is about to start batting')
        print('The First innings is about to start, get ready for the field, boys....')
        print('You have 5 seconds to start')
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        while 2==2:
            playermove=int(input('Enter your chosen shot'))
            while playermove not in playershots2:
                playermove=int(input('Enter your chosen shot between 0 and 6'))
            print('The ball will reach the batsman in 3 seconds')
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
                print('')
            cmove=random.choice(playershots2)
            print('the computer played a ',cmove)
            if playermove!=cmove:
                c+=playermove
                if playermove>=4:
                    print('What a magnificent shot')
                    print('Your current total is ',c,' runs')
                elif playermove<4 and playermove!=0:
                    print('Thats a thoughtful shot')
                    print('Your current total is ',c,' runs')
                elif playermove==0:
                    print('Oops, thats a dot ball, make sure you hit the ball next time')
                    print('Your current total is ',c,' runs')
            elif playermove==cmove:
                print('Oops, your batsman got out at ',c,' runs')
                break
        print('Your batsman made ',c,' runs in the first innings')
        print('Get ready to defend your target now')
        print('You have 5 seconds to start')
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        while 2==2:
            if d>c:
                print('You have lost to the computer, try again next time.')
                sys.exit()
            playermove=int(input('Enter your chosen ball'))
            while playermove not in playershots2:
                playermove=int(input('Enter your chosen ball between 0 and 6'))
            print('The ball will reach the batsman in 3 seconds')
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
                print('')
            cmove=random.choice(playershots2)
            print('The computer played a ',cmove)
            if playermove!=cmove:
                d+=cmove
                if cmove>=4:
                    print('Thats a poor ball')
                    print('The computers current total is ',d,' runs')
                elif cmove<4 and cmove!=0:
                    print('Thats a thoughtful ball')
                    print('The computers current total is ',d,' runs')
                elif cmove==0:
                    print('Yes, thats a dot ball, make sure you bowl more of these')
                    print('The computers current total is  ',d,' runs')
            elif playermove==cmove:
                print('Yes, you bowled out the computer at ',d,' runs')
                c=2
                print('You have defeated the computer by ',c-d,' runs')
                print(player_name,'You have won the title, may you have a great day ahead!')
                sys.exit()

    
