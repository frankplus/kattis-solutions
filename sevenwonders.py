"""
    Solution to Seven Wonders problem: https://open.kattis.com/problems/sevenwonders
    Author: Francesco Pham
    Date: 11/12/2019
"""
s = input()
cards = {"T":0, "C":0, "G":0}
for c in s:
    if c in cards:
        cards[c] += 1

tot = 0
for c in cards:
    tot += cards[c]**2
triples = min(cards['T'], cards['C'], cards['G'])
tot += triples*7
print(tot)