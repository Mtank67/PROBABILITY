suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# we have to find the probability of jack or heart

# we will create the deck of card with wach card being categorise by 2 features 
# its suit: spades , diamonds , hearts or clubs.

deck=[(suit, rank) for suit in suits for rank in ranks]

# now we want all the cards which have the rank as jack
jacks=[card for card in deck if card[1]=='J']
print(f"Number of jacks:{len(jacks)}")
hearts=[card for card in deck if card[0]=='Hearts']
print(f"Number of hearts:{len(hearts)}")
jacks_and_hearts=list(set(jacks).intersection(set(hearts)))
print(f"The intersection of jacks and hearts is {len(jacks_and_hearts)}")

jack_or_hearts=list(set(jacks).union(set(hearts)))
probability=len(jack_or_hearts)/52

print(f"The probability of jack or heart is : {probability:.4f}")