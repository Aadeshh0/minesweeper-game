## 🧨 CLI - Minesweeper Game
A simple command-line Minesweeper game where you can set a custom grid size and play by selecting coordinates.

---

### **🎮 How to Play**

Start the game by running:
```bash
python src/main.py
```

It will launch a terminal based game.

After that you will be prompted to input an integer value to create a grid.

```bash
Enter the values of widht: 
Enter the value of height: 
```

Example if you enter the grid size : (5,5)

Then : 

```css
[' ', ' ', ' ', ' ', ' ']
[' ', ' ', ' ', ' ', ' ']
[' ', ' ', ' ', ' ', ' ']
[' ', ' ', ' ', ' ', ' ']
[' ', ' ', ' ', ' ', ' ']
```

You'll be then asked to start guessing safe positions.
```bash 
Try to guess a non-mine. I'll ask your x and y coordinates. 0, 0  at my top left. 
Positives to right and down.

Enter zero-index x-coordinate between 0 and 4: 
Enter zero-index y-coordinate between 0 and 4: 
```

Now you can enter any value betwee 0 and 4 to guess the safe positions.

---

### **Game rules**

- Try to select a cell that doesn’t contain a mine.

- The board updates after each guess.

- The game ends when you either:

    - Step on a mine 💥

    - Or safely uncover all non-mine cells 🏆