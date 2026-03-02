class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        if len(self.cards) < 52:
            print("Cannot shuffle a deck with missing cards.")
            return
        import random
        random.shuffle(self.cards)
    
    def deal(self, num_cards):
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards
    
def main():
    deck = Deck()
    print("Deck created.")
    
    deck.shuffle()
    print("Deck shuffled.")
    
    num_cards = int(input("Enter the number of cards to deal: "))
    dealt_cards = deck.deal(num_cards)
    
    print("Dealt cards:")
    for card in dealt_cards:
        print(card)

if __name__ == "__main__":
    main()