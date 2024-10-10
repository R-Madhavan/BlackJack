![image](https://github.com/user-attachments/assets/f84ed937-eccb-4290-a6e5-fb94dd568918)

# BlackJack Game 🎮🃏

This is a simple terminal-based implementation of the classic card game **BlackJack**. The game allows a user to play against a computer, aiming to get as close to 21 without going over.

## How to Play 📝

1. The game will ask if you'd like to play a round of BlackJack. Type `'y'` to start or `'n'` to exit.
2. Both you and the computer will be dealt two cards.
3. You can choose to draw another card by typing `'y'` or pass by typing `'n'`.
4. The objective is to have a hand value closer to 21 than the computer without exceeding 21.
5. The game will display the results and declare a winner based on the scores.

## Rules 📜

- Face cards (King, Queen, Jack) are worth 10 points.
- The Ace (11) can count as 1 or 11, but in this version, it counts as 11.
- The player can keep drawing cards until they decide to stop or they exceed a total of 21, which results in a loss.
- The computer has a random chance of drawing another card.
  
## Features ⚙️

- User and computer hands displayed after each round.
- Random card dealing to both the user and computer.
- Determines win/loss/draw based on BlackJack rules.

## How to Run 🏃‍♂️

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/blackjack-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd blackjack-game
   ```
3. Run the game:
   ```bash
   python blackjack.py
   ```

## Example 🖼️

```
Your cards: [10, 7], current score: 17
Computer's first card: 8
Type 'y' to get another card, type 'n' to pass: y
Your cards: [10, 7, 2], current score: 19
Computer's first card: 8
You Won 🎉
```
