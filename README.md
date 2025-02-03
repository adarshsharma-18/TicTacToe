# Tic-Tac-Toe Game

## Overview

This project is a Python implementation of the classic Tic-Tac-Toe game. It offers two main modes of play: single-player against the computer and multiplayer where two players can compete against each other. The game is designed with a simple text-based interface, making it easy to play directly in the terminal.

## Features

1. **Single-Player Mode**: Play against the computer. The computer uses a basic strategy to make its moves.
2. **Multiplayer Mode**: Play against a friend. Both players take turns to mark their positions on the board.
3. **Game Board Display**: The game board is displayed in a user-friendly format, with clear separators between cells.
4. **Win/Draw Detection**: The game automatically detects when a player has won or if the game ends in a draw.
5. **Input Validation**: Ensures that players enter valid positions and handles invalid inputs gracefully.
6. **History Tracking**: (Commented out in the code) The game can be extended to track game history, including player names, results, and timestamps.

## How to Play

### Single-Player Mode

1. **Start the Game**: Choose the single-player option from the main menu.
2. **Enter Your Name**: Input your name when prompted.
3. **Gameplay**:
   - The computer will make the first move as "X".
   - You will be prompted to enter your move as "O".
   - The game will alternate turns between you and the computer.
4. **Winning the Game**: The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game.
5. **Draw**: If all nine squares are filled without a winner, the game ends in a draw.

### Multiplayer Mode

1. **Start the Game**: Choose the multiplayer option from the main menu.
2. **Enter Player Names**: Input the names of both players.
3. **Gameplay**:
   - Player 1 will be "X" and Player 2 will be "O".
   - Players will take turns entering their moves.
4. **Winning the Game**: The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game.
5. **Draw**: If all nine squares are filled without a winner, the game ends in a draw.

## Code Structure

The code is structured into several functions to handle different aspects of the game:

- **`show_board(al)`**: Displays the current state of the game board.
- **`check_win(check_winner, winner)`**: Checks if a player has won the game.
- **`excuteinpx(ipx, c1mx, c2mx, al)`**: Executes the computer's move in single-player mode.
- **`excuteinpo(ipo, c1mo, c2mo, al)`**: Executes the player's move in single-player mode.
- **`savwhr(check_winner)`**: Determines the computer's move to block the player from winning.
- **`chksav(check_winner)`**: Checks if the player is about to win.
- **`finwhr(check_winner)`**: Determines the computer's move to win the game.
- **`chkfin(check_winner)`**: Checks if the computer is about to win.
- **`avmov(av, al)`**: Updates the list of available moves.
- **`DrawBoard()`**: Displays the game board in multiplayer mode.
- **`CheckPosition(x)`**: Checks if a position on the board is empty.
- **`CheckWin()`**: Checks if a player has won in multiplayer mode.

## Dependencies

The code uses the following Python libraries:

- **`time`**: Used to introduce delays in the game for a better user experience.
- **`os`**: (Commented out) Could be used to clear the terminal screen between moves.
- **`datetime`**: Used to timestamp the game results.

## Future Enhancements

1. **Database Integration**: The code includes commented-out sections for MySQL database integration to store game history. This can be uncommented and configured to track game results over time.
2. **Improved AI**: The computer's strategy can be enhanced with more advanced algorithms, such as the Minimax algorithm, to make it more challenging.
3. **GUI**: A graphical user interface (GUI) can be added using libraries like Tkinter or Pygame to make the game more visually appealing.
4. **Network Play**: Implement a multiplayer mode over a network, allowing players to compete remotely.

## Conclusion

This Tic-Tac-Toe game is a fun and simple project that demonstrates basic Python programming concepts, including functions, loops, conditionals, and list manipulation. It can be extended and improved in many ways, making it a great starting point for learning game development in Python.

## How to Run

1. Ensure you have Python installed on your system.
2. Copy the code into a Python file, e.g., `tic_tac_toe.py`.
3. Run the file using the command:
   ```bash
   python tic_tac_toe.py
   ```
4. Follow the on-screen instructions to play the game.

Enjoy playing Tic-Tac-Toe!
