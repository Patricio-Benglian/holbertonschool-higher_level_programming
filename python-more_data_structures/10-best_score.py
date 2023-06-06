#!/usr/bin/python3
def best_score(a_dictionary):
    top = {'Name': 0, 'Score': 0}
    if a_dictionary:
        for key, value in a_dictionary.items():
            if top['Name'] == 0 or value > top['Score']:
                top['Name'] = key
                top['Score'] = value
    return top['Name'] or None
