import random
import pandas as pd

# class Card:
#     def __init__(self, value):
#         self.value = self.VALUES[value % 13]

DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1]

UN_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

# def deal_card(deck):
#     return VALUES[deck.pop(random.randrange(len(deck))) % 13]

# def deal_round(n_players = 1, n_decks = 6):
#     if n_players < 1 or n_players > 7:
#         raise Exception("Error: Invalid number of players (1 - 7)")

#     deck = [i for i in range(54 * n_decks)]

#     hands = {}

#     hands["dealer"] = [deal_card(deck)]
#     hands["dealer"].append(deal_card(deck))

#     for i in range(n_players):
#         hands[i] = [deal_card(deck)]
#         hands[i].append(deal_card(deck))
    
#     return hands

def printStrategy(strategy):
    for table in strategy:
        print(table + ":")
        print(strategy[table])
        print()



def evaluateCase(table, pc, dc):
    if table == "PAIR_SPLITTING":
        return "SPLIT"
    elif table == "SOFT_TOTALS":
        return "HIT"
    elif table == "HARD_TOTALS":
        return "HIT"
    else:
        raise Exception("Invalid case type")

def buildGrid():
    strategy = {
        "HARD_TOTALS": pd.DataFrame(columns = UN_VALUES, index = range(20, 3, -1)),
        # "SOFT_TOTALS": pd.DataFrame(columns = UN_VALUES, index = range(10, 1, -1)),
        # "PAIR_SPLITTING": pd.DataFrame(columns = UN_VALUES, index = UN_VALUES[::-1])
    }

    for table in strategy:
        for pc in strategy[table].index:
            for dc in strategy[table].columns:
                strategy[table].at[pc, dc] = evaluateCase(table, pc, dc)
    
    printStrategy(strategy)
        
    return strategy


def main():
    buildGrid()


if __name__ == "__main__":
    main()