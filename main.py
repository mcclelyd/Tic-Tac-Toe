S1 = 1 
S2 = 2 
S3 = 3 
S4 = 4 
S5 = 5 
S6 = 6 
S7 = 7 
S8 = 8 
S9 = 9
win = False

def board(S1,S2,S3,S4,S5,S6,S7,S8,S9):
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  
  print('_')
  print('|', S1, ' ', ' ',' ','|',S2,' ',' ',' ','|',S3,' ',' ',' ','|')
  print('|', ' ', ' ', ' ',' ','|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
  print('|', ' ', ' ', ' ',' ','|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
  
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-')
  
  
  print('|', S4, ' ', ' ',' ','|',S5,' ',' ',' ','|',S6,' ',' ',' ','|')
  print('|', ' ', ' ', ' ',' ','|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
  print('|', ' ', ' ', ' ',' ','|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
  
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-', end=' ')
  print('-')
  
  print('|', S7, ' ', ' ',' ','|',S8,' ',' ',' ','|',S9,' ',' ',' ','|')
  print('|', ' ', ' ', ' ',' ','|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
  print('|', ' ', ' ', ' ',' ','|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
  
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_', end= ' ')
  print('_')
# print numbers on empty spaces by inserting the number in the spaces when it prints the board?
print('Welcome to Tic Tac Toe!')
board(S1,S2,S3,S4,S5,S6,S7,S8,S9)
player1 = input('Place your X on a space on the board.')
player2 = input('Place your O on a space on the board.')

if player1 == '1':
  S1 = 'X'
elif player1 == '2':
  S2 = 'X'
elif player1 == '3':
  S3 = 'X'
elif player1 == '4':
  S4 = 'X'
elif player1 == '5':
  S5 = 'X'
elif player1 == '6':
  S6 = 'X'
elif player1 == '7':
  S7 = 'X'
elif player1 == '8':
  S8 = 'X'
elif player1 == '9':
  S9 = 'X'


if player2 == '1':
  S1 = 'O'
elif player2 == '2':
  S2 = 'O'
elif player2 == '3':
  S3 = 'O'
elif player2 == '4':
  S4 = 'O'
elif player2 == '5':
  S5 = 'O'
elif player2 == '6':
  S6 = 'O'
elif player2 == '7':
  S7 = 'O'
elif player2 == '8':
  S8 = 'O'
elif player2 == '9':
  S9 = 'O'
board(S1,S2,S3,S4,S5,S6,S7,S8,S9)
while True:
  player1 = input('Place your X on a space on the board.')
  if player1 == '1':
    S1 = 'X'
  elif player1 == '2':
    S2 = 'X'
  elif player1 == '3':
    S3 = 'X'
  elif player1 == '4':
    S4 = 'X'
  elif player1 == '5':
    S5 = 'X'
  elif player1 == '6':
    S6 = 'X'
  elif player1 == '7':
    S7 = 'X'
  elif player1 == '8':
    S8 = 'X'
  elif player1 == '9':
    S9 = 'X'
  if win == True:
    print(winner, 'wins!') 
  player2 = input('Place your O on a space on the board.')
  if player2 == '1':
    S1 = 'O'
  elif player2 == '2':
    S2 = 'O'
  elif player2 == '3':
    S3 = 'O'
  elif player2 == '4':
    S4 = 'O'
  elif player2 == '5':
    S5 = 'O'
  elif player2 == '6':
    S6 = 'O'
  elif player2 == '7':
    S7 = 'O'
  elif player2 == '8':
    S8 = 'O'
  elif player2 == '9':
    S9 = 'O'
  board(S1,S2,S3,S4,S5,S6,S7,S8,S9)
  if S1 == S5 and S5 == S9:
    win = True
    winner = S1
  if S1 == S4 and S4 == S7:
    win = True
    winner = S1
  if S1 == S2 and S2 == S3:
    win = True
    winner = S1
  if S2 == S5 and S5 == S8:
    win = True
    winner = S2
  if S3 == S6 and S6 == S9:
    win = True
    winner = S3
  if S3 == S5 and S5 == S7:
    win = True
    winner = S3
  if S4 == S5 and S5 == S6:
    win = True
    winner = S4
  if S7 == S8 and S8 == S9:
    win = True
    winner = S7
  if win == True:
    print(winner, 'wins!')
    over = input('Game over. Do you want to play again? Enter Yes or No.')
    if over == 'Yes':
      S1 = 1 
      S2 = 2 
      S3 = 3 
      S4 = 4 
      S5 = 5 
      S6 = 6 
      S7 = 7 
      S8 = 8 
      S9 = 9 
      board(S1,S2,S3,S4,S5,S6,S7,S8,S9)
    if over == 'No':
      break
    
# problem: no - repeats to "place x on a space on the board"