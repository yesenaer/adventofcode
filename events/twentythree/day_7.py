from pathlib import Path


RESOURCES_DIR = Path(__file__).parent / 'resources'


def first_assignment():
    result = 0
    with open(RESOURCES_DIR / 'day7_input.txt') as file:
        hands = {'five-of-a-kind': [], 'four-of-a-kind': [], 'full-house': [], 'three-of-a-kind': [], 'two-pair': [],
                 'one-pair': [], 'high-card': []}
        for line in file:
            line = line.replace('T', 'V')
            line = line.replace('J', 'W')
            line = line.replace('Q', 'X')
            line = line.replace('K', 'Y')
            line = line.replace('A', 'Z')
            splits = line.split()
            cards = splits[0]
            bid = int(splits[1])

            hands = determine_hand(bid, cards, hands)

        for hand in hands.values():
            hand.sort()

        bid_index = 1
        order_of_rank = ['high-card', 'one-pair', 'two-pair', 'three-of-a-kind', 'full-house', 'four-of-a-kind', 'five-of-a-kind']
        for type in order_of_rank:
            for index, x in enumerate(hands[type]):
                win = x[1] * bid_index
                result += win
                hands[type][index] = x + (bid_index, win)
                bid_index += 1



        # print(hands)



    return result


def determine_hand(bid, cards, hands):
    unique_cards = set()
    for card in cards:
        unique_cards.add(card)
    if len(unique_cards) == 1:
        hands['five-of-a-kind'].append((cards, bid))

    elif len(unique_cards) == 2:
        # four of a kind or full house
        for i in unique_cards:
            total = cards.count(i)
            if total == 4:
                hands['four-of-a-kind'].append((cards, bid))
            elif total == 2:
                hands['full-house'].append((cards, bid))

    elif len(unique_cards) == 3:
        for i in unique_cards:
            total = cards.count(i)
            if total == 3:
                hands['three-of-a-kind'].append((cards, bid))
                # break
            elif total == 2:
                hands['two-pair'].append((cards, bid))
                break

    elif len(unique_cards) == 4:
        hands['one-pair'].append((cards, bid))

    elif len(unique_cards) == 5:
        hands['high-card'].append((cards, bid))

    return hands


def determine_hand_part2(bid, cards, hands):
    unique_cards = set()
    for card in cards:
        unique_cards.add(card)

    if len(unique_cards) == 1:
        hands['five-of-a-kind'].append((cards, bid))

    elif len(unique_cards) == 2:
        # four of a kind or full house
        for index, i in enumerate(unique_cards):
            if index == 0:
                total = cards.count(i)
        if 'W' in unique_cards:
            hands['five-of-a-kind'].append((cards, bid))

        elif total == 4:
            hands['four-of-a-kind'].append((cards, bid))

        elif total == 2:
            hands['full-house'].append((cards, bid))


    elif len(unique_cards) == 3:
        for i in unique_cards:
            total = cards.count(i)
            if total == 3:
                if 'W' in unique_cards:
                    hands['four-of-a-kind'].append((cards, bid))
                else:
                    hands['three-of-a-kind'].append((cards, bid))
                break
            elif total == 2:
                if 'W' in unique_cards:
                    if cards.count('W') == 2:
                        hands['four-of-a-kind'].append((cards, bid))
                    else:
                        hands['full-house'].append((cards, bid))
                else:
                    hands['two-pair'].append((cards, bid))
                break

    elif len(unique_cards) == 4:
        if 'W' in unique_cards:
            hands['three-of-a-kind'].append((cards, bid))
        else:
            hands['one-pair'].append((cards, bid))

    elif len(unique_cards) == 5:
        if 'W' in unique_cards:
            hands['one-pair'].append((cards, bid))
        else:
            hands['high-card'].append((cards, bid))

    return hands


def second_assignment():
    result = 0
    with open(RESOURCES_DIR / 'day7_input.txt') as file:
        hands = {'five-of-a-kind': [], 'four-of-a-kind': [], 'full-house': [], 'three-of-a-kind': [], 'two-pair': [],
                 'one-pair': [], 'high-card': []}
        for line in file:
            line = line.replace('T', 'V')
            line = line.replace('J', 'W')
            line = line.replace('Q', 'X')
            line = line.replace('K', 'Y')
            line = line.replace('A', 'Z')
            splits = line.split()
            cards = splits[0]
            bid = int(splits[1])

            hands = determine_hand_part2(bid, cards, hands)

        for hand in hands.values():
            hand.sort()

        bid_index = 1
        order_of_rank = ['high-card', 'one-pair', 'two-pair', 'three-of-a-kind', 'full-house', 'four-of-a-kind', 'five-of-a-kind']
        for type in order_of_rank:
            for index, x in enumerate(hands[type]):
                win = x[1] * bid_index
                result += win
                hands[type][index] = x + (bid_index, win)
                bid_index += 1
        print(hands['three-of-a-kind'])

    return result


print(f'answer to assignment 1 is: {first_assignment()}')  # 251029473
print(f'answer to assignment 2 is: {second_assignment()}')  # 264564931 too high  206475337 too low
