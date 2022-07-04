#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    # returns the sentence lenth and first character
    return (len(sentence), sentence[0])
