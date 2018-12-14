from math import floor
n = int(input())
cards_s = input().split()
cards = [int(s) for s in cards_s]
cards = sorted(cards, reverse = True)
m = floor(n/2)
cards_a = cards[::2]
cards_b = cards[1::2]
print("{}".format(sum(cards_a)-sum(cards_b)))
