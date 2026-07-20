import scrython

# Rate limiting is automatic! No delays needed
cards_to_fetch = ["Lightning Bolt", "Counterspell", "Black Lotus"]

for card_name in cards_to_fetch:
    card = scrython.cards.Named(fuzzy=card_name)  # Automatically rate limited (2/s)
    print(f"{card.name} - {card.set}")

results = scrython.cards.Search(q="set:eoe -type:legendary t:creature")

for card in results:
    print(f"{card.name} - {card.type_line}")
