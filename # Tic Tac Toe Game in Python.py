import tkinter as tk
from tkinter import messagebox

# Initialize the board with empty values
board = [' ' for _ in range(9)]
current_player = 'X'  # Player 1 is 'X', Player 2 is 'O'

# Function to handle the game reset and restart the game window
def play_again():
    root.destroy()  # Close the current window
    start_game()  # Start a new game window

# Function to handle each player's move
def player_move(index, button):
    global current_player
    
    if board[index] == ' ':
        board[index] = current_player
        # Update button text to show the player's symbol and change the color based on the player
        if current_player == 'X':
            button.config(text=current_player)
        else:
            button.config(text=current_player)

        # Disable the button after a move has been made
        button.config(state="disabled")
        
        # Check for a win or tie after the move
        if check_win(current_player):
            end_game_message(f"Player {current_player} wins! Play again?")
        elif check_tie():
            end_game_message("It's a tie! Play again?")
        else:
            # Switch to the next player
            current_player = 'O' if current_player == 'X' else 'X'
    else:
        messagebox.showwarning("Invalid Move", "This spot is already taken. Choose another.")

# Function to check if the current player has won
def check_win(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the game is a tie
def check_tie():
    return ' ' not in board

# Function to display the end game message and the option to play again
def end_game_message(message):
    # Ask the player if they want to play again using a custom message box with "Play Again"
    result = messagebox.askquestion("Game Over", message, icon='info', type="yesno", default="yes")
    if result == "yes":
        play_again()  # Restart the game if they choose to play again
    else:
        root.destroy()  # Close the game if they don't want to play again

# Function to update the board buttons based on the game state
def update_board():
    for i in range(9):
        buttons[i].config(text=board[i])

# Function to start the Tic Tac Toe game
def start_game():
    global root, buttons, board, current_player

    board = [' ' for _ in range(9)]  # Reset the board
    current_player = 'X'  # Reset to Player X's turn

    # Create the GUI window
    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.configure(bg='black')  # Set the background color to black

    # Create buttons for the Tic Tac Toe board with the specified color scheme
    buttons = []
    for i in range(9):
        button = tk.Button(root, text=' ', font=('normal', 20), width=5, height=2,
                           bg='black', fg='white',  # Background black, text color white
                           command=lambda i=i: player_move(i, buttons[i]))
        button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
        buttons.append(button)

    root.mainloop()

# Start the initial game
start_game()
