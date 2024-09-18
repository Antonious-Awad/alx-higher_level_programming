#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    winner = ''
    for key, val in a_dictionary:
        if val > best:
            best = val
            winner = key

    return winner
