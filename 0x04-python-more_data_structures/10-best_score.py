#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None 

    fin_max = max(a_dictionary, key=a_dictionary.get)
    return fin_max
