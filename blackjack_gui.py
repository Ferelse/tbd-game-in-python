# GUI version of Blackjack using pygame

import pygame
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
        return self.cards.pop()

def hand_value(hand):
    total = sum(VALUES[rank] for rank, _ in hand)
    aces = sum(1 for rank, _ in hand if rank == 'A')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def draw_text(screen, text, pos, font, color=(255, 255, 255)):
    surface = font.render(text, True, color)
    screen.blit(surface, pos)

def draw_hand(screen, hand, x, y, font, hide_first=False):
    offset = 0
    for i, card in enumerate(hand):
        if i == 0 and hide_first:
            label = '??'
        else:
            rank, suit = card
            label = f'{rank}{suit[0]}'
        draw_text(screen, label, (x + offset, y), font)
        offset += 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Blackjack')
    font = pygame.font.SysFont(None, 32)

    deck = Deck()
    player = [deck.deal(), deck.deal()]
    dealer = [deck.deal(), deck.deal()]
    running = True
    player_turn = True
    message = ''

    hit_rect = pygame.Rect(50, 400, 100, 40)
    stand_rect = pygame.Rect(200, 400, 100, 40)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                if hit_rect.collidepoint(event.pos):
                    player.append(deck.deal())
                    if hand_value(player) > 21:
                        message = 'Player busts! Dealer wins.'
                        player_turn = False
                elif stand_rect.collidepoint(event.pos):
                    player_turn = False
            elif event.type == pygame.KEYDOWN and player_turn:
                if event.key == pygame.K_h:
                    player.append(deck.deal())
                    if hand_value(player) > 21:
                        message = 'Player busts! Dealer wins.'
                        player_turn = False
                elif event.key == pygame.K_s:
                    player_turn = False

        if not player_turn and not message:
            # Dealer's turn
            while hand_value(dealer) < 17:
                dealer.append(deck.deal())
            player_total = hand_value(player)
            dealer_total = hand_value(dealer)
            if dealer_total > 21 or player_total > dealer_total:
                message = 'You win!'
            elif dealer_total > player_total:
                message = 'Dealer wins!'
            else:
                message = 'Push.'

        screen.fill((0, 100, 0))
        draw_text(screen, f'Dealer ({hand_value(dealer) if not player_turn else "?"})', (50, 50), font)
        draw_hand(screen, dealer, 50, 80, font, hide_first=player_turn)
        draw_text(screen, f'Player ({hand_value(player)})', (50, 200), font)
        draw_hand(screen, player, 50, 230, font)

        pygame.draw.rect(screen, (0, 0, 0), hit_rect)
        pygame.draw.rect(screen, (0, 0, 0), stand_rect)
        draw_text(screen, 'Hit', (hit_rect.x + 25, hit_rect.y + 10), font)
        draw_text(screen, 'Stand', (stand_rect.x + 10, stand_rect.y + 10), font)

        if message:
            draw_text(screen, message, (50, 350), font)

        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()
