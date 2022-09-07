#!/usr/bin/python3
def best_score(a_dictionary):
    scores = 0
    winner = None
    if type(a_dictionary) is dict:
        for (name, score) in a_dictionary.items():
            if score > scores:
                scores = score
                winner = name
    return winner
