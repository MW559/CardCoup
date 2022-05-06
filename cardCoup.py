import random
import tkinter as tk

window = tk.Tk()
window.title('CardCoup - Card Desk')
window.iconbitmap('C:/Users/myahw/PycharmProjects/SDEV 140/Final Project/cardCoup')
window.geometry("950x550")
window.configure(background="#68A7AD")

main_label = tk.Label(window, text="Welcome to Card Coup!")


# Shuffle the Cards
def shuffle():
    # Defining Our Deck
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = range(2, 15)
    # 11 = Jack, 12 = Queen, 13 = King, 14 = Ace

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')
    # how many cards in decks
    print(len(deck))

    # Create the Players
    global dealer, player
    dealer = []
    player = []

    # Grab Cards for Dealer
    card = random.choice(deck)
    # Removes the Cards from Deck
    deck.remove(card)
    # Append the Cards to Dealer
    dealer.append(card)
    # Append the Cards to Player
    dealer_label.config(text=card)

    # Grab Cards for Player
    card = random.choice(deck)
    # Removes the Cards from Deck
    deck.remove(card)
    # Append the Cards to Dealer
    player.append(card)
    # Append the Cards to Player
    player_label.config(text=card)

    # Count Remaining Cards in Title Bar
    window.title(f'CardCoup - {len(deck)} Cards Left')


# Deal Cards
def deal():
    try:
        # Grab Cards for Dealer
        card = random.choice(deck)
        # Removes the Cards from Deck
        deck.remove(card)
        # Append the Cards to Dealer
        dealer.append(card)
        # Append the Cards to Player
        dealer_label.config(text=card)

        # Grab Cards for Player
        card = random.choice(deck)
        # Removes the Cards from Deck
        deck.remove(card)
        # Append the Cards to Dealer
        player.append(card)
        # Append the Cards to Player
        player_label.config(text=card)

        # Count Remaining Cards in Title Bar
        window.title(f'CardCoup - {len(deck)} Cards Left')

    except:
        window.title('CardCoup - No Cards in Desk')

# Frame:
my_frame = tk.Frame(window, bg="#68A7AD")
my_frame.pack(pady=20)

button_frame = tk.Frame(window, bg="#68A7AD")
button_frame.pack(pady=20)

# Frames for Cards
dealer_frame = tk.LabelFrame(my_frame, text="Dealer", height=600, width= 200, bg="white", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = tk.LabelFrame(my_frame, text="Player", height=600, width= 200, bg="white", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

# Cards in Frames
dealer_label = tk.Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = tk.Label(player_frame, text='')
player_label.pack(pady=20)

# Create Frame for Buttons
shuffle_button = tk.LabelFrame(window, text="Shuffle Deck", height=100, width=75, bg="grey", bd=0)
shuffle_button.grid(column=0, padx=10, ipadx=10)

card_button = tk.LabelFrame(window, text="Get Cards", height=100, width=75, bg="grey", bd=0)
card_button.grid(column=1, ipadx=10)

#  Game Buttons
shuffle_button = tk.Button(button_frame, text="Shuffle Deck", font=("Helvetica", 14), bg="#FFD365", command=shuffle)
shuffle_button.pack(pady=20, x=100, y=20)

card_button = tk.Button(button_frame, text="Get Cards", font=("Helvetica", 14), bg="#FDFFA9", command=deal)
card_button.pack(x=150, y=20, pady=20)

window.mainloop()
