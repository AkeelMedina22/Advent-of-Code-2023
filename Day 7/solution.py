"""
Apologies in advance for the messy code, 
I was running short on time and this was surprisingly tricky to solve.
"""

import multiprocessing
from typing import List

CPU_COUNT = multiprocessing.cpu_count()

card_strengths_p1 = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
card_strengths_p2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

hands = {
    7: (5,),
    6: (4, 1),
    5: (3, 2),
    4: (3, 1, 1),
    3: (2, 2, 1),
    2: (2, 1, 1, 1),
    1: (1, 1, 1, 1, 1),
}


def task_p1(data: List[str]) -> List[int]:
    hand_rank = []
    for card in data:
        hand = tuple(sorted([card.count(i) for i in list(set(card))], reverse=True))
        hand_rank.append(list(hands.keys())[list(hands.values()).index(hand)])

    ranked = []
    for cards in sorted(list(set(hand_rank)), reverse=True):
        if hand_rank.count(cards) == 1:
            ranked.append(data[hand_rank.index(cards)])
        else:
            card_data = [data[i] for i, x in enumerate(hand_rank) if x == cards]

            def card_max(card_data: List[str], i: int) -> str:
                strengths = [card_strengths_p1.index(card[i]) for card in card_data]
                if strengths.count(max(strengths)) <= 1:
                    return card_data[strengths.index(max(strengths))]
                else:
                    cards = [
                        card_data[i]
                        for i, x in enumerate(strengths)
                        if x == max(strengths)
                    ]
                    return card_max(cards, i + 1)

            while card_data:
                card_to_pop = card_max(card_data, 0)
                ranked.append(card_to_pop)
                card_data.pop(card_data.index(card_to_pop))

    return [data.index(i) for i in ranked]


def part_1() -> None:
    with open("data/data.txt", "r") as f:
        data = f.read().splitlines()

    cards = [line.split(" ")[0] for line in data]
    bids = [int(line.split(" ")[1]) for line in data]

    results: List[int] = task_p1(cards)

    bids = [bids[i] for i in results]

    result = 0
    rank = 1
    for i in range(len(results) - 1, -1, -1):
        result += bids[i] * rank
        rank += 1

    print(f"Part 1 Solution: {result}")


def task_p2(data: List[str]) -> List[int]:
    hand_rank = []
    for card in data:
        if 'J' in card and card != "JJJJJ":
            max_strength = max([card.count(i) for i in list(set(card)) if i != 'J'])
            for i in card:
                if i != 'J':
                    if card.count(i) == max_strength:
                        letter = i
            card = card.replace('J', letter)
        hand = tuple(sorted([card.count(i) for i in list(set(card))], reverse=True))
        hand_rank.append(list(hands.keys())[list(hands.values()).index(hand)])

    ranked = []
    for cards in sorted(list(set(hand_rank)), reverse=True):
        if hand_rank.count(cards) == 1:
            ranked.append(data[hand_rank.index(cards)])
        else:
            card_data = [data[i] for i, x in enumerate(hand_rank) if x == cards]

            def card_max(card_data: List[str], i: int) -> str:
                strengths = [card_strengths_p2.index(card[i]) for card in card_data]
                if strengths.count(max(strengths)) <= 1:
                    return card_data[strengths.index(max(strengths))]
                else:
                    cards = [
                        card_data[i]
                        for i, x in enumerate(strengths)
                        if x == max(strengths)
                    ]
                    return card_max(cards, i + 1)

            while card_data:
                card_to_pop = card_max(card_data, 0)
                ranked.append(card_to_pop)
                card_data.pop(card_data.index(card_to_pop))

    return [data.index(i) for i in ranked]


def part_2() -> None:
    with open("data/data.txt", "r") as f:
        data = f.read().splitlines()

    cards = [line.split(" ")[0] for line in data]
    bids = [int(line.split(" ")[1]) for line in data]

    results: List[int] = task_p2(cards)

    bids = [bids[i] for i in results]

    result = 0
    rank = 1
    for i in range(len(results) - 1, -1, -1):
        result += bids[i] * rank
        rank += 1

    print(f"Part 2 Solution: {result}")


if __name__ == "__main__":
    part_1()
    part_2()
