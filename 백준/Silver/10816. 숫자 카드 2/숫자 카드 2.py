import sys
from collections import Counter
N = int(sys.stdin.readline())
card = Counter(sys.stdin.readline().split())
M = int(sys.stdin.readline())
M_card = sys.stdin.readline().split()
for m in M_card:
    print(card[m], end = ' ')