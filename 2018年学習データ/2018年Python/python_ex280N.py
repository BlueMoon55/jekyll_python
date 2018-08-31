# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.


from random import shuffle


class Card:
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]

    values = [None, None,"2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        print("__lt__ ", self.value, c2.value) #debug
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            return self.suit < c2.suit
        return False

    def __gt__(self, c2):
        print("__gt__ ", self.value, c2.value) #debug
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            return self.suit > c2.suit
        return False

    def __repr__(self):
        v = self.values[self.value] +\
            " of " + \
            self.suits[self.suit]
        print("Card__repr__", v) #debug
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                print("Deck Card...", Card(i,j)) #Debug
                self.cards\
                    .append(Card(i,
                                j))
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("p1 name ")
        name2 = input("p2 name ")
        self.deck = Deck()
        print("Game self.deck set:", self.deck) # debug
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def print_winner(self, winner):
        w = "{} wins this round"
        print(w.format(winner.name))

    def print_draw(self, p1, p2):
        d = "{} drew {} {} drew {}"
        print(d.format(
            p1.name, p1.card, p2.name, p2.card))

    def play_game(self):
        print("play_game careds set") # debug
        cards = self.deck.cards
        print("play_game cards:", cards) # debug
        print("beginning War!")
        while len(cards) >= 2:
            print("Left:", len(cards)) # debug
            m = "q to quit. Any " + \
                "key to play:"
            response = input(m)
            if response == 'q':
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.print_draw(self.p1, self.p2)
            print("独自クラスで比較演算", self.p1.card, self.p2.card) #debug
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.print_winner(self.p1)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)

        win = self.winner(self.p1,
                         self.p2)
        print("War is over.{} wins"
              .format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

game = Game()
game.play_game()
