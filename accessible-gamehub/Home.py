from Speech import get_speech

# Game Hub
game_case = ['battleship', 'whack a mole', 'tic-tac-toe']

while True:
    print("Welcome to game hub! Please choose which game you would like to play: Battleship, Wackamole, or Tic-Tac-Toe. (Speak the name of the game)")
    game = get_speech(game_case)
    if game != 'Error':
        break

if game == 'battleship':
    print("\nThis will run battleship")
    exec(open("Battleship.py").read())
elif game == 'whack a mole' or game == 'what':
    print("\nOpening Wackamole!")
    exec(open("WhackamoleSpeech.py").read())
else:
    print("\nOpening Tic-Tac-Toe")
    exec(open("TicTacToeSpeech.py").read())