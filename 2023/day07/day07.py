data = [i.strip() for i in open('7.in')]

#part 1  erase all joker lines!!!
#cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
#part 2
cards = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']

rank = [[] for i in range(7)]

for card in data:
  hand, bid = card.split()
  found = []
  p = 0
  jok = hand.count('J')
  for c in cards:
    count = hand.count(c)
    if count > 1:
      found.append((c,count))
      if count == 5:  p = 6  #five of a kind
      if count == 4:         #four of a kind
        if jok == 0: p = 5
        else: p= 6 
  s = 0
  for f in found: s += f[1]

  if len(found) == 2:  
    if s == 5:  #full house
      if jok == 0: p = 4
      if jok == 3 or jok == 2: p = 6
      if jok == 1: p = 5
    if s == 4:  #two pairs
      if jok == 0: p = 2
      if jok == 2: p = 5
      if jok == 1: p = 4
  
  if len(found) == 1:
    if s == 2:  #pair
      if jok == 0: p = 1
      if jok == 2: p = 3
      if jok == 1: p = 3
    if s == 3:    #three of a kind
      if jok == 0: p = 3
      if jok == 3: p = 5
      if jok == 1: p = 5
  
  if len(found) == 0:  #high card
    if jok == 0: p = 0
    else: p = 1

  rank[p].append((hand,bid,p))

def card_sort(pile):
  for i in range(len(pile)-1):
    for j in range(i+1,len(pile)):
      for k in range(5):
        if cards.index(pile[i][0][k]) > cards.index(pile[j][0][k]):
          pile[i], pile[j] = pile[j], pile[i]
          break
        elif cards.index(pile[i][0][k]) < cards.index(pile[j][0][k]): break
    
for i in range(7): card_sort(rank[i])

all_cards = []
for i in range(7): all_cards += rank[i]

sum = 0
for i,r in enumerate(all_cards): sum += (i+1) * int(r[1])

print(sum)
