# Tic-Tac-Toe
A simple implementation of the classic Tic-Tac-Toe game written in Python. This game allows two players to play against each other on a standard 3x3 grid using a numerical input system (0-8).

## Project Structure

The project consists of a single Python file containing the game logic, board rendering, and input loop.
* `project.py`: The source code

**Execution Order:**
1.  There are no external dependencies or multiple files to compile.
2.  Simply execute the single Python code to start the game.

## Prerequisites

* **Python 3.6+**: The code uses f-strings, which require Python 3.6 or newer.

## How to Play

**1. Game Start**
Upon running the script, the game will welcome you and ask for the names of the two players.

**2. The Board Layout**
The board is represented by a list of 9 numbers (0-8).
When asked to make a move, enter the number corresponding to the position on the board:
0 1 2 3 4 5 6 7 8

**3. Input and Output**
* **Input:** The game waits for an integer between 0 and 8.
* **Output:** After every move, the board repaints showing 'X' for Player 1 and 'O' for Player 2.

**4. Winning**
The game checks for a win after every move. A player wins if they occupy 3 consecutive spots in any of the following patterns:
* **Rows:** [0,1,2], [3,4,5], [6,7,8]
* **Columns:** [0,3,6], [1,4,7], [2,5,8]
* **Diagonals:** [0,4,8], [2,4,6]

## Note on Inputs

Please ensure you enter only integers between 0 and 8.
* Entering non-numeric characters (like 'a') may cause a crash.
* Entering numbers outside 0-8 is handled, but requires a restart of the input turn.

## How to Run

1.  **Clone or Download:** Download the project to your local machine.
2.  **Open Terminal:** Navigate to the project directory.
3.  **Execute:** Run the following command in your terminal/command prompt:

```bash
python project.py

Welcome to Tic-Tac-Toe!!
Enter the name of player 1 : Shreyam
Enter the name of player 2 : Rahul
0 | 1 | 2 
3 | 4 | 5 
6 | 7 | 8 
Current turn -> Shreyam
Please enter the index where you want to put your mark : 4
0 | 1 | 2 
3 | X | 5 
6 | 7 | 8
.... (final turn)
Current turn -> Rahul
Please enter the index where you want to put your mark : 2
X | 1 | X
3 | X | 5
O | O | O
Rahul won the match!
MATCH OVER!
