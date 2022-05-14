# copyrifght of this code : eng abdirizak abdullahi hussein

# kinsi and dhaban and wah is a somali game basicly is a like a rock paper scissors

import random as rand

print('how to play it:')
print('theirs rules;  kinsi = 1 , dhaban = 2 , wah = 0')
print('if i ask you to  guess it you have to guess the option i told above')
print('\n')

length = int(input('how many rounds you playing you wanna to play it: '))
con = 0

points = 0
gusses = ['kinsi', 'dhaban', 'wah']
while con < length:
    sh = rand.choice(gusses)
    vb = 0
    # these if statement we gonna changing the options to enter the user
    if sh == gusses[0]:
        vb = 1
    elif sh == gusses[1]:
        vb = 2
    else:
        vb = vb

    guess = int(input('Gess it [kinsi = 1 , dhaban = 2 , wah = 0] : '))

    if guess == vb:
        print('you get it! congrast ')
        points += 1
    elif not guess:
        pass
    else:
        print('you lose!')
    con+=1
    print('\n')

print('GAME OVER! \n')
print('YOUR SCORES;')

print('Expect guesses:  {} \nYour guesses: {} \nYou lose: {} \n'.format(length,points,length-points))

print('AOUTHER OF THE GAME : Abdirizak Abdullahi hussein')