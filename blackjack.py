#!/usr/bin/env python3
"""Simple command-line Blackjack game.

The game deals from a standard 52-card deck. The player may hit or stand.
Dealer draws until the hand value is at least 17. Aces count as 1 or 11.
"""

import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11,
}

class Deck:
    """Represents a shuffled deck of playing cards."""

    def __init__(self):
        self.cards = [(rank, suit) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def deal(self):
        """Deal a single card from the deck."""
        return self.cards.pop()

def hand_value(hand):
    """Return the best score for the given hand."""
    total = sum(VALUES[rank] for rank, _ in hand)
    aces = sum(1 for rank, _ in hand if rank == 'A')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def format_hand(hand, hide_first=False):
    """Return a string representation of a hand."""
    if hide_first:
        return '[hidden], ' + ', '.join(f'{r} of {s}' for r, s in hand[1:])
    return ', '.join(f'{r} of {s}' for r, s in hand)

def main():
    deck = Deck()
    player = [deck.deal(), deck.deal()]
    dealer = [deck.deal(), deck.deal()]

    while True:
        print(f'Dealer: {format_hand(dealer, hide_first=True)}')
        print(f'Player: {format_hand(player)} (Total: {hand_value(player)})')
        if hand_value(player) == 21:
            print('Blackjack! You win!')
            return
        choice = input('Hit or stand? (h/s): ').strip().lower()
        if choice.startswith('h'):
            player.append(deck.deal())
            if hand_value(player) > 21:
                print(f'Player busts with {hand_value(player)}!')
                print(f'Dealer wins with {hand_value(dealer)}.')
                return
        else:
            break

    print(f'Dealer: {format_hand(dealer)} (Total: {hand_value(dealer)})')
    while hand_value(dealer) < 17:
        dealer.append(deck.deal())
        print(f'Dealer hits: {format_hand(dealer)} (Total: {hand_value(dealer)})')

    player_total = hand_value(player)
    dealer_total = hand_value(dealer)
    if dealer_total > 21 or player_total > dealer_total:
        print('You win!')
    elif dealer_total > player_total:
        print('Dealer wins!')
    else:
        print('Push (tie).')

if __name__ == '__main__':
    main()
