def draw_cards(*args, **kwargs):
    monster_cards = []
    spell_cards = []

    for card_name, card_type in args:
        if card_type == "monster":
            monster_cards.append(card_name)
        elif card_type == "spell":
            spell_cards.append(card_name)

    for card_name, card_type in kwargs.items():
        if card_type == "monster":
            monster_cards.append(card_name)
        elif card_type == "spell":
            spell_cards.append(card_name)

    monster_cards.sort(reverse=True)
    spell_cards.sort()

    output = ""
    if monster_cards:
        output += "Monster cards:\n"
        for monster in monster_cards:
            output += f"  ***{monster}\n"

    if spell_cards:
        output += "Spell cards:\n"
        for spell in spell_cards:
            output += f"  $$${spell}\n"

    return output


print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
