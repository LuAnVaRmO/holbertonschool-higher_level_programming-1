#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        return sorted(a_dictionary.items())[-1][0]
