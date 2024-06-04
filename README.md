# BINGO Game

This is a simple implementation of the BINGO game using Python's Tkinter library for the graphical user interface. The game generates a 5x5 grid of buttons, each displaying a random number. When a button is clicked, it changes color to indicate it's been selected. The objective is to get 5 rows, columns, or diagonals with selected numbers to win the game.

## Features

1. **Random Number Generation**: The game generates a random number for each button in the 5x5 grid.
2. **Interactive Buttons**: Clicking a button marks it as selected and disables it.
3. **Winning Condition Check**: The game checks for a win condition after each click. A player wins by completing 5 rows, columns, or diagonals.
4. **Winning Message**: Displays a congratulatory message when the player wins.

## How to Play

1. **Start the Game**: Run the Python script. A 5x5 grid of buttons will appear, each with a random number.
2. **Select Numbers**: Click on the buttons to select the numbers. The button will change color and get disabled once clicked.
3. **Check for Win**: The game will automatically check if you have completed 5 rows, columns, or diagonals after each click.
4. **Win Message**: If you win, a congratulatory message will appear.

## Code Explanation

### Variables

- `numbers_str`: 5x5 list of strings representing numbers.
- `buttons`: 5x5 list to hold button references.
- `numbers`: 5x5 list to hold integer values of numbers.
- `BINGO`: Counter to keep track of completed rows, columns, and diagonals.

### Functions

#### `convert_to_int(_2dlist)`
Converts a 2D list of strings to a 2D list of integers.

#### `rand()`
Generates a random number from the remaining unselected numbers and marks it as selected.

#### `checkWin(row, col)`
Checks if the selected button completes a row, column, or diagonal and updates the `BINGO` counter.

#### `button_click(row, col)`
Handles the button click event. Marks the button as selected, disables it, and checks for a win condition.

### GUI Setup

- `main`: Main Tkinter window.
- `win_label`: Label to display the winning message.
- Grid of buttons is created with a random number assigned to each.

### Game Loop

- The Tkinter `mainloop` runs the game, waiting for button click events.

## Requirements

- Python 3.x
- Tkinter library (usually included with Python)

## Running the Game

1. Ensure you have Python installed on your machine.
2. Save the code to a file, e.g., `bingo_game.py`.
3. Run the script using `python bingo_game.py`.

## Author

- Developed by: PavanTeja-777

## License

- This game is for educational and entertainment purposes. Feel free to modify and enhance it.

Enjoy playing the BINGO game! If you have any questions or feedback, feel free to reach out.
