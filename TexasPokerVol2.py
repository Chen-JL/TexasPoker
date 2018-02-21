import random
import itertools

poker = ['2S', '2C', '2D', '2H',
         '3S', '3C', '3D', '3H',
         '4S', '4C', '4D', '4H',
         '5S', '5C', '5D', '5H',
         '6S', '6C', '6D', '6H',
         '7S', '7C', '7D', '7H',
         '8S', '8C', '8D', '8H',
         '9S', '9C', '9D', '9H',
         'OS', 'OC', 'OD', 'OH',
         'JS', 'JC', 'JD', 'JH',
         'QS', 'QC', 'QD', 'QH',
         'KS', 'KC', 'KD', 'KH',
         'AS', 'AC', 'AD', 'AH']
hand0 = random.sample(poker, 2)
hand1 = random.sample(poker, 5)
hand2 = random.sample(poker, 5)
for i in poker:
    if i in hand0:
        poker.remove(i)
public = random.sample(poker, 5)
itertools.combinations(public, 3)
choose = [_ for _ in itertools.combinations(public, 3)]
list0 = []
for i in choose:
    i = i + tuple(hand0)
    list0.append(i)


def card_ranks(cards):
    ranks = ['0123456789OJQKA'.index(r) for r, s in cards]
    ranks.sort(reverse=True)
    return ranks


def judge_straight(cards):
    ranks = card_ranks(cards)
    return (max(ranks)-min(ranks)) == 4 and len(set(ranks)) == 5


def judge_suit(cards):
    suit = [s for r, s in cards]
    return len(set(suit)) == 1


def judge_same(n, ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def judge_double(ranks):
    first = judge_same(2, ranks)
    second = judge_same(2, list(reversed(ranks)))
    if first and second != first:
        return first, second
    else:
        return None


def hand_rank(hand):

    ranks = card_ranks(hand)

    if judge_straight(hand) and judge_suit(hand):
        return 9, max(ranks)
    elif judge_same(4, ranks):
        return 8, judge_same(4, ranks), judge_same(1, ranks)
    elif judge_same(3, ranks) and judge_same(2, ranks):
        return 7, judge_same(3, ranks), judge_same(2, ranks)
    elif judge_suit(hand):
        return 6, ranks
    elif judge_straight(hand):
        return 5, max(ranks)
    elif judge_same(3, ranks):
        return 4, judge_same(3, ranks), ranks
    elif judge_double(ranks):
        return 3, judge_double(ranks), ranks
    elif judge_same(2, ranks):
        return 2, judge_same(2, ranks), ranks
    else:
        return 1, ranks


def compare(hands):
    return max(hands, key=hand_rank)


print(compare([list0[0], list0[1], list0[2], list0[3], list0[4], list0[5], list0[6], list0[7], list0[8], list0[9]]))
