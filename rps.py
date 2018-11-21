from pyfiglet import Figlet

custom_fig = Figlet(font = "graffiti")
print(custom_fig.renderText("Hello!!"))

print("Welcome to our 2 player rock, paper, scissors terminal game. This game has three rounds, have fun!")
player1 = input("Enter player1 name: ")
player2 = input("Enter player2 name: ")

print("Are you ready?")
rounds = 0
player1_total = 0
player2_total = 0

while rounds < 4:
 player1_round = input(player1 + " Enter rock, paper or scissors: ")
 player2_round = input(player2 + " Enter rock, paper or scissors: ")
 if player1_round == "scissors" and player2_round == "paper":
  player1_total += 1
  rounds += 1
  print(player1 + " wins this round")
 elif player1_round == "paper" and player2_round == "rock":
  player1_total += 1
  rounds += 1 
  print(player1 + " wins this round")
 elif player1_round == "rock" and player2_round == "scissors":
  player1_total += 1
  rounds += 1
  print(player1 + " wins this round")

 if player2_round == "scissors" and player1_round == "paper":
  player2_total += 1
  rounds += 1
  print(player2 + " wins this round")
 elif player2_round == "paper" and player1_round == "rock":
  player2_total += 1
  rounds += 1 
  print(player2 + " wins this round")
 elif player2_round == "rock" and player1_round == "scissors":
  player2_total += 1
  rounds += 1
  print(player2 + " wins this round")

 if player1_round == player2_round:
  print("This round was a draw")
  rounds += 1
 
 
 if rounds == 3:
  if player1_total > player2_total:
   newfig = Figlet(font = "small")
   print(newfig.renderText(player1 + " Wins"))
  elif player2_total > player1_total:
   newfig = Figlet(font = "small")
   print(newfig.renderText(player2 + " Wins"))
  break; 
 

