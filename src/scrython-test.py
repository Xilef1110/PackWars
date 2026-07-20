import scrython

# Rate limiting is automatic! No delays needed
cards_to_fetch = ["Lightning Bolt", "Counterspell", "Black Lotus"]

# Fetch indivicual cards
for card_name in cards_to_fetch:
    card = scrython.cards.Named(
        fuzzy=card_name, cache=True
    )  # Automatically rate limited (2/s)
    print(f"{card.name} - {card.set}")


# Fetch all cards based on a scryfall search, then print the uri for their small image
results = scrython.cards.Search(q="set:eoe -type:legendary t:creature", cache=True)
for card in results:
    print(f"{card.name} - {card.image_uris['small']}")
