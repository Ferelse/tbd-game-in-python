# Blackjack Game in Python

This repository originally contained a simple snake game. It has been
replaced with a command-line Blackjack implementation written in pure
Python.

## Playing

Run `python blackjack.py` for the original command-line version. It
prompts you to hit or stand until the dealer reaches a hand value of 17
or higher.

If you prefer a windowed interface, run `python blackjack_gui.py` to
play using a pygame-based UI with clickable **Hit** and **Stand** buttons.
The graphical version renders cards using images extracted from the
[ios-cards](https://github.com/finiteloop/ios-cards) project. **Binary
images are not included in this repository.** Download the PNG files
from that project and place them in `assets/cards` before running the
GUI.

### Card Images

Card images should be saved as `card_00.png` through `card_52.png` in
`assets/cards`. The order matches the original ios-cards collection:

1. Spades from **2** up to **A** (in that order)
2. Hearts from **2** up to **A**
3. Clubs from **2** up to **A**
4. Diamonds from **2** up to **A**
5. `card_52.png` is the back of a card used when the dealer's first
   card should remain hidden.
