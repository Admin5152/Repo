#quiz 

print('Welcome')

playing = input ('Lets play a game? ')

if playing.lower() != 'yes': 
    quit()

print('alight lets begin :)')
score=0

answear = input('What does CPU stand for? ')
if answear == 'central processing unit':
    print('You got it!!, lets move on')
    score +=1
else:
    print('Incorrect >:(   i know where you live')



answear = input('How many planets are there? ')
if answear == '8':
    print('are u sure pluto isnt part!, lets move on')
    score +=1
else:
    print('WRONG >:(   are you trying to piss me off on purpose')


answear = input('whats the meaning of ACSII ')
if answear == 'american standard code for information interchange':
    print('wow!, lets move on')
    score +=1
else:
    print('WRONG AGAIN! >:(   STOP ACTING DAM')


answear = input('whats my fav color? ')
if answear == 'black':
    print('weird as stalker how tf did u know!, lets move on')
    score +=1
else:
    print('HERH HERH >:(   even a 9 year old could get that')


answear = input('have you eating? ')
if answear == 'maby':
    print('oh really !, lets move on cuz i aint buyinh u shishi')
    score +=1
else:
    print('HOW TF DID U GET THAT WORNG >:(   you must be retarded or something')


print('You got ' + str(score) + 'right')
print('You got ' + str((score/5) * 100 )+ 'right')

