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
`assets/cards`. The numbering follows the ios-cards project exactly:

1. `card_00.png`–`card_12.png` are the Spades, starting at the **2** and
   ending with the **A** (Ace).
2. `card_13.png`–`card_25.png` are the Hearts from **2** through **A**.
3. `card_26.png`–`card_38.png` are the Clubs from **2** through **A**.
4. `card_39.png`–`card_51.png` are the Diamonds from **2** through
   **A**.
5. `card_52.png` represents the back of a card used when the dealer's
   first card should remain hidden.
