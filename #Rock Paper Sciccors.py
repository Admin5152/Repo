#Rock Paper Sciccors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

hands = [rock, paper, scissors]


User = int(input('Lets play a little game of Rock ,Paper , Scissors. \n'))
print(hands[User])

choices = random.randint(0, 2)
print(f'Computer chose: \n {hands[choices]}')


if User == 0 and choices == 0:
  print('Its a tie')
elif User == 0 and choices == 1:
  print('You lose')
elif User == 0 and choices == 2:
  print('You win')
elif User == 1 and choices == 0:
  print('You win')
elif User == 1 and choices == 1:
  print('Its a tie')
elif User == 1 and choices == 2:
  print('You lose')
elif User ==2 and choices == 0:
  print('You lose')
elif User == 2 and choices == 1:
  print('You win')
elif User == 2 and choices == 2:
  print('Its a tie')
else:
  print('Game Over')