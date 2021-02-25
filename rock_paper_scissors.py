import random

values = {
'rock': 0,
'paper': 1,
'scissors': 2,
}

def make_choice():
  i = int(random.random()*3)
  if i == 0:
    return 'rock'
  elif i == 1:
    return 'paper'
  else:
    return 'scissors'

def do_i_win(me, player):
  me_value = values[me]
  player_value = values[player]
  if me_value == player_value:
    return 0

  diff = player_value - me_value
  if diff == 1 or diff == -2:
    return 1

  return -1

def play():
  while(True):
    choice = make_choice()
    s = input('Rock / Paper / Scissors? ').lower()
    if (s != 'rock' and s != 'paper' and s != 'scissors'):
      print('I do not understand your input. Do you know how to play the game at all?')
      continue

    print ('I have {}. '.format(choice), end='')

    win = do_i_win(choice, s)
    if win == 0:
      print('Tied, let\'s try again')
      continue

    print ('You {}!'.format((win > 0) and 'win' or 'lose'))
    return

if __name__ == '__main__':
  play()