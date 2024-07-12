#import os and random
import os
import random
#make function to clean consel
def clear_screen():
  os.system("clear"if os.name =="posix" else "cls")
#make class for take information from user
class player:
  #make inittilaize to attributes
  def __init__(self):
    self.name=""
    self.semple=""

  #make function to get name from the user
  def GetName(self):
    while True:
      name=input("Enter your name: ").strip().capitalize()
      if name.isalpha():
        self.name=name
        clear_screen()
        break
      else:
        clear_screen()
        print("You must write your name with letters")

  #make function to get semple
  def GetSemple(self):
    while True:
      semple=input("Enter your semple with one letter: ").strip().upper()
      if semple.isalpha()and len(semple)==1:
        clear_screen()
        self.semple=semple
        break
      else:
        clear_screen()
        print("You must write one capittal letter")
        
#make class to menue
class manue:
  #make function to the befining of the game
  def display_start_G(self):
    while True:
      choice=input("""
===========================
    WELCOME TO OUR GAME
         (X, O)
===========================
1. Start
2. Exit

Choose number: """).strip()
      if choice in ("1","2"):
        clear_screen()
        return choice
      else:
        clear_screen()
        print("Invaled input!!!")
  #make function to show the end of the Game
  def display_end_G(self):
    while True:
      choice=input("""
==========================
       GAME OVER
==========================

1. Restart.
2. Quit.

Choose number:  """).strip()
      if choice in ("1", "2"):
        clear_screen()
        return choice
      else:
        clear_screen()
        print("Invaled input!!!")

#make class for board
class board:
  #create list as attribute
  def __init__(self):
    self.board=[str(i)for i in range(1,10)]

  #make function to show board to user
  def showBoard(self):
    for i in range(0,len(self.board),3):
      print("|".join(self.board[i:i+3]))
      if i<6:
        print("-"*5)
  #make function takes symple and board to make changes
  def update_board(self, num, semple):
    if self.board[num-1].isdigit():
      self.board[num-1]=semple
      return True
    return False
  #restart board if the user wants play again
  def restart(self):
    self.board=[str(i)for i in range(1,10)]
  
#make class in charge to work whole the game
class Game:
  #make inittilize to classes 
  def __init__(self):
    self.palyer=[player(), player()]
    self.manue=manue()
    self.board=board()
    self.index_player_turn=0

  #make function to mange whole app
  def main(self):
    if self.manue.display_start_G()=="1":
      #make function to set up names and semples to players
      self.set_player(self.palyer)
      #make fuction to play game
      self.playGame()
    else:
      clear_screen()
      print("Quit...")
  def set_player(self, players):
    for i, pl in enumerate(players,1):
      clear_screen()
      print(f"Player {i}, fill info")
      pl.GetName()
      pl.GetSemple()
  def playGame(self):
    while True:
      self.board.showBoard()
      self.playerTurn()
      
      if  (self.check_win()or self.check_draw()):
        self.board.showBoard()
        
        
        if self.manue.display_end_G()=="1":
          self.board.restart()
          self.playGame()
        else:
          clear_screen()
          print("Quit...")
          quit()
  def playerTurn(self):
    
    curr_player=self.palyer[self.index_player_turn]
    if self.index_player_turn==0:
      while True:
        try:
          choice=int(input("Enter number in the range (1-9): ").strip())
        
          if 1<=choice<=9 and self.board.update_board(choice, curr_player.semple):
            clear_screen()
            break
          else:
          
            print("Invaled input!!!")
        except ValueError:
          print("Invaled input!!!")
    else:
      self.board.update_board(self.ribbortPlayer(self.board.board),curr_player.semple)
      clear_screen()
    self.ChangePlayer()    
  def ChangePlayer(self):
    self.index_player_turn=(self.index_player_turn+1)%2
  def check_win(self):
    options=[[0,1,2],[3,4,5],[6,7,8],
             [0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    for row in options:
      if self.board.board[row[0]]==self.board.board[row[1]]==self.board.board[row[2]]:
        self.result(self.board.board[row[0]])
        return True
    return False
  def result(self, semple):
    players=self.palyer
    for pl in players:
      if pl.semple==semple:
        print(f"🎊✨ {pl.name} wons, congragelation 🎊✨")
        break
  def check_draw(self):
    return all(not i.isdigit()for i in self.board.board)

  def ribbortPlayer(self, board):
    new_board=[i for i in board if i.isdigit()]
    return int(random.choice(new_board))
G=Game()
G.main()