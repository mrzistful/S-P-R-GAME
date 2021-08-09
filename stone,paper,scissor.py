import random
player=input( "choose 'r'for rock, 'p' for paper,'s'for scissor\n")
opponent = random.choice(['r','p','s'])
print(opponent)

if player == opponent:
    print('tie')
elif(player=='r'and opponent=='s')or(player=='s'and opponent=='p')or(player=='p'and opponent=='s'):
    print('player win')
else:
    print('opponent win')

    
